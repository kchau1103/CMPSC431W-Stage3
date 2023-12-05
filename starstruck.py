#import modules
from flask import Flask, render_template, request, redirect, url_for, g, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time, timedelta
import pandas as pd
import sqlite3
import hashlib
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#create Flask instance and set template holder
app = Flask(__name__, template_folder='templates')
app.secret_key = 'secretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

#set host
host = 'https://127.0.0.1:5000/'

DATABASE = 'starstuck.db'
#set up database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#initiate the database with the schema
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/success')
def success():
    return 'Registration successful!'

@app.route('/logout')
def logout():
    session.pop('studio_name', None)  # Remove the studio name from the session
    return redirect(url_for('login'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/judges')
def judges():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Judges_Score")
    judges = cursor.fetchall()  # Fetches all rows from the Judges_Score table
    return render_template('judges.html', judges=judges)

@app.route('/add_scores', methods=['POST'])
def add_scores():
    # Get data from form
    judge_id = request.form['judge_id']
    order_num = request.form['order_num']
    score = request.form['score']

    # Insert data into database
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO Judges_Score (judge_id, order_num, score) VALUES (?, ?, ?)", (judge_id, order_num, score))
    db.commit()
    cursor.close()

    # Redirect back to judges page
    return redirect(url_for('judges'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        studio_name = request.form['studio']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Studio WHERE studio_name = ?", (studio_name,))
        studio = cursor.fetchone()

        if studio:
            session['studio_name'] = studio_name
            return redirect(url_for('login_choices'))
        else:
            flash('No such studio found. Please try again.', 'error')
    return render_template('login.html')

@app.route('/login_choices')
def login_choices():
    if 'studio_name' in session:
        # Pass the studio name to the template if needed
        return render_template('loginChoices.html', studio_name=session['studio_name'])
    else:
        return redirect(url_for('login'))

@app.route('/register_studio', methods=['GET', 'POST'])
def register_studio():
    if request.method == 'POST':
        # Process the form data
        studio_name = request.form['studio_name']
        state = request.form['state']
        city = request.form['city']
        # ... process other form fields ...

        # Insert data into the database
        db = get_db()
        cursor = db.cursor()
        # Make sure your SQL query matches the database schema
        cursor.execute("INSERT INTO Studio (studio_name, state, city) VALUES (?, ?, ?)", (studio_name, state, city))
        db.commit()
        cursor.close()

        # Redirect to the success page after successful form submission
        return redirect(url_for('success'))

    # Render the form page for GET request
    return render_template('registerStudio.html')

@app.route('/schedule')
def schedule():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Schedule")
    schedules = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('schedule.html', schedules=schedules)

def get_size_category(age_group):
    age_category_map = {
        "8-10": "Mini",
        "11-12": "Junior",
        "13-15": "Teen",
        "16-19": "Senior"
    }
    return age_category_map.get(age_group, "Age Group Error")

@app.route('/register_pieces', methods=['GET', 'POST'])
def register_pieces():
    if request.method == 'POST':
        song = request.form.get('song')
        duration = request.form.get('duration')
        style = request.form.get('style')
        age_group = request.form.get('ageGroup')
        size_category = get_size_category(age_group)
        first_name = request.form.getlist('fname[]')
        last_name = request.form.getlist('lname[]')
        age = request.form.getlist('age[]')
        gender = request.form.getlist('gender[]')
        num_dancers = request.form.get('numDancers')
        registration_status = "Registered"

        studio_name = session.get('studio_name')
        if studio_name is None:
            return redirect(url_for('login'))

        if age:
            int_ages = [int(a) for a in age if a.isdigit()]
            avg_age = sum(int_ages) / len(int_ages) if int_ages else 0
        else:
            avg_age = 0

        studio_name = session.get('studio_name')
        amount_due = 100  # $100 charge for piece registration
        registration_status = "Registered"
        payment_status = "Pending"
        paid = 0  # False, as the payment is just initiated
        
        db = get_db()
        cursor = db.cursor()

        # Insert the payment entry into the Payment table
        cursor.execute("""
            INSERT INTO Payment (registration_status, studio_name, amount_due, paid, payment_status)
            VALUES (?, ?, ?, ?, ?)
            """, (registration_status, studio_name, amount_due, paid, payment_status))
        db.commit()

        cursor.execute("""
            INSERT INTO Piece (studio_name, size_category, age_group, style, song) 
            VALUES (?, ?, ?, ?, ?)
            """, (studio_name, size_category, age_group, style, song))
        db.commit()

        duration_str = request.form.get('duration')  # Assuming 'duration' is in the format 'HH:MM:SS'
        h, m, s = map(int, duration_str.split(':'))
        song_duration = h * 60 + m  # Convert to total minutes

        cursor.execute("SELECT MAX(call_time) FROM Schedule WHERE date = CURRENT_DATE")
        last_call_time = cursor.fetchone()[0]

        # Convert last_call_time from string to time object, if it is not None
        if last_call_time is not None:
            # Assuming last_call_time is in format "HH:MM:SS"
            last_call_time_obj = datetime.strptime(last_call_time, '%H:%M:%S').time()
        else:
            last_call_time_obj = None

        # Calculate next call time
        if last_call_time_obj is None:
            next_call_time = time(8, 0)  # Start at 8 AM if no entries for the day
        else:
            # Increment by the song's duration
            full_datetime = datetime.combine(datetime.today(), last_call_time_obj)
            next_call_time = (full_datetime + timedelta(minutes=song_duration)).time()

        # Convert next_call_time to a string format
        next_call_time_str = next_call_time.strftime('%H:%M:%S')

        # Insert into Schedule table
        cursor.execute("""
            INSERT INTO Schedule (date, call_time, song)
            VALUES (CURRENT_DATE, ?, ?)
            """, (next_call_time_str, song))
        db.commit()

        for i in range(len(first_name)):
            full_name = first_name[i] + " " + last_name[i]
            cursor.execute("""
                INSERT INTO Dancer (studio_name, name, age, gender) 
                VALUES (?, ?, ?, ?)
                """, (studio_name, full_name, age[i], gender[i]))
        db.commit()

        cursor.execute("""
            INSERT INTO Set_List (studio_name, num_dancers, style, registration_status, song_duration, avg_age, song)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (studio_name, num_dancers, style, registration_status, duration, avg_age, song))
       
        db.commit()
        cursor.close()
        return redirect(url_for('success'))
    return render_template('registerPieces.html')

@app.route('/add_payment', methods=['POST'])
def add_payment():
    payment_id = request.form.get('paymentId')
    pay_amount = request.form.get('payamount')

    if not payment_id or not pay_amount:
        flash("Please enter both payment ID and amount.", "error")
        return redirect(url_for('my_payments'))

    studio_name = session.get('studio_name')
    if not studio_name:
        return redirect(url_for('login'))

    try:
        pay_amount = float(pay_amount)
    except ValueError:
        flash("Invalid payment amount entered.", "error")
        return redirect(url_for('my_payments'))

    db = get_db()
    cursor = db.cursor()

    # Fetch the current amount due for the given payment ID
    cursor.execute("SELECT amount_due FROM Payment WHERE payment_id = ? AND studio_name = ?", (payment_id, studio_name))
    result = cursor.fetchone()

    if result:
        current_amount_due = result[0]
        if pay_amount <= current_amount_due:
            new_amount_due = current_amount_due - pay_amount
            paid_status = new_amount_due <= 0
            cursor.execute("UPDATE Payment SET amount_due = ?, paid = ? WHERE payment_id = ?", 
                           (new_amount_due, paid_status, payment_id))
            db.commit()
            flash('Payment successful!', 'success')
        else:
            flash('Payment amount exceeds the amount due.', 'error')
    else:
        flash('Payment ID not found or does not belong to your studio.', 'error')

    cursor.close()
    return redirect(url_for('my_payments'))

@app.route('/my_payments', methods=['GET'])
def my_payments():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))

    db = get_db()
    cursor = db.cursor()

    # Fetch all payments for the studio
    cursor.execute("SELECT * FROM Payment WHERE studio_name = ?", (studio_name,))
    payments = cursor.fetchall()
    cursor.close()
    print(payments)
    return render_template('myPayments.html', payments=payments)

@app.route('/my_setlist')
def my_setlist():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))  # Redirect to login if studio name is not in session
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Set_List WHERE studio_name = ?", (studio_name,))
    setlists = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('mySetlist.html', setlists=setlists)

@app.route('/my_pieces')
def my_pieces():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))  # Redirect to login if studio name is not in session
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Piece WHERE studio_name = ?", (studio_name,))
    pieces = cursor.fetchall()
    return render_template('myPieces.html', pieces=pieces)

@app.route('/my_dancers')
def my_dancers():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))  # Redirect to login if studio name is not in session
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Dancer WHERE studio_name = ?", (studio_name,))
    dancers = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('myDancers.html', dancers=dancers)

@app.route('/edit_dancers', methods=['GET', 'POST'])
def edit_dancers():
    dancer_name = request.args.get('name')  # Get the dancer name from URL parameters
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        new_age = request.form.get('age')
        new_gender = request.form.get('gender')
        cursor.execute("UPDATE Dancer SET age = ?, gender = ? WHERE name = ?", (new_age, new_gender, dancer_name))
        db.commit()
        return redirect(url_for('success'))

    cursor.execute("SELECT * FROM Dancer WHERE name = ?", (dancer_name,))
    dancer = cursor.fetchone()
    cursor.close()
    return render_template('editDancers.html', dancer=dancer)

@app.route('/select_dancer_edit', methods=['GET', 'POST'])
def select_dancer_edit():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))

    # Handle the POST request from the form submission
    if request.method == 'POST':
        selected_dancer_name = request.form.get('dancer')
        return redirect(url_for('edit_dancers', name=selected_dancer_name))

    # Handle the GET request to display the form
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM Dancer WHERE studio_name = ?", (studio_name,))
    dancers = cursor.fetchall()
    cursor.close()

    return render_template('selectEditDancer.html', dancers=dancers)

@app.route('/my_adjudications')
def my_adjudications():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Adjudication")
    adjudications = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('myAdjudications.html', adjudications=adjudications)

@app.route('/my_schedule')
def my_schedule():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))  # Redirect to login if studio name is not in session
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Schedule")
    schedules = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('mySchedule.html', schedules=schedules)

if __name__ == '__main__':
    init_db() # initialize the database
    app.run(debug=True, port=5001)  # Runs on http://127.0.0.1:5000 by default



# -- Retrieve all pieces in a specific age group
# SELECT * FROM Piece WHERE age_group = 'specific_age_group';

# -- Retrieve all pieces in a specific size category
# SELECT * FROM Piece WHERE size_category = 'specific_size_category';

# -- Retrieve all pieces that received a specific award
# SELECT * FROM Piece WHERE award_nameFK = 'specific_award';

# -- Retrieve all pieces in a specific genre
# SELECT * FROM Set_List WHERE style = 'specific_genre';

# -- Retrieve all scores for a specific piece
# SELECT * FROM Judges_Score WHERE order_numFK = 'specific_piece_order';

# -- Retrieve adjudication for a specific piece
# SELECT * FROM Adjudication WHERE order_numFK = 'specific_piece_order';

# -- Retrieve the schedule for a specific studio on a given date
# SELECT * FROM Schedule WHERE studio_nameFK = 'specific_studio' AND date = 'specific_date';

# -- Update dancer info
# UPDATE Dancer SET age = 'new_age', gender = 'new_gender' WHERE studio_nameFK = 'specific_studio' AND name = 'specific_dancer';

# -- Remove a dancer from a specific piece
# DELETE FROM Dancer WHERE studio_nameFK = 'specific_studio' AND name = 'specific_dancer' AND order_numFK = 'specific_piece_order';

# -- Insert a new studio
# INSERT INTO Studio (studio_name, city, state) VALUES ('new_studio', 'city_name', 'state_name');

# -- Insert a new dancer
# INSERT INTO Dancer (studio_nameFK, name, age, gender) VALUES ('specific_studio', 'new_dancer', 'age_value', 'gender_value');

# -- Insert judges' scores for a specific piece
# INSERT INTO Judges_Score (order_numFK, judge_id, score) VALUES ('specific_piece_order', 'judge_id_value', 'score_value');

# – Insert a new payment
# INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status)
# VALUES (1, 'Registered', 'StudioABC', 500.00, 0, 'Pending');

# – Insert a new set list
# INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song)
# VALUES (101, 'StudioABC', 5, 'Contemporary', 'Registered', '00:04:30', 20, 'SongXYZ');

# – Insert a new schedule
# INSERT INTO Schedule (order_num, date, call_time, song)
# VALUES (201, '2023-01-15', '14:00:00', 'SongXYZ');

# – Insert a new piece
# INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name)
# VALUES (201, 'StudioABC', 'Large', 'Adult', 'Contemporary', 'SongXYZ', 'Best Performance');

# – Update payment status after the payment is made
# UPDATE Payment
# SET paid = 1, payment_status = 'Completed'
# WHERE payment_id = 1;

# – Retrieve all pieces and their adjudications for a specific studio
# SELECT Piece.*, Adjudication.total_score
# FROM Piece
# LEFT JOIN Adjudication ON Piece.order_num = Adjudication.order_num
# WHERE Piece.studio_name = 'StudioABC';

# – Update payment status to TRUE when the correct amount is paid
# UPDATE Payment
# SET payment_status = TRUE
# WHERE amount_due = paid AND payment_status = FALSE;

# – Update registration status to TRUE when payment status is TRUE
# UPDATE Payment
# SET registration_status = TRUE
# WHERE payment_status = TRUE AND registration_status = FALSE;

# – Given the total_score of a piece, update the award_name
# UPDATE Adjudication
# SET award_name = 
#    CASE 
#       WHEN total_score >= 291.0 AND total_score <= 300 THEN 'Platinum'
#       WHEN total_score >= 282.0 AND total_score <= 290.9 THEN 'High Gold'
#       WHEN total_score >= 273.0 AND total_score <= 281.9 THEN 'Gold'
#       WHEN total_score >= 264.0 AND total_score <= 272.9 THEN 'Silver'
#       WHEN total_score >= 255.0 AND total_score <= 263.9 THEN 'Bronze'
#       ELSE 'Bronze' -- Handle cases where the total score is 254 and below
#    END;

# – Update a piece after they receive an adjudication
# UPDATE Piece
# SET award_name = (
#     SELECT award_name
#     FROM Adjudication
#     WHERE Adjudication.order_num = Piece.order_num
# );

# -- Assuming you have a function or mechanism to generate unique random order numbers
# CREATE FUNCTION GetUniqueRandomOrderNumber() RETURNS INT
# BEGIN
#     DECLARE rand_num INT;
#     -- Your logic to generate a unique random order number goes here
#     -- For example, you can use RAND() * 100000 to generate a random number
#     SET rand_num = CAST(RAND() * 100000 AS INT);
#     RETURN rand_num;
# END;
# – Given a Set_List, reorder it into a single Schedule
# -- Assuming you have a function or mechanism to generate unique random order numbers
# CREATE FUNCTION GetUniqueRandomOrderNumber() RETURNS INT
# BEGIN
#     DECLARE rand_num INT;
#     -- Your logic to generate a unique random order number goes here
#     -- For example, you can use RAND() * 100000 to generate a random number
#     SET rand_num = CAST(RAND() * 100000 AS INT);
#     RETURN rand_num;
# END;

# -- Create a temporary table to store unique random order numbers for each entry
# CREATE TEMPORARY TABLE TempOrderNumbers (
#     entry_num INT,
#     unique_order_num INT
# );

# -- Update TempOrderNumbers with unique random order numbers for entries with TRUE registration status
# INSERT INTO TempOrderNumbers (entry_num, unique_order_num)
# SELECT entry_num, GetUniqueRandomOrderNumber()
# FROM Set_List
# WHERE registration_status = TRUE;

# -- Update Schedule with the unique random order numbers and call times
# UPDATE Schedule
# SET order_num = TempOrderNumbers.unique_order_num,
#     call_time = ADDTIME('00:00:00', RAND() * 3600)
# FROM TempOrderNumbers
# WHERE Schedule.order_num = TempOrderNumbers.entry_num;

# -- Drop the temporary table
# DROP TEMPORARY TABLE IF EXISTS TempOrderNumbers;


# -- Update Piece table based on Schedule and Set_List
# UPDATE Piece
# SET 
#     order_num = Schedule.order_num, -- Update order_num based on Schedule
#     style = Set_List.style, -- Update style based on Set_List
#     studio_name = Set_List.studio_name, -- Update studio_name based on Set_List
#     size_category = 
#         CASE
#             WHEN (Set_List.num_dancers BETWEEN 4 AND 9 AND Set_List.size_category != 'Group') OR
#                  (Set_List.num_dancers BETWEEN 10 AND 15 AND Set_List.size_category != 'Line') OR
#                  (Set_List.num_dancers BETWEEN 16 AND 24 AND Set_List.size_category != 'Extended Line') OR
#                  (Set_List.num_dancers >= 25 AND Set_List.size_category != 'Production')
#             THEN
#                 'Category Error'
#             ELSE
#                 Set_List.size_category -- Update size_category based on Set_List
#         END,
#     age_group =
#         CASE
#             WHEN Set_List.avg_age BETWEEN 8 AND 10 THEN 'Mini'
#             WHEN Set_List.avg_age BETWEEN 11 AND 12 THEN 'Junior'
#             WHEN Set_List.avg_age BETWEEN 13 AND 15 THEN 'Teen'
#             WHEN Set_List.avg_age BETWEEN 16 AND 19 THEN 'Senior'
#             ELSE 'Age Group Error'
#         END
# WHERE Piece.order_num = Schedule.order_num; -- Match entries based on order_num

# -- If there are errors in category or age group, handle accordingly
# -- You can use variables or some other mechanism to track errors
# -- For example, you can define variables category_error and age_group_error earlier in your script
# -- and update them accordingly in the above queries.

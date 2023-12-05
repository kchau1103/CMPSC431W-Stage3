#import modules
from flask import Flask, render_template, request, redirect, url_for, g, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
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
    return render_template('schedule.html')

@app.route('/register_pieces', methods=['GET', 'POST'])
def register_pieces():
    if request.method == 'POST':
        studio_name = request.form.get('studio[]')
        songs = request.form.getlist('song[]')
        durations = request.form.getlist('duration[]')
        styles = request.form.getlist('style[]')
        age_groups = request.form.getlist('ageGroup[]')
        size_categories = request.form.getlist('sizeCategory[]')
        first_names = request.form.getlist('fname[]')
        last_names = request.form.getlist('lname[]')
        ages = request.form.getlist('age[]')
        genders = request.form.getlist('gender[]')
        
        db = get_db()
        cursor = db.cursor()
        # Assuming each list has the same length
        for i in range(len(songs)):
            # Insert each song into the Piece table
            cursor.execute("INSERT INTO Piece (studio_name, size_category, age_group, style, song) VALUES (?, ?, ?, ?, ?)", 
                           (studio_name, size_categories[i], age_groups[i], styles[i], songs[i]))
        
        for i in range(len(first_names)):
            # Combine first and last names to create full name
            full_name = first_names[i] + " " + last_names[i]
            # Insert each dancer into the Dancer table
            cursor.execute("INSERT INTO Dancer (studio_name, name, age, gender) VALUES (?, ?, ?, ?)", 
                           (studio_name, full_name, ages[i], genders[i]))
        db.commit()
        cursor.close()
        return redirect(url_for('success'))
    return render_template('registerPieces.html')

@app.route('/my_payments')
def my_payments():
    return render_template('myPayments.html')

@app.route('/my_pieces')
def my_pieces():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Piece")
    pieces = cursor.fetchall()  # Fetches all rows from the Piece table
    return render_template('myPieces.html', pieces=pieces)

@app.route('/my_dancers')
def my_dancers():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Dancer")
    dancers = cursor.fetchall()  # Fetches all rows from the Dancer table
    
    return render_template('myDancers.html', dancers=dancers)

@app.route('/my_adjudications')
def my_adjudications():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Adjudication")
    adjudications = cursor.fetchall()  # Fetches all rows from the Dancer table
    return render_template('myAdjudications.html', adjudications=adjudications)

if __name__ == '__main__':
    init_db() # initialize the database
    app.run(debug=True, port=5001)  # Runs on http://127.0.0.1:5000 by default



# -- Retrieve all payments for a specific studio
# SELECT * FROM Payment WHERE studio_nameFK = 'specific_studio';

# -- Retrieve all dancers from a specific studio
# SELECT * FROM Dancer WHERE studio_nameFK = 'specific_studio';

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

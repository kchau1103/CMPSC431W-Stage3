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
host = 'http://127.0.0.1:5001/'

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

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        
        # # Execute preset data script
        # with app.open_resource('preset_data.sql', mode='r') as f:
        #     db.cursor().executescript(f.read())

        # db.commit()

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
    judge_id = request.form['judge_id']
    order_num = request.form['order_num']
    score = request.form['score']

    try:
        score = int(score)
        if 0 <= score <= 100:
            db = get_db()
            cursor = db.cursor()

            # Start a transaction
            cursor.execute("BEGIN;")

            # Check if the order number exists
            cursor.execute("SELECT COUNT(*) FROM Piece WHERE order_num = ?", (order_num,))
            if cursor.fetchone()[0] == 0:
                db.rollback()  # Rollback if order number does not exist
                flash('Order number does not exist.', 'error')
                return redirect(url_for('judges'))

            # Check if this judge has already scored this order number
            cursor.execute("SELECT COUNT(*) FROM Judges_Score WHERE order_num = ? AND judge_id = ?", (order_num, judge_id))
            if cursor.fetchone()[0] > 0:
                db.rollback()
                flash('This judge has already scored this order number.', 'error')
                return redirect(url_for('judges'))

            # Check the total number of scores for this order number
            cursor.execute("SELECT COUNT(*) FROM Judges_Score WHERE order_num = ?", (order_num,))
            if cursor.fetchone()[0] >= 3:
                db.rollback()
                flash('This order number already has 3 scores.', 'error')
                return redirect(url_for('judges'))

            # Insert the new score
            cursor.execute("INSERT INTO Judges_Score (judge_id, order_num, score) VALUES (?, ?, ?)", (judge_id, order_num, score))

            # Commit the transaction if all checks pass
            db.commit()
            flash('Score added successfully.', 'success')
        else:
            flash('Score must be between 0 and 100.', 'error')
    except ValueError:
        flash('Invalid input for score.', 'error')

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
        registration_status = 0
        payment_status = "Pending"
        paid = 0  # False, as the payment is just initiated
        
        db = get_db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO Piece (studio_name, size_category, age_group, style, song) 
            VALUES (?, ?, ?, ?, ?)
            """, (studio_name, size_category, age_group, style, song))
        db.commit()

        order_num = cursor.lastrowid
        order_num = int(order_num) 
        cursor.execute("""
            INSERT INTO Adjudication (order_num)
            VALUES (?)
            """, (order_num,))
        db.commit()

        # Insert the payment entry into the Payment table
        cursor.execute("""
            INSERT INTO Payment (registration_status, studio_name, amount_due, paid, payment_status)
            VALUES (?, ?, ?, ?, ?)
            """, (registration_status, studio_name, amount_due, paid, payment_status))
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
                INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
                VALUES (?, ?, ?, ?, ?)
                """, (studio_name, full_name, age[i], gender[i], order_num))
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
    try:
        cursor.execute("SELECT amount_due, paid FROM Payment WHERE payment_id = ? AND studio_name = ?", (payment_id, studio_name))
        result = cursor.fetchone()

        if result:
            current_amount_due, already_paid = result

            # Start a transaction
            cursor.execute("BEGIN;")

            if pay_amount <= current_amount_due and not already_paid:
                new_amount_due = current_amount_due - pay_amount
                paid_status = new_amount_due <= 0
                payment_status = "Paid" if paid_status else "Pending"

                # Update paid status, registration status, and payment status
                cursor.execute("UPDATE Payment SET amount_due = ?, paid = ?, registration_status = ?, payment_status = ? WHERE payment_id = ?", 
                               (new_amount_due, paid_status, paid_status, payment_status, payment_id))

                # Update registration status in Set_List table if payment is completed
                if paid_status:
                    cursor.execute("UPDATE Set_List SET registration_status = TRUE WHERE studio_name = ?", (studio_name,))

                # Commit if the payment amount is correct
                db.commit()
                flash('Payment successful!', 'success')
            else:
                # Rollback the transaction if the payment amount is incorrect
                db.rollback()
                flash('Payment amount exceeds the amount due or payment already completed.', 'error')
        else:
            flash('Payment ID not found or does not belong to your studio.', 'error')
            db.rollback()
    except Exception as e:
        db.rollback()
        flash(f"An error occurred: {e}", "error")
    finally:
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

# Route to display the form for deleting dancers
@app.route('/select_delete_dancer', methods=['GET', 'POST'])
def select_delete_dancer():
    studio_name = session.get('studio_name')
    if studio_name is None:
        return redirect(url_for('login'))

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM Dancer WHERE studio_name = ?", (studio_name,))
    dancers = cursor.fetchall()
    cursor.close()

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Piece")  # Fetch pieces
    pieces = cursor.fetchall()
    cursor.close()

    return render_template('deleteDancers.html', dancers=dancers, pieces=pieces)

# Route to handle the deletion of dancers
@app.route('/delete_dancer', methods=['POST'])
def delete_dancer():
    dancer_to_delete = request.form['dancer_to_delete']
    piece_to_delete = request.form['ordernum_to_delete']

    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Dancer WHERE name = ? AND order_num = ?", (dancer_to_delete, piece_to_delete))
    db.commit()
    cursor.close()

    flash('Dancer successfully deleted from the piece!', 'success')
    return redirect(url_for('select_delete_dancer'))

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

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Piece")  # Fetch pieces
    pieces = cursor.fetchall()
    cursor.close()

    return render_template('selectEditDancer.html', dancers=dancers, pieces=pieces)

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
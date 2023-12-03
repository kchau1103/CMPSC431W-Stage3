from flask import Flask, render_template
from database import insert_piece

app = Flask(__name__)

@app.route('/')
def register_pieces():
    return render_template('register_pieces.html')


# Route for the form
@app.route('/submit_pieces', methods=['POST'])
def submit_pieces():
    if request.method == 'POST':
        cursor = db_connection.cursor()

        # Get form data
        studio = request.form['studio']
        song = request.form['song']
        duration = request.form['duration']
        style = request.form['style']
        ageGroup = request.form['ageGroup']
        sizeCategory = request.form['sizeCategory']
        fname = request.form.getlist('fname')
        lname = request.form.getlist('lname')
        age = request.form.getlist('age')
        gender = request.form.getlist('gender')

        # Insert data into Set_List table
        insert_set_list_query = "INSERT INTO Set_List (studio_name, song, song_duration, style, age_group, size_category) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_set_list_query, (studio, song, duration, style, ageGroup, sizeCategory))
        db_connection.commit()

        # Insert data into Dancer table
        insert_dancer_query = "INSERT INTO Dancer (studio_name, name, age, gender) VALUES (%s, %s, %s, %s)"
        for i in range(len(fname)):
            name = fname[i] + ' ' + lname[i]
            cursor.execute(insert_dancer_query, (studio, name, age[i], gender[i]))
            db_connection.commit()

        cursor.close()

        # Redirect to success page
        return redirect('/success')  # Change this to the appropriate success page URL





@app.route('/submit_piece', methods=['POST'])
def submit_piece():
    if request.method == 'POST':
        piece_name = request.form['piece_name']
        # Retrieve other form fields similarly

        # Insert data into the database using the function from database.py
        result = insert_piece(piece_name)

        if result:
            return "Piece registered successfully!"
        else:
            return "Error registering piece."

if __name__ == '__main__':
    app.run(debug=True)



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

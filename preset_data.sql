INSERT INTO Studio (studio_name, city, state) VALUES ('Dance Dynamics', 'Springfield', 'Illinois');
INSERT INTO Studio (studio_name, city, state) VALUES ('Elite Dance Academy', 'Madison', 'Wisconsin');
INSERT INTO Studio (studio_name, city, state) VALUES ('Rhythm Nation', 'Austin', 'Texas');
INSERT INTO Studio (studio_name, city, state) VALUES ('Jazz Hands Studio', 'Orlando', 'Florida');
INSERT INTO Studio (studio_name, city, state) VALUES ('Ballet Elite', 'Denver', 'Colorado');
INSERT INTO Studio (studio_name, city, state) VALUES ('Tap Stars Academy', 'Seattle', 'Washington');

INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song) VALUES (1, 'Dance Dynamics', 10, 'Ballet', 'Registered', '00:03:30', 12, 'Swan Lake');
INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song) VALUES (2, 'Elite Dance Academy', 15, 'Hip-Hop', 'Registered', '00:02:45', 16, 'Street Beats');
INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song) VALUES (3, 'Jazz Hands Studio', 8, 'Jazz', 'Registered', '00:02:30', 10, 'Jazz in Motion');
INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song) VALUES (4, 'Ballet Elite', 12, 'Contemporary', 'Registered', '00:03:00', 14, 'Modern Emotions');

INSERT INTO Schedule (order_num, date, call_time, song) VALUES (1, '2021-08-15', '09:00:00', 'Swan Lake');
INSERT INTO Schedule (order_num, date, call_time, song) VALUES (2, '2021-08-15', '09:05:00', 'Street Beats');
INSERT INTO Schedule (order_num, date, call_time, song) VALUES (3, '2021-08-16', '10:00:00', 'Jazz in Motion');
INSERT INTO Schedule (order_num, date, call_time, song) VALUES (4, '2021-08-16', '10:10:00', 'Modern Emotions');


INSERT INTO Dancer (studio_name, name, age, gender, order_num) VALUES ('Dance Dynamics', 'Emily Stone', 12, 'Female', 1);
INSERT INTO Dancer (studio_name, name, age, gender, order_num) VALUES ('Elite Dance Academy', 'John Doe', 16, 'Male', 2);
INSERT INTO Dancer (studio_name, name, age, gender, order_num) VALUES ('Jazz Hands Studio', 'Lucy Heart', 10, 'Female', 3);
INSERT INTO Dancer (studio_name, name, age, gender, order_num) VALUES ('Ballet Elite', 'Mark Evans', 14, 'Male', 4);


INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (1, 'Dance Dynamics', 'Small Group', 'Junior', 'Ballet', 'Swan Lake', NULL);
INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (2, 'Elite Dance Academy', 'Large Group', 'Senior', 'Hip-Hop', 'Street Beats', NULL);
INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (3, 'Jazz Hands Studio', 'Small Group', 'Mini', 'Jazz', 'Jazz in Motion', NULL);
INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (4, 'Ballet Elite', 'Medium Group', 'Teen', 'Contemporary', 'Modern Emotions', NULL);


INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (1, 101, 92.5);
INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (2, 102, 89.0);
INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (3, 103, 85.0);
INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (4, 104, 90.5);


INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Gold', 1, 275.0);
INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Silver', 2, 267.0);
INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('High Gold', 3, 255.0);
INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Platinum', 4, 281.5);


INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status) VALUES (1, TRUE, 'Dance Dynamics', 200.00, FALSE, 'Pending');
INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status) VALUES (2, TRUE, 'Elite Dance Academy', 300.00, FALSE, 'Pending');
INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status) VALUES (3, TRUE, 'Jazz Hands Studio', 150.00, FALSE, 'Pending');
INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status) VALUES (4, TRUE, 'Ballet Elite', 250.00, FALSE, 'Pending');

INSERT INTO Studio (studio_name, city, state)
VALUES 
    ('Orchesis Dance Company', 'State College', 'Pennsylvania'); 


INSERT INTO Dancer (studio_name, name, age, gender, order_num)
VALUES 
    ('Orchesis Dance Company', 'Jessie Arnold', 19, 'Female', 10), 
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Chesney Dowds', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Madison Duley', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 10), 
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 10), 
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 10), 
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 10), 
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Abby Loureiro', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 10), 
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 10), 
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 10), 
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 10), 
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 10), 
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 10), 
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 10),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 10), 
    ('Orchesis Dance Company', 'Ilysa Sanchez-Perez', 19, 'Female', 10);

-- Inserting Set_List values
INSERT INTO Set_List (entry_num, studio_name, num_dancers, style, registration_status, song_duration, avg_age, song)
VALUES
    (7, 'Orchesis Dance Company', 29, 'Jazz', 'Registered', '00:06:30', 23, 'GAGA'),
    (8, 'Orchesis Dance Company', 8, 'Contemporary', 'Registered', '00:02:30', 22, 'Rivers and Roads'),
    (9, 'Orchesis Dance Company', 8, 'Contemporary', 'Registered', '00:02:30', 24, 'Wolves'),
    (10, 'Orchesis Dance Company', 8, 'Contemporary', 'Registered', '00:02:30', 20, 'Heroes'),
    (11, 'Orchesis Dance Company', 8, 'Modern', 'Registered', '00:02:30', 19, 'Glitter'),
    (12, 'Orchesis Dance Company', 9, 'Contemporary', 'Registered', '00:02:30', 18, 'Strange'),
    (13, 'Orchesis Dance Company', 11, 'Jazz', 'Registered', '00:02:30', 17, 'A Pale'),
    (14, 'Orchesis Dance Company', 29, 'Contemporary', 'Registered', '00:03:30', 16, 'Brightside'),
    (15, 'Orchesis Dance Company', 9, 'Jazz', 'Registered', '00:02:30', 15, 'TNT'),
    (16, 'Orchesis Dance Company', 6, 'Contemporary', 'Registered', '00:02:30', 13, 'All Through the Night'),
    (17, 'Orchesis Dance Company', 5, 'Contemporary', 'Registered', '00:02:30', 11, 'Lovely'),
    (18, 'Orchesis Dance Company', 8, 'Modern', 'Registered', '00:02:30', 9, 'Bottom of the River'),
    (19, 'Orchesis Dance Company', 7, 'Contemporary', 'Registered', '00:02:30', 19, 'The End of Love'),
    (20, 'Orchesis Dance Company', 7, 'Contemporary', 'Registered', '00:02:30', 14, 'Going to California'),
    (21, 'Orchesis Dance Company', 7, 'Contemporary', 'Registered', '00:02:30', 8, 'Not Losing You'),
    (22, 'Orchesis Dance Company', 9, 'Contemporary', 'Registered', '00:02:30', 12, 'When Were Older'),
    (23, 'Orchesis Dance Company', 29, 'Jazz', 'Registered', '00:05:30', 10, 'Merry Christmas');


-- Inserting dancers for Set_List entry with song 'GAGA' and order_num = 7
INSERT INTO Dancer (studio_name, name, age, gender, order_num)
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 19, 'Female', 7),
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 17, 'Female', 7),
    ('Orchesis Dance Company', 'Chesney Dowds', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Madison Duley', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 7),
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 7),
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 7),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 7),
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 7),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 7),
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Abby Loureiro', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 7),
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 7),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 7),
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 7),
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 7),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 7),
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 7),
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 7),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 7);


-- Inserting dancers for Rivers and Roads (order_num = 22)
INSERT INTO Dancer (studio_name, name, age, gender, order_num)
VALUES
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 17, 'Female', 22),
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 22),
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 22),
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 22),
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 22),
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 22),
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 22),
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 22);


-- Order_num = 21
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 18, 'Female', 21),
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 21),
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 21),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 21),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 21),
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 21),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 21);
    -- Add other dancers for order_num = 21


-- Order_num = 20
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Chesney Dowds', 16, 'Female', 20),
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 20),
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 20),
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 20),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 20),
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 20),
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 20),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 20);
    -- Add other dancers for order_num = 20


-- Order_num = 19
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 15, 'Female', 19),
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 19),
    ('Orchesis Dance Company', 'Alex Jaworski', 17, 'Female', 19),
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 19),
    ('Orchesis Dance Company', 'Taylor Malek', 19, 'Female', 19),
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 19),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 19),
    ('Orchesis Dance Company', 'Madison Stewart', 18, 'Female', 19);
-- Add other dancers for order_num = 19


-- Order_num = 18
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 18),
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 18),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 18),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 18),
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 18),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 18),
    ('Orchesis Dance Company', 'Ilysa Sanchez-Perez', 19, 'Female', 18), -- Please provide the age for Ilysa Sanchez-Perez
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 18),
    ('Orchesis Dance Company', 'Lindsey Swanson', 19, 'Female', 18); -- Please provide the age for Lindsey Swanson

-- Order_num = 17
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 19, 'Female', 17),
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 17, 'Female', 17),
    ('Orchesis Dance Company', 'Chesney Dowds', 18, 'Female', 17),
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 17),
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 17),
    ('Orchesis Dance Company', 'Abby Loureiro', 18, 'Female', 17),
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 17),
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 17),
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 17),
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 17),
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 17);


INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 19, 'Female', 16),
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Olivia Ciccarelli', 17, 'Female', 16),
    ('Orchesis Dance Company', 'Chesney Dowds', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Madison Duley', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 16),
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 16),
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 16),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 16),
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Kelsey Jones', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 16),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 16),
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Abby Loureiro', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 16),
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 16),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 16),
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 16),
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 16),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 16),
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 16),
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 16),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 16);


INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Chesney Dowds', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Maggie Fechtman', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Sadie Van Horn', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Abby Loureiro', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Emma McCurdy', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Carley Mykut', 15, 'Female', 15),
    ('Orchesis Dance Company', 'Eva Schulz', 15, 'Female', 15);


-- Inserting dancers for order_num = 13
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 13),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 13),
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 13),
    ('Orchesis Dance Company', 'Taylor Malek', 17, 'Female', 13),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 13),
    ('Orchesis Dance Company', 'Ilysa Sanchez-Perez', 19, 'Female', 13);

-- Inserting dancers for order_num = 11
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 11),
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 11),
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 11),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 11),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 11);


-- Inserting dancers for order_num = 9
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Madison Duley', 15, 'Female', 9),
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 9),
    ('Orchesis Dance Company', 'Abby Loureiro', 18, 'Female', 9),
    ('Orchesis Dance Company', 'Emily Murta', 16, 'Female', 9),
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 9),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 9),
    ('Orchesis Dance Company', 'Madison Stewart', 19, 'Female', 9),
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 9);


-- Inserting dancers for order_num = 14
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Macy Erimias', 16, 'Female', 14),
    ('Orchesis Dance Company', 'Maggie Fechtman', 19, 'Female', 14),
    ('Orchesis Dance Company', 'Madison Kodis', 17, 'Female', 14),
    ('Orchesis Dance Company', 'Alyssa Morgan', 15, 'Female', 14),
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 14),
    ('Orchesis Dance Company', 'Sasha Silverman', 16, 'Female', 14),
    ('Orchesis Dance Company', 'Lindsey Swanson', 18, 'Female', 14);


INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 8),
    ('Orchesis Dance Company', 'Nora Eisenstein', 17, 'Female', 8),
    ('Orchesis Dance Company', 'Sadie Van Horn', 16, 'Female', 8),
    ('Orchesis Dance Company', 'Emma Kelly', 16, 'Female', 8),
    ('Orchesis Dance Company', 'Anna Libbon', 15, 'Female', 8),
    ('Orchesis Dance Company', 'Olivia Massari', 18, 'Female', 8),
    ('Orchesis Dance Company', 'Grace Weirich', 17, 'Female', 8);

-- Inserting dancers for order_num = 12
INSERT INTO Dancer (studio_name, name, age, gender, order_num) 
VALUES
    ('Orchesis Dance Company', 'Jessie Arnold', 19, 'Female', 12),
    ('Orchesis Dance Company', 'Emily Bowser', 15, 'Female', 12),
    ('Orchesis Dance Company', 'Chesney Dowds', 18, 'Female', 12),
    ('Orchesis Dance Company', 'Aleena Gil', 18, 'Female', 12),
    ('Orchesis Dance Company', 'Alex Jaworski', 15, 'Female', 12),
    ('Orchesis Dance Company', 'Emma McCurdy', 19, 'Female', 12),
    ('Orchesis Dance Company', 'Carley Mykut', 17, 'Female', 12),
    ('Orchesis Dance Company', 'Eva Schulz', 18, 'Female', 12),
    ('Orchesis Dance Company', 'Maddie Shine', 15, 'Female', 12);

    INSERT INTO Schedule (order_num, date, call_time, song) VALUES (5, '2021-08-17', '09:15:00', 'GAGA');
    INSERT INTO Schedule (order_num, date, call_time, song) VALUES (6, '2021-08-17', '09:20:00', 'Rivers and Roads');
    INSERT INTO Schedule (order_num, date, call_time, song) VALUES (24, '2021-08-17', '09:15:00', 'GAGA');
    INSERT INTO Schedule (order_num, date, call_time, song) VALUES (25, '2021-08-17', '09:25:00', 'Rivers and Roads');
    INSERT INTO Schedule (order_num, date, call_time, song) VALUES (26, '2021-08-17', '09:35:00', 'Wolves');
    INSERT INTO Schedule (order_num, date) VALUES (27, '2021-08-1');

    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (5, 'Orchesis Dance Company', 'Large Group', 'Senior', 'Jazz', 'GAGA', NULL);
    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (6, 'Orchesis Dance Company', 'Small Group', 'Teen', 'Contemporary', 'Rivers and Roads', NULL);
    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (24, 'Orchesis Dance Company', 'Large Group', 'Senior', 'Jazz', 'GAGA', NULL);
    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (25, 'Orchesis Dance Company', 'Small Group', 'Teen', 'Contemporary', 'Rivers and Roads', NULL);
    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (26, 'Orchesis Dance Company', 'Small Group', 'Teen', 'Contemporary', 'Wolves', NULL);
    INSERT INTO Piece (order_num, studio_name, size_category, age_group, style, song, award_name) VALUES (27, 'Orchesis Dance Company', 'Small Group', 'Teen', 'Contemporary', 'Heroes', NULL);
    -- Add more pieces as needed

    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (5, 105, 88.0);
    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (6, 106, 87.5);
    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (24, 201, 88.0);
    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (25, 202, 86.5);
    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (26, 203, 87.0);
    INSERT INTO Judges_Score (order_num, judge_id, score) VALUES (27, 204, 85.5);
    -- Add more judge scores as needed

    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('High Silver', 5, 264.0);
    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Gold', 6, 262.5);
    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Gold', 24, 264.0);
    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Silver', 25, 259.5);
    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('High Silver', 26, 261.0);
    INSERT INTO Adjudication (award_name, order_num, total_score) VALUES ('Bronze', 27, 256.5);
    -- Add more adjudications as needed

    INSERT INTO Payment (payment_id, registration_status, studio_name, amount_due, paid, payment_status) VALUES (5, FALSE, 'Orchesis Dance Company', 350.00, FALSE, 'Pending');
    INSERT INTO Payment (registration_status, studio_name, amount_due, paid, payment_status) VALUES (FALSE, 'Orchesis Dance Company', 500.00, FALSE, 'Pending');
    -- Add more payment details as needed
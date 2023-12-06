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

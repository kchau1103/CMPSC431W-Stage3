DROP TABLE IF EXISTS Payment;
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_status VARCHAR(50),
    studio_name VARCHAR(100),
    amount_due DECIMAL(10, 2),
    paid BOOLEAN,
    payment_status VARCHAR(50),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);

DROP TABLE IF EXISTS Set_List;
CREATE TABLE Set_List (
    entry_num INT AUTO_INCREMENT PRIMARY KEY,
    studio_name VARCHAR(100),
    num_dancers INT,
    style VARCHAR(50),
    registration_status VARCHAR(50),
    song_duration TIME,
    avg_age INT,
    song VARCHAR(100),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);

DROP TABLE IF EXISTS Studio;
CREATE TABLE Studio (
    studio_name VARCHAR(100) PRIMARY KEY,
    city VARCHAR(100),
    state VARCHAR(100)
);

DROP TABLE IF EXISTS Schedule;
CREATE TABLE Schedule (
    order_num INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    call_time TIME,
    song INT,
    FOREIGN KEY (song) REFERENCES Set_List(entry_num)
);

DROP TABLE IF EXISTS Dancer;
CREATE TABLE Dancer (
    studio_name VARCHAR(100),
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    order_num INT,
    PRIMARY KEY (studio_name, name), -- Assuming a dancer's name is unique within a studio
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (order_num) REFERENCES Schedule(order_num)
);

DROP TABLE IF EXISTS Piece;
CREATE TABLE Piece (
    order_num INT,
    studio_name VARCHAR(100),
    size_category VARCHAR(50),
    age_group VARCHAR(50),
    style VARCHAR(50),
    song INT,
    award_name INT,
    PRIMARY KEY (order_num, studio_name), -- Composite primary key
    FOREIGN KEY (order_num) REFERENCES Schedule(order_num),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (song) REFERENCES Set_List(entry_num),
    FOREIGN KEY (award_name) REFERENCES Adjudication(award_name)
);

DROP TABLE IF EXISTS Judges_Score;
CREATE TABLE Judges_Score (
    order_num INT,
    judge_id INT,
    score DECIMAL(5, 2),
    PRIMARY KEY (order_num, judge_id), -- Composite primary key
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);

DROP TABLE IF EXISTS Adjudication;
CREATE TABLE Adjudication (
    award_name INT AUTO_INCREMENT PRIMARY KEY,
    order_num INT,
    total_score DECIMAL(5, 2),
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);
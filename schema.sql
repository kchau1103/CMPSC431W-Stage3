DROP TABLE IF EXISTS Studio;
-- Studio Table
CREATE TABLE Studio (
    studio_name VARCHAR(255) PRIMARY KEY,
    city VARCHAR(255),
    state VARCHAR(255)
);

DROP TABLE IF EXISTS Set_List;
-- Set_List Table
CREATE TABLE Set_List (
    entry_num INT,
    studio_name VARCHAR(255),
    num_dancers INT,
    style VARCHAR(255),
    registration_status VARCHAR(255),
    song_duration TIME,
    avg_age INT,
    song VARCHAR(255),
    PRIMARY KEY (entry_num, song),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);

DROP TABLE IF EXISTS Schedule;
-- Schedule Table
CREATE TABLE Schedule (
    order_num INT PRIMARY KEY,
    date DATE,
    call_time TIME,
    song VARCHAR(255),
    FOREIGN KEY (song) REFERENCES Set_List(song)
);

DROP TABLE IF EXISTS Dancer;
-- Dancer Table
CREATE TABLE Dancer (
    studio_name VARCHAR(255),
    name VARCHAR(255),
    age INT,
    gender VARCHAR(255),
    order_num INT,
    PRIMARY KEY (studio_name, name, order_num),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (order_num) REFERENCES Schedule(order_num)
);

DROP TABLE IF EXISTS Piece;
-- Piece Table
CREATE TABLE Piece (
    order_num INT PRIMARY KEY,
    studio_name VARCHAR(255),
    size_category VARCHAR(255),
    age_group VARCHAR(255),
    style VARCHAR(255),
    song VARCHAR(255),
    award_name VARCHAR(255),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (song) REFERENCES Set_List(song),
    FOREIGN KEY (award_name) REFERENCES Adjudication(award_name)
);

DROP TABLE IF EXISTS Judges_Score;
-- Judges_Score Table
CREATE TABLE Judges_Score (
    order_num INT,
    judge_id INT,
    score DECIMAL(5, 2),
    PRIMARY KEY (order_num, judge_id),
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);

DROP TABLE IF EXISTS Adjudication;
-- Adjudication Table
CREATE TABLE Adjudication (
    award_name VARCHAR(255),
    order_num INT,
    total_score DECIMAL(5, 2),
    PRIMARY KEY (award_name, order_num),
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);

DROP TABLE IF EXISTS Payment;
-- Payment Table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_status BOOLEAN,
    studio_name VARCHAR(255),
    amount_due DECIMAL(10, 2),
    paid BOOLEAN,
    payment_status VARCHAR(255),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);

DROP TABLE IF EXISTS Studio;
-- Studio Table
CREATE TABLE Studio (
    studio_name TEXT PRIMARY KEY,
    city TEXT,
    state TEXT
);

DROP TABLE IF EXISTS Set_List;
-- Set_List Table
CREATE TABLE Set_List (
    entry_num INTEGER PRIMARY KEY,
    studio_name TEXT,
    num_dancers INT,
    style TEXT,
    registration_status TEXT,
    song_duration TIME,
    avg_age INT,
    song TEXT,
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);

DROP TABLE IF EXISTS Schedule;
-- Schedule Table
CREATE TABLE Schedule (
    order_num INTEGER PRIMARY KEY,
    date DATE,
    call_time TIME,
    song TEXT,
    FOREIGN KEY (song) REFERENCES Set_List(entry_num)
);

DROP TABLE IF EXISTS Dancer;
-- Dancer Table
CREATE TABLE Dancer (
    studio_name TEXT,
    name TEXT,
    age INT,
    gender TEXT,
    order_num INTEGER,
    PRIMARY KEY (studio_name, name),
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (order_num) REFERENCES Schedule(order_num)
);

DROP TABLE IF EXISTS Piece;
-- Piece Table
CREATE TABLE Piece (
    order_num INTEGER PRIMARY KEY,
    studio_name TEXT,
    size_category TEXT,
    age_group TEXT,
    style TEXT,
    song TEXT,
    award_name INTEGER,
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name),
    FOREIGN KEY (song) REFERENCES Set_List(entry_num),
    FOREIGN KEY (award_name) REFERENCES Adjudication(award_name)
);

DROP TABLE IF EXISTS Judges_Score;
-- Judges_Score Table
CREATE TABLE Judges_Score (
    order_num INTEGER,
    judge_id INTEGER,
    score DECIMAL(5, 2),
    PRIMARY KEY (order_num, judge_id),
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);

DROP TABLE IF EXISTS Adjudication;
-- Adjudication Table
CREATE TABLE Adjudication (
    award_name TEXT PRIMARY KEY,
    order_num INTEGER,
    total_score DECIMAL(5, 2),
    FOREIGN KEY (order_num) REFERENCES Piece(order_num)
);

DROP TABLE IF EXISTS Payment;
-- Payment Table
CREATE TABLE Payment (
    payment_id INTEGER PRIMARY KEY,
    registration_status TEXT,
    studio_name TEXT,
    amount_due DECIMAL(10, 2),
    paid BOOLEAN,
    payment_status TEXT,
    FOREIGN KEY (studio_name) REFERENCES Studio(studio_name)
);
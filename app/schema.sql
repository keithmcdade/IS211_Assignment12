CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY,
    subject TEXT,
    --date DATE,
    date TEXT,
    questions INTEGER
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY,
    score INT,
    student_id INT,
    quiz_id INT
);

INSERT INTO users (username, password) VALUES ("admin", "password");
INSERT INTO students (first_name, last_name) VALUES ("John", "Smith");
INSERT INTO quizzes (subject, date, questions) VALUES ("Python Basics", "2015-02-15", 5);--2015-02-15, 5);
INSERT INTO results (score) VALUES (85, 1, 1);

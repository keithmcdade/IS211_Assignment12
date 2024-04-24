CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY NOT NULL,
    subject TEXT NOT NULL,
    --date DATE,
    date TEXT NOT NULL,
    questions INTEGER NOT NULL
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY NOT NULL,
    score INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
);

INSERT INTO users (username, password) VALUES ("admin", "password");
INSERT INTO students (first_name, last_name) VALUES ("John", "Smith");
INSERT INTO quizzes (subject, date, questions) VALUES ("Python Basics", "2015-02-15", 5);--2015-02-15, 5);
INSERT INTO results (score, student_id, quiz_id) VALUES (85, 1, 1);

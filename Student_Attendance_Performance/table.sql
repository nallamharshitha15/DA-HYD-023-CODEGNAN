CREATE DATABASE student_management;

USE student_management;

SHOW DATABASES;
USE student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    batch VARCHAR(50) DEFAULT 'Data Analyst'
);
SHOW TABLES;

DESC students;
INSERT INTO students
(student_id, student_name, batch)
VALUES
(101, 'Harshitha', 'Data Analyst'),
(102, 'Priya', 'Data Analyst'),
(103, 'Rahul', 'Data Analyst'),
(104, 'Sneha', 'Data Analyst'),
(105, 'Kiran', 'Data Analyst');

SELECT * FROM students;

CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT UNIQUE,
    total_classes INT DEFAULT 0,
    attended_classes INT DEFAULT 0,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    CHECK (total_classes >= 0),
    CHECK (attended_classes >= 0),
    CHECK (attended_classes <= total_classes)
);
INSERT INTO attendance
(student_id, total_classes, attended_classes)
VALUES
(101, 100, 90),
(102, 100, 60),
(103, 100, 85),
(104, 100, 70),
(105, 100, 95);
SELECT * FROM attendance;
SELECT
    student_id,
    total_classes,
    attended_classes,
    total_classes - attended_classes AS absent_classes,
    ROUND(
        attended_classes * 100.0 / total_classes, 2
    ) AS attendance_percentage
FROM attendance;

SELECT
    student_id,
    attended_classes,
    total_classes,
    ROUND(
        attended_classes * 100.0 / total_classes, 2
    ) AS attendance_percentage
FROM attendance
WHERE attended_classes * 100.0 / total_classes < 75;

CREATE TABLE marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    marks INT,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    UNIQUE (student_id, subject),
    CHECK (marks BETWEEN 0 AND 100)
);

INSERT INTO marks
(student_id, subject, marks)
VALUES
(101, 'Python', 90),
(101, 'MySQL', 89),
(101, 'Power BI', 90),

(102, 'Python', 45),
(102, 'MySQL', 50),
(102, 'Power BI', 40),

(103, 'Python', 80),
(103, 'MySQL', 85),
(103, 'Power BI', 90),

(104, 'Python', 60),
(104, 'MySQL', 65),
(104, 'Power BI', 70),

(105, 'Python', 95),
(105, 'MySQL', 92),
(105, 'Power BI', 96);

SELECT * FROM marks;
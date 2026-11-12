USE student_management;

#1. Display all student records.
SELECT * FROM students;

#2. Find the student whose ID is 103.
SELECT * FROM students WHERE student_id = 103;

#3. Display students in alphabetical order.
SELECT * FROM students ORDER BY student_name ASC;

#4.Display the first three students.
SELECT * FROM students LIMIT 3;

#5.Find students who scored more than 80 marks.
SELECT * FROM marks WHERE marks > 80;

#6.Find students who scored between 60 and 90.
SELECT * FROM marks WHERE marks BETWEEN 60 AND 90;

#7.Display Python and MySQL marks only.
SELECT * FROM marks WHERE subject IN ('Python', 'MySQL');

#8.Find students whose names start with H.
SELECT * FROM students WHERE student_name LIKE 'H%';

#9.Find the total number of students.
SELECT COUNT(*) AS total_students FROM students;

#10.Find the highest marks.
SELECT MAX(marks) AS highest_marks FROM marks;

#11.Calculate the average marks.
SELECT ROUND(AVG(marks), 2) AS average_marks FROM marks;

#12.Find the average marks in each subject.
SELECT subject,ROUND(AVG(marks), 2) AS average_marks FROM marks GROUP BY subject;

#13.Find the number of students in each subject.
SELECT subject, COUNT(DISTINCT student_id) AS total_students FROM marks GROUP BY subject;

#14.Display students whose total marks are greater than 200.
SELECT student_id,SUM(marks) AS total_marks FROM marks GROUP BY student_id
HAVING SUM(marks) > 200;

#15.Display student names with their attendance details.
SELECT s.student_name,
       a.total_classes,
       a.attended_classes
FROM students s
INNER JOIN attendance a
ON s.student_id = a.student_id;

#16.Display all students, including those without attendance records.
SELECT s.student_name,
       a.attended_classes
FROM students s
LEFT JOIN attendance a
ON s.student_id = a.student_id;
#17.Display student names, attendance percentage and marks.
SELECT s.student_name,
       ROUND(a.attended_classes * 100.0 /
       NULLIF(a.total_classes, 0), 2) AS attendance_percentage,
       m.subject,
       m.marks
FROM students s
INNER JOIN attendance a
ON s.student_id = a.student_id
INNER JOIN marks m
ON s.student_id = m.student_id;
#18.Find students who scored above the overall average marks.
SELECT *
FROM marks
WHERE marks > (
    SELECT AVG(marks)
    FROM marks
);
#19.Find students who scored the highest marks.
SELECT *
FROM marks
WHERE marks = (
    SELECT MAX(marks)
    FROM marks
);
#20.Update a student's name.
UPDATE students
SET student_name = 'Sree Harshitha '
WHERE student_id = 101;

#21.Delete a particular student.
DELETE FROM students
WHERE student_name = 'kiran';

#22.Create a view for student average marks.
CREATE VIEW student_average AS
SELECT student_id,
       ROUND(AVG(marks), 2) AS average_marks
FROM marks
GROUP BY student_id;
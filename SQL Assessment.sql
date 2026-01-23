-- creating students table
CREATE TABLE students (
  student_id INT,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT
);
-- insert student value in table
INSERT INTO students VALUES
(1, 'Amit', 'CSE', 3, 85),
(2, 'Priya', 'IT', 2, 78),
(3, 'Rahul', 'CSE', 4, 92),
(4, 'Neha', 'ECE', 3, 70);

-- Display all student records
select * from students

-- Display only name and department
select name,department from students

-- Find student with marks greater than 75
SELECT * FROM students WHERE marks>75;

-- DIsplay students from CSE Department
SELECT * FROM students
WHERE department = 'CSE';

-- sort student by marks(descending order)
SELECT* FROM students 
ORDER BY marks DESC

-- SELECT TOP 3 STUDENTS
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3;

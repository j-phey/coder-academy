DROP TABLE students cascade;
DROP TABLE teachers cascade;
DROP TABLE subjects cascade;
DROP TABLE enrollments cascade;

CREATE TABLE STUDENTS (
    student_id serial PRIMARY KEY,
    f_name text NOT NULL,
    l_name text NOT NULL,
    dob date
);

CREATE TABLE TEACHERS (
    teacher_id serial PRIMARY KEY,
    name text
);

CREATE TABLE SUBJECTS (
    subject_id serial PRIMARY KEY,
    subject_name text,
    teacher_id integer,
    FOREIGN KEY (teacher_id) REFERENCES TEACHERS(teacher_id) ON DELETE SET NULL
    -- When a teacher is deleted from the database the subject they teach 
    -- remains there with a null value for the teacher
);

CREATE TABLE ENROLLMENTS (
    enrollment_id serial PRIMARY KEY, 
    student_id integer,
    subject_id integer,
    enrollment_date date DEFAULT CURRENT_DATE,

    FOREIGN KEY (student_id) REFERENCES STUDENTS(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES SUBJECTS(subject_id) ON DELETE CASCADE
    -- When a student or subject is deleted all related enrollments are deleted as well
);

-- Altering tables
ALTER TABLE STUDENTS
ADD COLUMN email text NOT NULL;

ALTER TABLE TEACHERS 
RENAME COLUMN name TO f_name;

ALTER TABLE TEACHERS
ADD COLUMN l_name text NOT NULL;

ALTER TABLE SUBJECTS
ADD COLUMN area text DEFAULT 'Databases';

-- Inserting rows
INSERT INTO STUDENTS (f_name, l_name, dob, email) values
('Michael', 'Scott', '1/1/1990', 'mscott@email.com'),
('Dwight', 'Schrute', '1/1/1990', 'dwight@email.com'),
('Pam', 'Lark', '1/1/1990', 'pam@email.com'),
('Jim', 'Doo', '1/1/1990', 'jim@email.com'),
('Stanley', 'Fay', '1/1/1990', 'stanley@email.com');

INSERT INTO TEACHERS (f_name, l_name) values
('Robert', 'Dink'),
('Jan', 'Levinson'),
('Charles', 'Barkley');

INSERT INTO SUBJECTS (subject_name, teacher_id, area) values
('HTML/CSS', 2, 'Computer Science'),
('SQL', 2, 'Computer Science'),
('Python', 2, 'Computer Science');

INSERT INTO ENROLLMENTS (student_id, subject_id) values
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 1),
(3, 3),
(4, 2),
(4, 3),
(5, 1),
(5, 2);

-- Updating values
UPDATE STUDENTS 
SET dob = '10/31/2000'
WHERE student_id = 4;

UPDATE subjects
SET subject_name = 'Programming'
WHERE subject_name = 'Python';

DELETE FROM ENROLLMENTS
WHERE enrollment_id = 1 OR enrollment_id = 2;

DELETE FROM STUDENTS 
WHERE student_id = 3;

-- Simple queries

--Show all the teachers.
SELECT * 
FROM teachers;

--Show the subject's different areas.
SELECT DISTINCT area
FROM subjects;

--Show the subject names alphabetically ordered.
SELECT subject_name
FROM subjects
ORDER BY subject_name asc;

--Show the first name, last name and dob of birth of the students starting with the youngest.
SELECT f_name, l_name, dob
FROM students
ORDER BY dob desc;

--Show the enrollments of the students 4 and 5
SELECT *
FROM enrollments
WHERE student_id = 4 OR student_id = 5;

--Show the email of students who were born in the 90s decade
SELECT email
FROM students
WHERE dob BETWEEN '01/01/1990' AND '12/31/1999';

--Show the students whose last name starts with an A.
SELECT *
FROM students
WHERE l_name LIKE 'D%';
CREATE TABLE STUDENTS (
    student_id serial PRIMARY KEY,
    f_name text NOT NULL,
    l_name text NOT NULL,
    dob date
);

CREATE TABLE TEACHERS (
    teacher_id serial PRIMARY KEY,
    teacher_name text
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
CREATE DATABASE School

CREATE TABLE Classes (
	Class_ID INT PRIMARY KEY NOT NULL IDENTITY (1,1),
	Class_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Students (
	Student_ID INT PRIMARY KEY NOT NULL IDENTITY (500,1),
	Student_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Instructors (
	Instructor_ID INT PRIMARY KEY NOT NULL IDENTITY (300,1),
	Instructor_Name VARCHAR(50)
);

ALTER TABLE Classes
	ADD Student_ID varchar(255);

ALTER TABLE Classes
	ADD Instructor_ID varchar(255);

ALTER TABLE Instructors
	ADD Student_ID varchar(255);

ALTER TABLE Instructors
	ADD Class_ID varchar(255);

ALTER TABLE Students
	ADD Class_ID varchar(255);

ALTER TABLE Students
	ADD Instructor_ID varchar(255);

INSERT INTO Classes
	(Class_Name)
	VALUES
	('Software Development Boot Camp'),
	('C# Boot Camp')
;

INSERT INTO Students
	(Student_Name)
	VALUES
	('Jason Scott'),
	('Zack Taylor'),
	('Trini Kwan'),
	('Billy Cranston'),
	('Kimberly Hart'),
	('Tommy Oliver')
;

INSERT INTO Instructors
	(Instructor_Name)
	VALUES
	('Zordon'),
	('Alpha Five')
;

SELECT * FROM Classes
SELECT * FROM Students
SELECT * FROM Instructors

USE School
GO

UPDATE Students
SET Class_ID = 2
WHERE student_name = 'Tommy Oliver' ;
SELECT * FROM Students

UPDATE Classes
SET Student_ID = 500
WHERE Class_Name = 'Software Development Boot Camp' ;
SELECT * FROM Classes

UPDATE Instructors
SET Class_ID = 2
WHERE Instructor_Name = 'Alpha Five' ;
SELECT * FROM Instructors

SELECT Instructor_Name
FROM Instructors

SELECT Student_Name
FROM Students
ORDER BY Student_Name ASC

USE School
GO

SELECT Students.Student_Name, Classes.Class_Name, Instructors.Instructor_Name
	FROM ((Students
	INNER JOIN Classes ON Students.Class_ID = Classes.Class_ID)
	INNER JOIN Instructors ON Classes.Instructor_ID = Instructors.Instructor_ID);


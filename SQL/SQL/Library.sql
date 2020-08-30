CREATE DATABASE MC_Library

CREATE TABLE Library_Branch (
	BranchID INT PRIMARY KEY NOT NULL IDENTITY (1,1),
	BranchName VARCHAR(255) NOT NULL,
	BranchAddress VARCHAR(255) NOT NULL
);

CREATE TABLE Book_Copies (
	BookID INT,
	BranchID INT,
	Number_Of_Copies INT
);

CREATE TABLE Books (
	BookID INT PRIMARY KEY NOT NULL IDENTITY (200,1),
	Title VARCHAR(255) NOT NULL,
	PID VARCHAR(255)
);

CREATE TABLE Book_Authors (
	AuthorName VARCHAR(255),
	BookID INT
);

CREATE TABLE Borrowers (
	CardNo INT PRIMARY KEY NOT NULL IDENTITY (7000,1),
	B_Name VARCHAR(255) NOT NULL,
	B_Address VARCHAR(255) NOT NULL,
	B_Phone VARCHAR(255) NOT NULL
);

CREATE TABLE Book_Loans (
	BookID INT,
	BranchID INT,
	CardNo INT,
	DateOut DATE,
	DateDue DATE
);

CREATE TABLE Publishers (
	PID INT PRIMARY KEY NOT NULL IDENTITY (1,1),
	PublisherName VARCHAR(255),
	PAddress VARCHAR(255),
	PPhone VARCHAR(255)
);

INSERT INTO Library_Branch (BranchName, BranchAddress)
	VALUES
	('Sharpstown', '7660 Clarewood Dr, Houston, TX 77036'),
	('Rockwood', '17917 SE Stark St, Portland, OR 97233'),
	('Midland', '805 SE 122nd Ave, Portland, OR 97233'),
	('Holgate', '7905 SE Holgate Blvd, Portland, OR 97206'),
	('Woodstock', '6008 SE 49th Ave, Portland, OR 97206'),
	('Belmont', '1038 SE Cesar Estrada Chavez Blvd, Portland, OR 97214')
;

INSERT INTO Books
	(Title)
	VALUES
	('The Lost Tribe'),
	('Saga'),
	('Dragonlance'),
	('Interview with a Vampire'),
	('Party Summer'),
	('Frankenstein'),
	('Through the Looking Glass'),
	('The Wonderful Wizard of OZ'),
	('The Giver'),
	('The BFG'),
	('The Lord of the Rings'),
	('The Lord of the Flies'),
	('Great Expectations'),
	('The Adventures of Tom Sawyer'),
	('The Wizards First Rule'),
	('The Colour of Magic '),
	('Harry Potter'),
	('The Hitchhikers Guide to the Galaxy'),
	('Dune'),
	('Enders Game')
;

INSERT INTO Borrowers
	(B_Name, B_Address, B_Phone)
	VALUES
	('Alice Liddell', '9317 Fairway Dr. Willingboro, NJ 08046', '202-555-0160'),
	('Tasslehoff Burrfoot', '9689 Lakeview Ave. Adrian, MI 49221', '616-555-0146'),
	('Lestat de Lioncourt', '3001 Beacon Light Rd Ruston, LA, 71270', '318-202-3054'),
	('Dorothy Gale', '736 E 1485th Rd Lawrence, KS, 66046', '785-594-6671'),
	('Arthur Dent', '69 Ledgeview Dr Rochester, NH, 03839', '603-332-0250'),
	('Becky Thatcher', '142 Louise St Nettleton, MS, 38858', '662-963-1455'),
	('Richard Cypher', '100 Wild Bill Blvd Westcliffe, CO, 81252', '719-783-2954'),
	('Aragorn Telcontar', '33000 SE Kelso Rd Boring, OR, 97009', '360-335-9380')
;

INSERT INTO Publishers
	(PublisherName, PAddress, PPhone)
	VALUES
	('TSR inc', '1600 Lind Ave SW, Renton, WA 98057', '425-226-6500'),
	('Tor Books', '120 Broadway New York, NY 10271', '646-307-5151'),
	('Image Comics', '2701 NW Vaughn Street, Portland, OR 97210', '971-865-5794'),
	('Scholastic', '5127 NE 158th Ave, Portland, OR 97230', '503-252-8486'),
	('Penguin Books', '1745 Broadway, New York, NY 10019', '800-793-2665')
;

INSERT INTO Book_Loans
	(DateOut, DateDue)
	VALUES
	('04-16-2020', '09-15-2020')
;

INSERT INTO Book_Loans
	(DateOut, DateDue)
	VALUES
	('02-28-2019', '07-27-2019')
;

INSERT INTO Book_Loans
	(DateOut, DateDue)
	VALUES
	('06-02-2020', '12-01-2020')
;

SELECT * FROM Library_Branch
SELECT * FROM Book_Copies
SELECT * FROM Books
SELECT * FROM Book_Authors
SELECT * FROM Borrowers
SELECT * FROM Book_Loans
SELECT * FROM Library_Branch
SELECT * FROM Publishers


UPDATE Book_Loans
SET BookID = '200'
WHERE DateOut = '2020-04-16';

UPDATE Book_Loans
SET CardNo = '7000'
WHERE DateOut = '2020-04-16';

UPDATE Book_Loans
SET BranchID = '1'
WHERE DateOut = '2020-04-16';

UPDATE Book_Loans
SET BookID = '200'
WHERE DateOut = '2019-02-28';

UPDATE Book_Loans
SET CardNo = '7005'
WHERE DateOut = '2019-02-28';

UPDATE Book_Loans
SET BranchID = '1'
WHERE DateOut = '2019-02-28';

UPDATE Book_Loans
SET BookID = '200'
WHERE DateOut = '2020-06-02';

UPDATE Book_Loans
SET CardNo = '7003'
WHERE DateOut = '2020-06-02';

UPDATE Book_Loans
SET BranchID = '1'
WHERE DateOut = '2020-06-02';

CREATE PROC Copy_Count
AS
SELECT COUNT (BookID)
FROM Book_Loans
WHERE BookID = '200';

EXEC [dbo].[Copy_Count]
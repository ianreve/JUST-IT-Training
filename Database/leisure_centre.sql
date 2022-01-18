use leisure_centre;
drop database leisure_centre;
create database leisure_centre;
show tables;

-- Creating Table Course 
CREATE TABLE `Course` (
`CourseID` INT PRIMARY KEY NOT NULL , 
`Level` INT,
`Session` VARCHAR(50),
`Instructor` VARCHAR(50),
`StartDate` date,
`Lesson_time` time
);

-- Creating Table Members
CREATE TABLE `Members`(
`MemberID`INT PRIMARY KEY AUTO_INCREMENT ,
`FirstName` VARCHAR(20),
`Surname` VARCHAR(10),
`DOB` DATE,
`Address` VARCHAR(100),
`City` VARCHAR(20)

);
-- Creating Table  Lessons
CREATE TABLE `Lessons` (
`LessonID` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
`CourseID` INT,
`MemberID` INT,
FOREIGN KEY(`CourseID`) REFERENCES `Course`(`CourseID`) ON UPDATE CASCADE,
FOREIGN KEY (`MemberID`) REFERENCES `Members`(`MemberID`) ON UPDATE CASCADE
);



--  Data insertion 
INSERT INTO `Lessons` (`LessonID`) VALUES (1000),(2000),(3000),(4000),(5000),(6000),(7000);


INSERT INTO `Members`(`MemberID`,`FirstName`,`Surname`,`DOB`,`Address`,`City` ) VALUES

 (1,'John','Snow','1980-01-01', '1 Stark House','WinterFell'),
 (2,'Brian','Jonas','1985-10-02', '897 Long Airport Avenue','NYC'),
 (3,'Bruce','Jonas','1985-10-02', 'PR 334 Sentrum Bergen','Norway'),
 (4,'Omar','Colmore','1975-05-02', '5 Clarendon Road','London'),
 (5,'King','Jean','1990-10-01', '8489 Strong St','Las Vegas'),
 (6,'Ferguson','Peter','1960-11-25', '636 St Kilda Road Level','Victoria'),
 (7,'Bergulfsen','Jonas ','1995-10-01', ' 5677 Strong St. San Rafael','CA');
 
 
INSERT INTO `Course` (`CourseID`,`Level`,`Session`,`Instructor`,`StartDate`,`Lesson_time` ) VALUES

 (1,'1','Morning','Joe Martin', '2022-01-17','09:00:00'),
(2,'1','Morning','Martin Green', '2022--02-11','10:0:00'),
(3,'2','Morning','Janice Carter', '2022-03-27','11:00:00'),
(4,'1','Morning','Josept White', '2022-04-27','11:00:00'),
(5,'3','Afternoon','ALfie Murdock', '2022-08-10','12:00:00'),
(6,'2','Morning','Janice Carter', '2022-03-27','11:00:00'),
(7,1, 'Morning', 'Night King','2022-01-20','08:00:00');
   
-- Assign Lessons Member ID 
	UPDATE Lessons Set MemberID  = 1  Where LessonID = 1000;
	UPDATE Lessons Set MemberID  = 2  Where LessonID = 2000;
	UPDATE Lessons Set MemberID  = 3  Where LessonID = 3000;
	UPDATE Lessons Set MemberID  = 4  Where LessonID = 4000;
	UPDATE Lessons Set MemberID  = 5  Where LessonID = 5000;
	UPDATE Lessons Set MemberID  = 6  Where LessonID = 6000;
	UPDATE Lessons Set MemberID  = 7  Where LessonID = 7000;
 
-- Assign Lessons Course ID
	UPDATE Lessons Set CourseID = 1 Where LessonID = 1000;
	UPDATE Lessons Set CourseID = 2 Where LessonID = 2000;
	UPDATE Lessons Set CourseID = 3 Where LessonID = 3000;
	UPDATE Lessons Set CourseID = 4 Where LessonID = 4000;
	UPDATE Lessons Set CourseID = 5 Where LessonID = 5000;
	UPDATE Lessons Set CourseID = 6 Where LessonID = 6000;
	UPDATE Lessons Set CourseID = 7 Where LessonID = 7000;

-- Exercise 
-- A.	Use the SQL AND, OR and NOT Operators in your query (The WHERE clause can be combined with AND, OR, and NOT operators)
-- 1.	Where courseID is equals to a number below 5 and the first name of any of the instructors 
 
 SELECT CourseID, Instructor FROM Course WHERE CourseID < 5;
 
 -- 2.	Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.  
 
 SELECT CourseID, Lesson_time  FROM Course WHERE Lesson_time BETWEEN '08:00:00' AND '11:00:00';
 
 --  B.	Order by the above results by:
 -- 1.	 startDate in “course” table
 
SELECT * FROM Course ORDER BY startDate;

-- 2.	 MemberID in “members” table

SELECT * FROM Members ORDER BY MemberID;

-- C.	UPDATE the following:
-- 1.	 Members table, change the addresses of any three members.

UPDATE Members SET Address = ' ' WHERE MemberID = 1;
UPDATE Members SET Address = ' ' WHERE MemberID = 2;
UPDATE Members SET Address = ' ' WHERE MemberID = 5;

-- 2.	Course table, change the startDate and lesson time for three of the sessions.

UPDATE Course SET startDate = '2022-10-02', Lesson_time = '01:00:00' WHERE CourseID = 1;
UPDATE Course SET startDate = '2022-12-02', Lesson_time = '00:30:00' WHERE CourseID = 3;
UPDATE Course SET startDate = '2022-05-02', Lesson_time = '02:00:00' WHERE CourseID = 7;

-- D.	Use the SQL MIN () and MAX () Functions to return the smallest and largest value 
-- 1.	Of the LessonID column in the “lesson” table

SELECT MIN(LessonID) FROM Lessons;

-- 2.	Of the membersID column in the “members” table 

SELECT MAX(MemberID) FROM Members;

-- E.	Use the SQL COUNT (), AVG () and SUM () Functions for these:
-- 1.	Count the total number of members in the “members” table
 
 SELECT COUNT(MemberID) FROM Members;

-- 2.	Count the total number of sessions in the” members” table ***** maybe actual meant for Course;

SELECT COUNT(Session) FROM Course;

-- 3.	Find the average session time for all “sessions” in course table 

SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(`Lesson_time`))) FROM Course;


-- F.	WILDCARD queries (like operator)
-- a)	Find all the people from the “members” table whose last name starts with A.
-- replaced the seach values to fit the data in the tables to j and s
	
    SELECT * from Members Where Surname like "A%";
    
-- b)	Find all the people from the “members” table whose last name ends with A.

SELECT * from Members Where Surname like "%A";

-- c)	Find all the people from the “members” table that have "ab" in any position in the last name.

  SELECT * from Members Where Surname like "%ab%";

-- d)	Find all the people from the “members” table that that have "b" in the second position in their first name.

SELECT * from Members Where Surname like "_b%";

-- e)	Find all the people from the “members” table whose last name starts with "a" and are at least 3 characters in length:

SELECT * from Members Where Surname like "A__%";

-- f)	Find all the people from the “members” table whose last name starts with "a" and ends with "y"

 SELECT * from Members Where Members.Surname LIKE "a%" AND Members.Surname like "%y%";

-- g)	Find all the people from the “members” table whose last name does not starts with "a" and ends with "y"

 SELECT * from Members Where Members.Surname  NOT LIKE "a%" AND Members.Surname like "%e%";

-- G.	What do you understand by LEFT and RIGHT join? Explain with an example.

SELECT  Lessons.MemberID, Members.FirstName, Members.Surname,  Lessons.LessonID
FROM Lessons
INNER JOIN Members
 ON Lessons.MemberID = Members.MemberID ;

 --  Left  Join
SELECT   Members.FirstName, Members.Surname,  Lessons.LessonID, Lessons.MemberID 
FROM Members
Left JOIN Lessons
 ON Members.MemberID = Lessons.LessonID;
 
 --  Right Join
 SELECT  Members.FirstName, Members.Surname,  Lessons.LessonID, Lessons.MemberID
FROM Lessons
RIGHT JOIN Members
 ON Lessons.MemberID = Members.MemberID 
 
 
 -- ------------------------------------------------------------------------------


db.Members.insertMany([
{'MemberID': 1,
'Firstname': 'John',
'Surname':'Snow',
'DOB':new Date ('1980-01-01'),
'Address':'1 Stark House',
'City':'WinterFell'
},
{'MemberID': 2,
'Firstname': 'Brian',
'Surname':'Jonas',
'DOB':new Date ('1985-10-02'),
'Address':'897 Long Airport Avenue',
'City':'NYC'
},
{'MemberID': 3,
'Firstname': 'Bruce',
'Surname':'Jonas',
'DOB':new Date ('1985-10-02'),
'Address':'PR 334 Sentrum Bergen',
'City':'Norway'
},
{'MemberID': 4,
'Firstname': 'Omar',
'Surname':'Colmore',
'DOB':new Date ('1975-05-02'),
'Address':'5 Clarendon Road',
'City':'London'
},
{'MemberID': 5,
'Firstname': 'King',
'Surname':'Jean',
'DOB':new Date ('1990-10-01'),
'Address':'8489 Strong St',
'City':'Las Vegas'
},
{'MemberID': 6,
'Firstname': 'Ferguson',
'Surname':'Peter',
'DOB':new Date ('1960-11-25'),
'Address':'636 St Kilda Road Level',
'City':'Victoria'
},
{'MemberID': 7,
'Firstname': 'Bergulfsen',
'Surname':'Jonas',
'DOB':new Date ('1995-10-01'),
'Address':'5677 Strong St. San Rafael',
'City':'CA'
}])

db.Course.insertMany([
{'CourseID': 1,
'Level': 1,
'Session':'Swimming',
'Instructor':'Joe Martin',
'StartDate': new Date ('2022-01-17'),
'Lesson_time': time: new ISODate(' 09:00:00')
}

])

db.Course.insertMany([{'CourseID': 1,
'Level': 1,
'Session':'Morning',
'Instructor':'Joe Martin',
'StartDate': new Date ('2022-01-17'),
'Lesson_time':' 09:00:00'
},
{'CourseID':2,
'Level': 1,
'Session':'Morning',
'Instructor':'Martin Green',
'StartDate': new Date ('2022-02-11'),
'Lesson_time':' 10:00:00'
},
{'CourseID': 3,
'Level': 2,
'Session':'Morning',
'Instructor':'Janice Carter',
'StartDate': new Date ('2022-03-27'),
'Lesson_time':' 11:00:00'
},
{'CourseID': 4,
'Level': 1,
'Session':'Morning',
'Instructor':'Josept White',
'StartDate': new Date ('22022-04-27'),
'Lesson_time':' 11:00:00'
},
{'CourseID': 5,
'Level': 3,
'Session':'Afternoon',
'Instructor':'ALfie Murdock',
'StartDate': new Date ('2022-08-10'),
'Lesson_time':' 12:00:00'
},
{'CourseID': 6,
'Level': 2,
'Session':'Morning',
'Instructor':'Janice Carter',
'StartDate': new Date ('2022-03-27'),
'Lesson_time':' 11:00:00'
},
{'CourseID': 7,
'Level': 1,
'Session':'Morning',
'Instructor':'Night King',
'StartDate': new Date ('2022-01-20'),
'Lesson_time':' 08:00:00'
}
])


db.Lessons.insertMany([
{
'LessonID': 1000,
 'CourseID':1,
 'MemberID':1},
 {
 'LessonID': 2000,
 'CourseID':2,
 'MemberID':2},
 {
 'LessonID': 3000,
 'CourseID':3,
 'MemberID':3},
 {
 'LessonID': 4000,
 'CourseID':4,
 'MemberID':4},
 {
 'LessonID': 5000,
 'CourseID':5,
 'MemberID':5},
 {
 'LessonID': 6000,
 'CourseID':6,
 'MemberID':6},
 {
 'LessonID': 7000,
 'CourseID':7,
 'MemberID':7}
 ])



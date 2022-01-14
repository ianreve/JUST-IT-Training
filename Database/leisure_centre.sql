USE `leisure_centre`;


CREATE TABLE `Course` (
`CourseID` INT PRIMARY KEY NOT NULL , 
`Level` INT,
`Session` VARCHAR(50),
`Instructor` VARCHAR(50),
`StartDate` date,
`Lesson_time` time
);

CREATE TABLE `Lessons` (
`LessonID` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
`CourseID` INT,
`MemberID` INT,
FOREIGN KEY(`CourseID`) REFERENCES `Course`(`CourseID`) ON UPDATE CASCADE,
FOREIGN KEY (`MemberID`) REFERENCES `Members`(`MemberID`) ON UPDATE CASCADE
);



CREATE TABLE `Members`(
`MemberID`INT PRIMARY KEY AUTO_INCREMENT ,
`FirstName` VARCHAR(20),
`Surname` VARCHAR(10),
`DOB` DATE,
`Address` VARCHAR(100),
`City` VARCHAR(20)

);
INSERT INTO `Lessons` (`LessonID`) VALUES (1000),(2000),(3000),(4000),(5000),(6000),(7000);


INSERT INTO `Members`(`MemberID`,`FirstName`,`Surname`,`DOB`,`Address`,`City` ) VALUES

 (56,'Omar','Colmore ','1975-05-02', '5 Clarendon Road','London');
 
 
INSERT INTO `Course` (`CourseID`,`Level`,`Session`,`Instructor`,`StartDate`,`Lesson_time` ) VALUES

 (1,'1','Swimming ','Joe Martin', '2022-01-17','09:00:00'),
(2,'1','Tennis ','Martin Green', '2022--02-11','10:0:00'),
(3,'2','Yoga ','Janice Carter', '2022-03-27','11:00:00'),
(4,'1','Cadio ','Josept White', '2022-04-27','11:00:00'),
(5,'3','Tennis ','ALfie Murdock', '2022-08-10','12:00:00'),
(6,'2','Badmiton','Janice Carter', '2022-03-27','11:00:00'),
(7,1, 'aerobics', 'Night King','2022-01-20','08:00:00');
   
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



USE `leisure_centre`;


CREATE TABLE `Course` (
`CourseID` INT PRIMARY KEY NOT NULL , 
`Level` INT,
`Session` VARCHAR(50),
`StartDate` date,
`Lesson_time` time
);

CREATE TABLE `Lessons` (
`LessonID` INT PRIMARY KEY NOT NULL,
`CourseID` INT,
`MemberID` INT,
FOREIGN KEY(`CourseID`) REFERENCES `Course`(`CourseID`),
FOREIGN KEY (`MemberID`) REFERENCES `Members`(`MemberID`)
);

CREATE TABLE `Members`(
`MemberID`INT PRIMARY KEY AUTO_INCREMENT ,
`FirstName` VARCHAR(20),
`Surname` VARCHAR(10),
`DOB` DATE,
`Address` VARCHAR(100),
`City` VARCHAR(20)

);
SHOW TABLES;
DESC Course;

DROP TABLE `Course`;
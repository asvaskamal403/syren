use gvp;
DROP TABLE sections;
CREATE TABLE sections(
     sectionID varchar(255) NOT NULL PRIMARY KEY,
     courseID INT NOT NULL,
     tutorID varchar(255) NOT NULL);
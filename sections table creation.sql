use gvp;
DROP TABLE sections;
CREATE TABLE sections(
     roll INT NOT NULL, 
     sectionID INT NOT NULL PRIMARY KEY,
     courseID INT NOT NULL,
     tutorID INT NOT NULL);
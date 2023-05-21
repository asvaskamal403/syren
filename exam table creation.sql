use gvp;
DROP TABLE exams;
CREATE TABLE gvp.exams(
	roll int NOT NULL UNIQUE AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    courseID int NOT NULL,
    marks float,
    grade varchar(255) NOT NULL,
    PRIMARY KEY (roll)
    );
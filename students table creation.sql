DROP TABLE students;
CREATE TABLE students (
	roll int PRIMARY KEY not null unique,
	name varchar(255) not null,
	courseID INT NOT NULL);

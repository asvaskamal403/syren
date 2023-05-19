DROP TABLE studentdetails;
CREATE TABLE studentdetails(
    roll int PRIMARY KEY UNIQUE NOT NULL,
    name varchar(255) NOT NULL,
    branch varchar(255) NOT NULL,
    city varchar(255) NOT NULL,
    country varchar(255) NOT NULL);
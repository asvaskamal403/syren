DROP TABLE  courses ;
CREATE TABLE courses (
     courseID varchar(255) NOT NULL UNIQUE,
     offeredby varchar(255) NOT NULL,
     coursename varchar(255),
     durationinyrs int NOT NULL,
     cost int NOT NULL
);
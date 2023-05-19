DROP TABLE  courses ;
CREATE TABLE courses (
     courseID int NOT NULL UNIQUE,
     offeredby varchar(255) NOT NULL,
     coursedesp varchar(255),
     durationinyrs int NOT NULL,
     cost int NOT NULL
);
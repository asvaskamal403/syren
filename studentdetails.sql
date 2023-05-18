CREATE DATABASE gvp;
CREATE TABLE studentdetails(
    roll int,
    name varchar(255),
    gender varchar(255),
    branch varchar(255),
    city varchar(255),
    country varchar(255));
INSERT INTO gvp.studentdetails
values(1,"varun","male","E.C.E","kadapa","india"),
      (2,"rakesh","male","E.C.E","visakhapatnam","india"),
      (3,"kamal","male","E.C.E","visakhapatnam","india"),
      (4,"aditya","male","E.C.E","amalapuram","india"),
      (5,"meghana","female","E.C.E","rajolu","india"),
      (6,"yeswanth","male","E.C.E","rajahmundry","india");
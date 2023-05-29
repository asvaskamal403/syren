use gvp;
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

#1. print coursename which has max number of stude
with numofcourses as (select c.coursename,count(s.roll) as count from studentscourses s inner join courses c on s.courseID = c.courseID
group by s.courseID) select coursename,count from numofcourses where count=(select max(count) from numofcourses);

select c.coursename from courses c
inner join studentscourses s on s.courseID=c.courseID
group by c.coursename
order by count(s.roll) desc
limit 2;



#2. print student name who took more number of courses
with studentdata as (select count(courseID) as count,roll from students group by roll) select stu.name, 
s.count from studentdetails stu inner join studentdata s on stu.roll=s.roll
where s.count=(select max(count) from studentdata);

#3. print student name who pays highest fee
with studentfee as (select sum(c.cost) as total,
s.roll from courses c inner join students s on c.courseID=s.CourseID group by s.roll) select s.name,
stu.total from studentfee stu inner join studentdetails s on stu.roll = s.roll where total=(select max(total) from studentfee);


#4 print tutor name who taught more number of courses
with tutordata as (select count(courseID) as count,tutorID from tutors group by tutorID) select t.tutorsname, 
tu.count from tutordetails t inner join tutordata tu on t.tutorsID=tu.tutorID where tu.count=(select max(count) from tutordata); 


#5. window functions
#lead() function will allows to access data of the following row, or the row after the subsequent row, and continue on.

select courseID,coursename, month,salevalue, lead(salevalue,1) over (partition by courseID order by month) 
nextmonthsalevalue from coursesales;

#LAG() function which is very useful in case the current row values need to be 
compared with the data/value of the previous record or any record before the previous record.

select courseID,coursename, month,salevalue, lag(salevalue,1) over (partition by courseID order by month) 
prevmonthsalevalue from coursesales;

#In the SQL RANK functions, we use the OVER() clause to define a set of rows in the result set. 
#We can also use SQL PARTITION BY clause to define a subset of data in a partition.
#You can also use Order by clause to sort the results in a descending or ascending order.

select * from ranks;
select coursename,offeredby,rankingscore,rank() over (order by rankingscore) ranking_score from ranks;

#We use DENSE_RANK() function to specify a unique rank number within the partition as per the specified column value.
#It is similar to the Rank function with a small difference.

select coursename,offeredby,rankingscore,dense_rank() over (order by rankingscore) ranking_score from ranks;

#We use ROW_Number() SQL RANK function to get a unique sequential number for each row in the specified data. 
#It gives the rank one for the first row and then increments the value by one for each row.
#We get different ranks for the row having similar values as well.

select coursename,offeredby,rankingscore,row_number() over (order by rankingscore) s_no from ranks;

#rank() with partition by
select * from ranks;
select coursename,offeredby,rankingscore,rank() over (partition by offeredby order by rankingscore) ranking_score from ranks;

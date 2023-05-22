use gvp;
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

#1. print coursename which has max number of students
with kamal as (select c.coursename,count(s.roll) as count from students s inner join courses c on s.courseID = c.courseID
group by s.courseID) select coursename,count from kamal where count=(select max(count) from kamal);


#2. print student name who took more number of courses
with kamal as (select count(courseID) as count,roll from students group by roll) select stu.name, 
k.count from studentdetails stu inner join kamal k on stu.roll=k.roll
where k.count=(select max(count) from kamal);

#3. print student name who pays highest fee
with kamal as (select sum(c.cost) as total,
s.roll from courses c inner join students s on c.courseID=s.CourseID group by s.roll) select s.name,
k.total from kamal k inner join studentdetails s on k.roll = s.roll where total=(select max(total) from kamal);


#4 print tutor name who taught more number of courses
with kamal as (select count(courseID) as count,tutorID from tutors group by tutorID) select t.tutorsname, 
k.count from tutordetails t inner join kamal k on t.tutorsID=k.tutorID where k.count=(select max(count) from kamal); 


#5. window functions
#lead
select courseID,coursename, month,salevalue, lead(salevalue,1) over (partition by courseID order by month) 
nextmonthsalevalue from coursesales;

#lag
select courseID,coursename, month,salevalue, lag(salevalue,1) over (partition by courseID order by month) 
prevmonthsalevalue from coursesales;

#rank()
select * from ranks;
select coursename,offeredby,rankingscore,rank() over (order by rankingscore) ranking_score from ranks;

#dense_rank()
select coursename,offeredby,rankingscore,dense_rank() over (order by rankingscore) ranking_score from ranks;

#row_number():
select coursename,offeredby,rankingscore,row_number() over (order by rankingscore) s_no from ranks;

#rank() with partition by
select * from ranks;
select coursename,offeredby,rankingscore,rank() over (partition by offeredby order by rankingscore) ranking_score from ranks;
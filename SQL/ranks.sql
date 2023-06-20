use gvp;
drop table ranks;
create table ranks(courseID varchar(255) not null primary key,
			  offeredby varchar(40) not null,
              coursename varchar(40) not null,
              rankingscore int not null);
insert into ranks values('CO999',"BABA","sql",600),
       ('CO777',"KEKA","databricks",500),
       ('CO888',"BABA","azure",400),
       ('CO555',"MICROSOFT","sql",300),
       ('CO666',"JNTU","databricks",600),
       ('CO111',"AU","azure",500),
       ('CO612',"CISCO","c#",400),
       ('CO750',"CISCO","css",300);
select * from ranks;
select coursename,offeredby,rankingscore,rank() over (order by rankingscore) ranking_score from ranks;
#2
select name,category,rankingscore,dense_rank() over (order by rankingscore) ranking_score from product;
#3
select name,category,rankingscore,row_number() over (order by rankingscore) s_no from product;
#4
select name,category,rankingscore,rank() over (partition by category order by rankingscore) ranking_score from product;
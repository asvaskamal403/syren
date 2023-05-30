import pymysql
class methods:
    def __init__(self,Host,User,Password,database):
        self.Host=Host
        self.User=User
        self.Password=Password
        self.database=database

    def read(self):
        conn = pymysql.connect(host=self.Host,user=self.User,password=self.Password,db=self.database)
        cur = conn.cursor()
        cur.execute("select * from courses")
        conn.commit()
        output = cur.fetchall()
        for i in output:
           print(i)
        conn.close()

    def insert(self):
        conn = pymysql.connect(host=self.Host,user=self.User,password=self.Password,db=self.database)
        cur = conn.cursor()
        cur.execute("insert into courses values ('CO403','AU','azure',3,100)")
        conn.commit()
        cur.execute("select * from courses")
        output = cur.fetchall()
        for i in output:
           print(i)
        conn.close()

    def update(self):
        conn = pymysql.connect(host=self.Host,user=self.User,password=self.Password,db=self.database)
        cur = conn.cursor()
        cur.execute("update courses set cost = 850000 where courseID = 'CO999'")
        conn.commit()
        cur.execute("select * from courses where courseID = 'CO999'")
        output = cur.fetchall()
        for i in output:
           print(i)
        conn.close()

    def delete(self):
        conn = pymysql.connect(host=self.Host,user=self.User,password=self.Password,db=self.database)
        cur = conn.cursor()
        cur.execute("delete from courses where courseID = 'CO111'")
        conn.commit()
        cur.execute("select * from courses")
        output = cur.fetchall()
        for i in output:
           print(i)
        conn.close()

kamal=methods('localhost','root','Kamal@230167','gvp')
kamal.delete()



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
        cur.execute(f"select 1 where exists (select cost from courses)")
        conn.commit()
        output = cur.fetchall()
        print(type(output))
        for i in output:
           print(i)
        conn.close()
my=methods('localhost','root','Kamal@230167','gvp')
my.read()      
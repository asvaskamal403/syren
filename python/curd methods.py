import pymysql
class datamethods:
    def __init__(self,Host,User,Password,database):
        self.Host=Host
        self.User=User
        self.Password=Password
        self.database=database
        self.conn=pymysql.connect(host=self.Host,user=self.User,password=self.Password,db=self.database)
        self.cur=self.conn.cursor()

    def read(self,tablename,columnname): 
        try:
            if(columnname[0]=='*'):
                self.conn.ping()
                self.cur.execute(f"select * from {tablename}")
                output=self.cur.fetchall()
                for i in output:
                    print(i)
                self.conn.close()
            elif(len(columnname)==1 and columnname[0]!='*'):
                self.conn.ping()
                self.cur.execute(f"select {columnname[0]} from {tablename}")
                output=self.cur.fetchall()
                for i in output:
                    print(i)
                self.conn.close()
            elif(len(columnname)==2):
                self.conn.ping()
                self.cur.execute(f"select {columnname[0]},{columnname[1]} from {tablename}")
                output=self.cur.fetchall()
                for i in output:
                    print(i)
                self.conn.close()  
            elif(len(columnname)==3):
                self.conn.ping()
                self.cur.execute(f"select {columnname[0]},{columnname[1]},{columnname[2]} from {tablename}")
                output=self.cur.fetchall()
                for i in output:
                    print(i)
                self.conn.close()  
        except pymysql.err.ProgrammingError:
            print("table doesn't exist")    
        except pymysql.err.OperationalError:
            print("column not there in table")
        except pymysql.err.InterfaceError:
            print("interface error")    
    def insert(self,tablename,values):
        try:
            self.cur.execute(f"insert into {tablename} values {values}")
            self.conn.commit()
            print("insertion done successfully")
            self.conn.close()
        except pymysql.err.IntegrityError:
            print("sorry! Duplicate entry")
        except pymysql.err.ProgrammingError:
            print("table doesn't exist") 
        except pymysql.err.OperationalError:
            print("column not there in table") 
        except pymysql.err.DataError:
            print("sorry! there is an error in data types")              

    def update(self,tablename,columnname1,value1,columnname2,value2):
        try:
            self.cur.execute(f"update {tablename} set {columnname1} = '{value1}' where {columnname2} = '{value2}'")
            self.conn.commit()
            print("update done successfully")  
            self.conn.close() 
        except pymysql.err.ProgrammingError:
            print("table doesn't exist") 
        except pymysql.err.OperationalError:
            print("column not there in table") 
        except pymysql.err.DataError:
            print("sorry! there is an error in data types")  
        except pymysql.err.InterfaceError:
            print("sorry!. you are updating primary key,duplicate entries recorded")                

    def delete(self,tablename,columnname,value):
        try:
            self.cur.execute(f"delete from {tablename} where {columnname} = '{value}'")
            self.conn.commit()
            print("successfully deleted")
            self.conn.close()
        except pymysql.err.ProgrammingError:
            print("table doesn't exist") 
        except pymysql.err.OperationalError:
            print("column not there in table") 
        except pymysql.err.InterfaceError:
            print("interface error")    

def main():
    obj=datamethods('localhost','root','Kamal@230167','gvp')

    while True:
        print("select 1 if you want to read the table")
        print("select 2 if you want to insert into table")
        print("select 3 if you want to update the table")
        print("select 4 if you want to delete table")
        print("select 5 if you want to quit")

        choice=int(input("enter your choice: "))

        if choice==1:
            tablename=str(input("please enter the table name : "))
            num=int(input("enter the number of columns : "))
            columnname=[]
            for i in range(1,num+1):
                print("enter columnname:",i)
                columnname.append(input())
            obj.read(tablename,columnname)
        elif choice==2:
            tablename=str(input("please enter the table name : "))
            values=list(input("please provide values to insert with spaces: ").split())
            values=tuple(values)
            obj.insert(tablename,values)
        elif choice==3:
                tablename=str(input("please enter the table name : "))
                columnname1=str(input("please enter the column that need to be updated : "))
                value1=input("enter the value to be updated : ")
                columnname2=str(input("please enter the columnname wherre it is needed to be updated: "))
                value2=input("enter the value for where clause: ")           
                obj.update(tablename,columnname1,value1,columnname2,value2)
        elif choice==4:
            tablename=str(input("please enter the table name : "))
            columnname=str(input("please enter the column from where it to be deleted : "))
            value=input("enter the value for where clause : ")
            obj.delete(tablename,columnname,value)
        elif choice==5:
            print("thankyou! successfully quited from platform")
            break
        else:
            print("invalid choice. please select between 1 - 5 ")
            print("thank you")

if __name__=="__main__":
    main()
# how to do if more than 3 cloumns are selected by users
   
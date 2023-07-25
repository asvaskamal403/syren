import pymysql

conn_obj = pymysql.connect(host="localhost",user="root",password="Kamal@230167",db="gvp")

cursor = conn_obj.cursor()

cursor.execute("SHOW TABLES")

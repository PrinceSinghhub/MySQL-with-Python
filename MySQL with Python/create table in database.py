import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "create table stu_marks(rollNo int(3) primary key,Name varchar(20),lang varchar(10),Branch varchar(10),Percent decimal(2.2))"
conn = MySql.cursor()
conn.execute(sql_quari)
conn.close()
MySql.close()


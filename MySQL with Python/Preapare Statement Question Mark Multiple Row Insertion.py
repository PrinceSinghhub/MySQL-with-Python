import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo using ?
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(?,?,?,?,?)"


# todo create a list of tuple to execute this syntax using executemany()

conn = MySql.cursor(prepared=True)
param = [(130,"PS","Python","AI",80),
         (131,"P Singh","Java","AI",76)]
try:
    conn.executemany(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")
conn.close()
MySql.close()

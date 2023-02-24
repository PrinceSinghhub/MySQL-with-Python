import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo usining ?Mark
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(?,?,?,?,?)"


conn = MySql.cursor(prepared=True)
param = (123,"K JAISWAL","C","AI",70)
try:
    conn.execute(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")
conn.close()
MySql.close()

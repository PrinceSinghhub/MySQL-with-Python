import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo using %c
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(%s,%s,%s,%s,%s)"


conn = MySql.cursor(prepared=True)
param = (122,"PR SINGH","Python","B TECH",75)
try:
    conn.execute(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")
conn.close()
MySql.close()

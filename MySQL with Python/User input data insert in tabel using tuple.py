import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using Tuple Parameter
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(%s,%s,%s,%s,%s)"

conn = MySql.cursor()

rollNo = int(input("Enter RollNo: "))
Name = input("Enter Name: ")
Lang = input("Enter Lang Name: ")
Branch = input("Enter Branch Name: ")
Perce = input("Enter Percent: ")

param = (rollNo,Name,Lang,Branch,Perce)

try:
    conn.execute(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")

conn.close()
MySql.close()

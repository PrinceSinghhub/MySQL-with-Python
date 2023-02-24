import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(%(rollNo)s,%(Name)s,%(lang)s,%(Branch)s,%(Percent)s)"


conn = MySql.cursor()

rollNo = int(input("Enter RollNo: "))
Name = input("Enter Name: ")
Lang = input("Enter Lang Name: ")
Branch = input("Enter Branch Name: ")
Perce = input("Enter Percent: ")


param = {'rollNo':rollNo,'Name':Name,'lang':Lang,'Branch':Branch,'Percent':Perce}
try:
    conn.execute(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")


# todo show tabel in database
sql_quari = "select * from stu_marks"
conn.execute(sql_quari)
rows = conn.fetchall()
for i in rows:
    print(i)

conn.close()
MySql.close()

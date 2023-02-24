import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "delete from stu_marks where rollNo = 111"


conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    print("Sucessfully data delete in Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not delete data")

conn.close()
MySql.close()
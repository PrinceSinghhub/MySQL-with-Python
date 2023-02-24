import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "update stu_marks set percent = 87 where rollNo = 110"


conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    print("Sucessfully data update in Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not update data")

conn.close()
MySql.close()
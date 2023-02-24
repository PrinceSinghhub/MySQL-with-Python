# todo this property only work with auto_increment values in databases other wise return 0
import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(112,'KP','PYTHON','B TECH',100)"


conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    print("Sucessfully data insert in Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not insert data")

# // todo lastrowid
print(f"{conn.lastrowid} last row id")
conn.close()
MySql.close()
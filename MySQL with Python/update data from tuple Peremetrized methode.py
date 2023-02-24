import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using Tuple Parameter
sql_quaries = "update stu_marks set lang = %s where rollNo = %s"
conn = MySql.cursor()

try:
    conn.execute(sql_quaries,('C',107))
    MySql.commit()
    print("Update Data Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not update")

conn.close()
MySql.close()

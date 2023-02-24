import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using Tuple Parameter
sql_quaries = "delete from stu_marks where rollNo = %s"
conn = MySql.cursor()

try:
    conn.execute(sql_quaries,(124,))
    MySql.commit()
    print("Data delete Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not delete")

conn.close()
MySql.close()

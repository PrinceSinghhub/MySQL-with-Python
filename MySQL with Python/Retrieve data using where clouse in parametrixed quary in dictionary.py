import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "select * from stu_marks where Percent > %(Percent)s"
conn = MySql.cursor()

try:
    conn.execute(sql_quaries, {'Percent':90})
    row = conn.fetchall()
    for i in row:
        print(i)
    print("Data fetch Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not Fetch")

conn.close()
MySql.close()

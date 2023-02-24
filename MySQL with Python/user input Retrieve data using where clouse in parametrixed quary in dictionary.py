import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "select Name from stu_marks where Branch = %(Branch)s"
conn = MySql.cursor()

retrew_data = input("Enter Branch: ")
param = {'Branch':retrew_data}

try:
    conn.execute(sql_quaries, param)
    row = conn.fetchall()
    for i in row:
        print(i)
    print("Data fetch Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not Fetch")
print(f"{conn.rowcount} affected Row")
conn.close()
MySql.close()

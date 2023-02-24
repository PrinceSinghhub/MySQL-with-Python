import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "select * from stu_marks"  #all sql quaries use here


conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    row = conn.fetchall()
    print(row)
    for i in row:
        print(i)

    print("Sucessfully data fetch in a Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not fetch data")
print("total row",conn.rowcount)
conn.close()
MySql.close()
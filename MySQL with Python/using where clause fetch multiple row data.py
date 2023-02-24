import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "select name,Branch from stu_marks where percent > 90"  #all sql quaries use here


conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    row = conn.fetchone()
    while row is not None:
        print(row)
        row = conn.fetchone()
    print("Sucessfully data fetch in a Table using where clouse")

except:
    MySql.rollback()
    print("Ooops Something Worng! not fetch data")
print("total row",conn.rowcount)
conn.close()
MySql.close()
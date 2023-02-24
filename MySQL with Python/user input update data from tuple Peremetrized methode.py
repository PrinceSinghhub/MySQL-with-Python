import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using Tuple Parameter
sql_quaries = "update stu_marks set lang = %s where rollNo = %s"
conn = MySql.cursor()

update_data = input("Enter Lang: ")
where_update = int(input("Enter rollNo: "))
param = (update_data,where_update)

try:
    conn.execute(sql_quaries,param)
    MySql.commit()
    print("Update Data Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not update")

conn.close()
MySql.close()

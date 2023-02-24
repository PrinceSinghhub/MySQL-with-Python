import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "update stu_marks set Branch = %(Branch)s where rollNo = %(rollNo)s"

conn = MySql.cursor()

updated_data = input("Enter Branch: ")
where_update = int(input("Enter rollNo: "))
param = {'Branch':updated_data,'rollNo':where_update}
try:
    conn.execute(sql_quaries, param)
    MySql.commit()
    print("update Data Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not update")

conn.close()
MySql.close()

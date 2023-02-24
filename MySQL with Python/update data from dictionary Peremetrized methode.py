import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "update stu_marks set lang = %(lang)s where rollNo = %(rollNo)s"

conn = MySql.cursor()
try:
    conn.execute(sql_quaries, {'lang':"C,JAVA",'rollNo':103})
    MySql.commit()
    print("Data delete Sucessfully")
except:
    MySql.rollback()
    print("Oooops Data not delete")

conn.close()
MySql.close()

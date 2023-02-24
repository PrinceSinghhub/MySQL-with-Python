import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(104,'Babu','PYTHON','B TECH',85.95)," \
                                                                      "(105,'PR SINGH','PYTHON','B TECH',97.50)," \
                                                                       "(106,'MR SINGH','PYTHON','B TECH',88.90)"
'''also use as simple if not any error
conn = MySql.cursor()
conn.execute(sql_quari)
MySql.commit()'''

conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    MySql.commit()
    print("Sucessfully data insert in Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not insert data")

conn.close()
MySql.close()
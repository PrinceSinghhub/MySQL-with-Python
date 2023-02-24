import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(107,'Khushi','PYTHON','B TECH',85.95)," \
                                                                      "(108,'Khushi Jaiswal','PYTHON','B TECH',92.50)," \
                                                                       "(109,'Fire Brigrade','PYTHON','B TECH',87.90)"

conn = MySql.cursor()
try:
    conn.execute(sql_quari)
    print("Sucessfully data insert in Tabel")
except:
    MySql.rollback()
    print("Ooops Something Worng! not insert data")

# // todo rowcount
print(f"{conn.rowcount} rows are affected")
conn.close()
MySql.close()
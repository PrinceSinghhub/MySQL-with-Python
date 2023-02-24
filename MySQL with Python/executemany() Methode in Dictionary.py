import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using dictionary Parameter
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(%(rollNo)s,%(Name)s,%(lang)s,%(Branch)s,%(Percent)s)"


conn = MySql.cursor()
param = [{'rollNo':118,'Name':'PRINCE SINGH','lang':'JAVA','Branch':'B TECH','Percent':90.66},
        {'rollNo':119,'Name':'PRINCE','lang':'Python','Branch':'AI','Percent':97.66},
        {'rollNo':120,'Name':'P SINGH','lang':'JAVA','Branch':'AI','Percent':85.66}]
try:
    conn.executemany(sql_quaries,param)
    MySql.commit()
    print("Data insert sucessfully")
except:
    MySql.rollback()
    print("ooopss Data not inserted")


# todo show tabel in database
sql_quari = "select * from stu_marks"
conn.execute(sql_quari)
rows = conn.fetchall()
for i in rows:
    print(i)

conn.close()
MySql.close()

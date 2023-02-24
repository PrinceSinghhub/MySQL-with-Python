import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")

sql_quari = "show tables"
conn = MySql.cursor()
conn.execute(sql_quari)

for i in conn:
    print(i)
conn.close()
MySql.close()
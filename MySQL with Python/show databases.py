import mysql.connector

Mysql = mysql.connector.connect(user='root',password='2005@Anushka',host='localhost',port=3306)
print(Mysql.is_connected())

show = 'show databases' #syntax of sql show database
conn = Mysql.cursor()
conn.execute(show)

for i in conn:
    print(i)
conn.close()
Mysql.close()


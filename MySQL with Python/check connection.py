import mysql.connector
Mysql = mysql.connector.connect(user='root',password='2005@Anushka',host='localhost',port=3306)
print(Mysql.is_connected())
Mysql.close()

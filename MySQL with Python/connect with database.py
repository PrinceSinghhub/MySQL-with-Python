import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='operators',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


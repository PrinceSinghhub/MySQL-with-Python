import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',host='localhost',port=3306)
print(MySql.is_connected())


# todo create databse
sql_Quarie = "create database python_database"
database = MySql.cursor()
database.execute(sql_Quarie)

database.close()
MySql.close()

import mysql.connector as mc
MySql = mc.connect(user='root', password='2005@Anushka',database='python_database', host='localhost', port=3306)
conn = MySql.cursor()

sql_quary = "drop table namo"
try:
    conn.execute(sql_quary)
    MySql.commit()
    print("Table Sucessfully Delete in DataBase")

except:
    print("Oooops Table not Delete in DataBase")
conn.close()
MySql.close()

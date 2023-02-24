import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo using ?
def insert_data(param):
    sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(?,?,?,?,?)"
    conn = MySql.cursor(prepared=True)
    try:
        conn.executemany(sql_quaries,param)
        MySql.commit()
        print("Data Insertion Sucessfully")
    except:
        MySql.rollback()
        print("Data Insertion Not Sucessfully")
    conn.close()
    MySql.close()


n = int(input("Num of Tuples: "))
param = []
for i in range(n):
    rollNo = int(input("Enter RollNo: "))
    Name = input("Enter Name: ")
    Lang = input("Enter Lang Name: ")
    Branch = input("Enter Branch Name: ")
    Perce = input("Enter Percent: ")

    Tuple = (rollNo, Name, Lang, Branch, Perce)
    param.append(Tuple)
insert_data(param)




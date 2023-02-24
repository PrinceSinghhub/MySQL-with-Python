import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


def data_insert(rollNo, Name, Lang, Branch, Perce):
    # todo using %s
    sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(?,?,?,?,?)"
    param = (rollNo, Name, Lang, Branch, Perce)
    conn = MySql.cursor(prepared=True)
    try:
        conn.execute(sql_quaries,param)
        MySql.commit()
        print("Data Insert Sucessfully")
    except:
        MySql.rollback()
        print("Oppps data not insert")
    conn.close()
    MySql.close()

while True:
    rollNo = int(input("Enter RollNo: "))
    Name = input("Enter Name: ")
    Lang = input("Enter Lang Name: ")
    Branch = input("Enter Branch Name: ")
    Perce = input("Enter Percent: ")

    data_insert(rollNo,Name,Lang,Branch,Perce)
    comm = input("Y or N")
    if comm == "N":
        break

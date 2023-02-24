import mysql.connector as mc
MySql = mc.connect(user='root',password='2005@Anushka',database='python_database',host='localhost',port=3306)
print(MySql.is_connected())
print("connected with database")


# todo Parametrixe methode using Tuple Parameter
sql_quaries = "insert stu_marks(rollNo,Name,lang,Branch,Percent) values(%s,%s,%s,%s,%s)"

conn = MySql.cursor()

def insert_data(rn,n,l,b,p):
    param = (rn,n,l,b,p)
    try:
        conn.execute(sql_quaries,param)
        MySql.commit()
        print("Data insert sucessfully")
    except:
        MySql.rollback()
        print("ooopss Data not inserted")

# todo multiple user input
while True:
    rollNo = int(input("Enter RollNo: "))
    Name = input("Enter Name: ")
    Lang = input("Enter Lang Name: ")
    Branch = input("Enter Branch Name: ")
    Perce = input("Enter Percent: ")
    insert_data(rollNo,Name,Lang,Branch,Perce)

    comm = input("Press Y or N: ")
    if comm == 'Y':
        pass
    else:
        break
conn.close()
MySql.close()
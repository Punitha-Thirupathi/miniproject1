from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="tjroot", password="9942233593tjp", database="student")


def insert(sno,sname,pertng):
    res = con.cursor()
    sql = "insert into student(sno,sname,pertng)values(%s,%s,%s)"
    res.execute(sql, (sno, sname, pertng))
    con.commit()
    print("Data Insert Sucessfully!!!")


def update(sno,sname,pertng):
    res = con.cursor()
    sql = "update student set pertng=%s where sno=%s And sname=%s"
    res.execute(sql,(pertng,sno,sname))
    con.commit()
    print("Data Update sucessfully!!!")


def select():
    res = con.cursor()
    sql = "select*from student"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["sno", "sname", "pertng"]))
    con.commit()
    print("Data Selected sucessfully")


def delete(sname):
    res = con.cursor()
    sql = "delete from student where sname=%s"
    res.execute(sql,(sname))
    con.commit()
    print("Data deleted sucessfully")

while(True):
    print("1.insert Data")
    print("2.update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter the choice"))
    if(choice==1):
      sno=int(input("Enter the Serial number"))
      sname=input("Enter the name")
      pertng=int(input("Enter the percentage"))
      insert(sno,sname,pertng)
    elif(choice==2):
       sno=int(input("Enter the Serial number"))
       sname=input("Enter the name")
       pertng=int(input("Enter the percentage"))
       update(sno,sname,pertng)
    elif(choice==3): 
         select()
    elif(choice==4):
        sname=input("Enter the sname")
        delete(sname)
    elif(choice==5):
        quit()
    else:
       print("Invalid Option!!!")


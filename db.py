#dbms with python
import sqlite3
connection=sqlite3.connect('sample.db')
cursor=connection.cursor()
print("connected")
def createTable(query):
    cursor.execute(query)
    print("created")
def insert():
    name=input("enter the student name: ")
    age=int(input("enter age: "))
    mark=int(input("enter the mark: "))
    cursor.execute("Insert into studentdb4 values(?,?,?)",(name,age,mark))
    print("inserted successfully")
def update():
    name=input("enter the student name: ")
    mark=int(input("enter the mark: "))
    cursor.execute("update studentdb4 SET mark= ? WHERE name=?",(mark,name))
    print("updated successfully")
def display():
    row=cursor.execute("select * from studentdb4").fetchall()
    print(row)

query="CREATE TABLE studentdb4(name text,age integer,mark integer)"
createTable(query)
print("Enter the operation to be performed: 1.insert 2.update 3.display 4.exit")
choice=int(input())
while(choice!=4):
    if(choice==1):
        insert()
    elif(choice==2):
        update()
    elif(choice==3):
        display()
    else:
        print("recheck the choice entered")
    print("Enter the operation to be performed: 1.insert 2.update 3.display 4.exit")
    choice=int(input())
   

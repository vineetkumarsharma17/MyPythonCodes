import mysql.connector
def select():
    sql='select * from emp order by name'
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        print(i)
def insert():
    name=input("Enter name:")
    i=input("Enter id:")
    sql='insert into emp values(%s,%s)'
    val=[name,i]
    cursor.execute(sql,val)
    mydb.commit()
def dele():
    i=input("enter id to delete:")
    sql='delete from emp where id=%s'
    val=(i,)
    cursor.execute(sql,val)
    mydb.commit()
    print("Deleted")


mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='pythondatabase'
)
while(1):
    cursor=mydb.cursor()
    print("1.insert\n2.delete\n3.display")
    ch=int(input("Enter choice:"))
    if(ch==1):
        insert()
    elif(ch==2):
        dele()
    elif(ch==3):
        select()
    else:break
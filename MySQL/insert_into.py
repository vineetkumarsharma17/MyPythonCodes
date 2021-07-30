import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user="root",
    password="1234",
    database='pythondatabase'
)

sql = "INSERT INTO emp (name, id) VALUES (%s, %s)"
name=input("Enter name:")
r=input("Enter id:")
cursor=mydb.cursor()
cursor.execute(sql,[name,r])
mydb.commit()

mydb.close()
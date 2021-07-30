import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='pythonDatabase'
)
mycursor=mydb.cursor()
sql='delete from emp where id=%s'
val=('1',)
mycursor.execute(sql,val)
mydb.commit()
mydb.close()
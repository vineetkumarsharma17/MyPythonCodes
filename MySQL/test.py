import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database='pythondatabase'
)
cursor=mydb.cursor()
sql='create table std2(id int,name varchar(25))'
# val=('std1',)
#sql='create table emp(name varchar(25),id int)'
cursor.execute(sql)
mydb.commit()
mydb.close()
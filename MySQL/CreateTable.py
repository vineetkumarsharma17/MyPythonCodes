import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='pythonDatabase'
)
mycursor=mydb.cursor()
query='create table emp(name varchar(25),id int)'
# query='desc emp'
print(mycursor.execute(query))

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pythondatabase"
)
cursor=mydb.cursor()
sql='select * from emp order by id'
cursor.execute(sql)
data=cursor.fetchall()
lis=[]
for i in data:
    tmp=[]
    for j in i:
        tmp.append(j)
    lis.append(tmp)
for i in lis:
    i[0],i[1]=i[1],i[0]

for i in lis:
    print(i)

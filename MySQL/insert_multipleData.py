import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pythondatabase"
)
cursor=mydb.cursor()

sql = "INSERT INTO emp (Name, id) VALUES (%s, %s)"
val = [("Akash", "98"),
       ("Neel", "23"),
       ("Rohan", "43"),
       ("Amit", "87"),
       ("Anil", "45"),
       ("Megha", "55"),
       ("Sita", "95")]

cursor.executemany(sql, val)
# cursor.execute(q,val)
mydb.commit()
mydb.close()
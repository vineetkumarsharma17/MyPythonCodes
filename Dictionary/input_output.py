std=dict()
n=int(input("Enter the number of student:"))
for i in range(n):
    id=int(input("enter id"))
    name=input("Enter name:")
    std[id]=name
for i in std:
    print(i)
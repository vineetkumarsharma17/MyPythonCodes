std=dict()
n=int(input("Enter the number of student:"))
for i in range(n):
    id=int(input("enter id"))
    name=input("Enter name:")
    std[id]=name
re=int(input("enter id to delete value"))
std.pop(re)#using pop
print(std)
re=int(input("enter id to delete value"))
del std[re]#using del
print(std)
n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
a=int(input("Enter a number to search:"))
if(a in lis):
    print("value exist")
else:
    print("value not found")
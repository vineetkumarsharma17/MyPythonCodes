n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
num=int(input("Enter number to delete"))
if(num in lis):
    lis.remove(num)
else:
    print("Number not found")
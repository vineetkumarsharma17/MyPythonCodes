n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
lis2=[val for val in lis if (val%2==0)]
print(lis2)
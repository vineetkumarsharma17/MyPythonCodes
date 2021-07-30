n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
lis2=[]
for i in range(len(lis)-1,-1,-1):#first method
    lis2.append(lis[i])
print(lis2)
#second method
lis2=lis[::-1]
print(lis2)
#third method
lis2=lis
lis2.reverse()
print(lis2)
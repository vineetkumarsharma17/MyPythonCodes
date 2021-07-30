n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
#first method
total=0
for i in lis:
    total+=i
print(total)
#Second method usinng built in function sum
print(sum(lis))
n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
# method 2 with tyr and except method
try:
    lis=[]
    while True:
        lis.append(int(input()))
except:
    print(lis)

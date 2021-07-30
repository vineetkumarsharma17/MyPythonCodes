def swap1(lis,p1,p2):
    lis[p1],lis[p2]=lis[p2],lis[p1]
    return lis
def swap2(lis,p1,p2):#using pop and insrt function
    tmp2=lis.pop(p2)
    tmp1=lis.pop(p1)
    lis.insert(p1,tmp2)
    lis.insert(p2,tmp1)
    return  lis
def swap3(lis,p1,p2):#using tuple
    tup=lis[p2],lis[p1]
    lis[p1],lis[p2]=tup#extracting tuple
    return lis

n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
p1=int(input("Enter position 1:"))
p2=int(input("Enter position2:"))
lis =swap1(lis,p1,p2)
print(lis)
p1=int(input("Enter position 1:"))
p2=int(input("Enter position2:"))
lis =swap2(lis,p1,p2)
print(lis)
p1=int(input("Enter position 1:"))
p2=int(input("Enter position2:"))
lis =swap3(lis,p1,p2)
print(lis)




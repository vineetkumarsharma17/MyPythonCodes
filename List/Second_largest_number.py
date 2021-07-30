n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
#first method
mx=lis[0]
smx=lis[1]
for i in range(len(lis)):
    if(lis[i]>mx):
        smx=mx
        mx=lis[i]
    elif(lis[i]>smx and lis[i]!=mx):
        smx=lis[i]
print(smx)
#second method
lis2=lis
lis2.sort()#sort list in assending order
print(lis[-2])
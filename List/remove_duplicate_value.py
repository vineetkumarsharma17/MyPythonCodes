n=int(input("Enter the number of element:"))
lis=[]
for i in range(n):
    val=int(input("Enter value:"))
    lis.append(val)
print(lis)
# first method
res=[]
for i in lis:
    if(i not in res):
        res.append(i)
print(res)

#using set
lis=list(set(lis))
print(lis)
lis2=lis
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if(lis[i]==lis[j]):
            lis.remove(lis2[j])
print(lis2)
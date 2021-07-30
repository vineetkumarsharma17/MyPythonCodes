def meth1():
    lis=list()
    n=int(input("Entet the number of element"))
    for i in range(n):
        lis.append(int(input("Enter value:")))
    return lis
lis=meth1()
print("List before interchange.",lis)
lis[0],lis[-1]=lis[-1],lis[0]
print("List after interchange.",lis)
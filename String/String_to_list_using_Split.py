a=[]
def fun():
    str=input("Enter operation")
    lis=str.split()
    if(lis[0]=='append'):
        a.append(int(lis[1]))
    elif(lis[0]=='insert'):
        a.insert(int(lis[-1]),int(lis[-2]))
    else:
        print("Wrong input")
fun()
fun()
fun()
print(a)

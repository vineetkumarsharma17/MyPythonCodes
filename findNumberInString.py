str=input("Enter a string")
list=[]
sum=0
for x in str:
    if(x>='0'and x<='9'):
        list.append(x)
if(len(list)==0):
    print("No digit")
else:
    for x in list:
        sum+=int(x)
    print("String:",str)
    print("number:",list)
    print("sum of digit:",sum)




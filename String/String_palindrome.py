str=input("Enter a String:")
str2=str[::-1]
print(str2)
if(str==str2):
    print("palindrome")
else:
    print("not palindrome")
#second method
mid=len(str)//2
s=l=0
flag=False
for i in range(mid+1):
    if(str[s]==str[l]):
        l-=1
        s+=1
    else:
        flag=True
        break
if(flag!=True):
    print("not palindrome")
else:print("palindrome")
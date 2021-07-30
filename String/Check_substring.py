str=input("Enter a string:")
sub=input("Enter sub string:")
if sub not in str:
    print("not")
else:print("yes")
#using find method
if(str.find(sub)==-1):
    print("not")
else:print("yes")
import math
print("Enter the value of a,b,c in a**2+bx+c=0")
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
if(a==0):
    print("A should not be zero\nAborting....")
else:
    d=b**2-4*a*c
    if(d>0):
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Roots are real and unequal")
        print("roots1:",r1)
        print("roots2:",r2)
    elif(d==0):
        print("Roots are real and equal")
        r1=-b/(2*a)
        print("roots:",r1)
    else:
        print("roots are complex and imaginary")


valu=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
sys=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

def convert(x):
    i=12
    rom=''
    while(x!=0):
        if(valu[i]<=x):
            x-=valu[i]
            rom+=sys[i]
        else:
            i-=1
    return rom
def convert_using_Dictionary(n):
    d={}
    for i in range(len(valu)-1,-1,-1):
        d[valu[i]]=sys[i]#copying value and symbol in reverse order
    rom=''
    while (n>0):
        for i in d:
            if(i<=n):
                n-=i
                rom+=d[i]
                break
    return rom

print(convert(435))
print(convert_using_Dictionary(435))
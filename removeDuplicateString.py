strr="xabbcacpqr"
lis=list(strr)
print(lis)
s=set(lis)
s=list(s);
print(s)
c={}
for i in s:
    x=lis.count(i);
    c[i]=x
print(c)
print(lis.index('b'))

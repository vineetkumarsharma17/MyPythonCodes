class cal:
    def __init__(self,n):
        self.n=n
    def add(self,a,b):
        return (a+b)
    def sub(self,a,b):
        return (a-b)
    def mul(self,a,b):
        return (a*b)
    def sqr(self):
        return (self.n**2)

v=cal(3)
print(v.add(3,4))

print(v.sub(5,3))
print(v.mul(5,3))
print(v.sqr())

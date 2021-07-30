class std:
    def getData(self):
        self.name=input("Enter name:")
        self.id=int(input("Enter id:"))
        self.add=input("Enter address")
s1=std()
s2=std()
s1.getData()
s2.getData()
print(s1.__dict__)
lis=[s1,s2]
for s in lis:
    for j in s.__dict__:
        print(f'{j}-->{getattr(s,j)}')
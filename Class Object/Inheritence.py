class person(object):
    def __init__(self,name):
        self.name=name
    # def pri(self):
    #     print(self.name)
class chile(person):
    def __init__(self,name,id):
        person.__init__(self,name)
        self.id=id
    pass
# x=person('vineet')
# x.pri()
y=chile('vineet',67)
print(y.name)
print(y.id)
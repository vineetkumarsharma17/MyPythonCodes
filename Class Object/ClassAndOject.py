class std:
    name='vineet'
    def putData(self):
        print(f"name is {self.name}")
    def getData(self):
        self.name=input("Enter name:")

vk=std()
vk.getData()
vk.putData()

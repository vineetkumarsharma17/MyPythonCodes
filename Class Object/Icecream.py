class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        lis=[]
        if(len(self.ingredients)==0 or len(self.toppings)==0):
            return lis
        for i in self.ingredients:
            for j in self.toppings:
                lis.append([i,j])
        return lis

        pass

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
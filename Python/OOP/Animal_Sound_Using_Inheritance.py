class animal:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class dog(animal):
    def display(self):
        print("your Dog Name is",self.name + " And price is",self.price)

class cat(animal):
    def display(self):
        print("your Cat Name is", self.name +" And price is",self.price)

d1 = dog("juju",100000)
c1 = cat("mety",100000)
d1.display()
c1.display()
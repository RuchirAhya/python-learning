class Rectangle:
    def __init__(self,langth,width):
        self.langh = langth
        self.width = width
    
    def calculate_area(self):
        return self.langh*self.width

r = Rectangle(10,5)
print("Area =",r.calculate_area()) 
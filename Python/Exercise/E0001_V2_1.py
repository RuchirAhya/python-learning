'''Exercise: E001-V2
Create one class named "category" with members "name", "code", "no_of_products" Done 
Create one class named "product" with members "name", "code", "category", "Price" Done

Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class. Done
Add a new member function to generate “display_name”. Done

“display_name” has the text value as below.Done
   1.Vehicle category without parent then “Vehicle” 
   2.Car category with “Vehicle” as a parent then “Vehicle main  > Car subclass”
   3.Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”

Create 5 category objects with parent and child relation.
Create 3 product objects in each category.

Display Category with its Code, Display Name and all product details inside that category.
Display product list by category (group by category, order by category name).'''
class category:
    def __init__(self,name,code,no_of_products,parent,display_name,products):
        self.name = name 
        self.code = code 
        self.no_of_products = no_of_products
        self.parent = parent
        self.Display_name = display_name
        self.products = products
    
    def display_name(c1):
     class vehicle:
         print("this is class vehicle")
     class car(vehicle):
         print("this is class car")
     class petrol(car):
         print("this is class petrol")
         for y in c1:
           print("your product Name is :",y.name )
           print(" Product code is :",y.code)
           print("Product no of products :",y.no_of_products)
           print("Product Parent is :",y.parent)
           print("Product Display Name :",y.Display_name)
           print("Product of Products :",y.products)
           print("-"*20)
         print("-"*30)
     a = 0
     if a == 0 :
         petrol()
         a == 1
     else:
        pass    
          
              
class product:
    def __init__(self,name,code,category,price):
     self.name = name
     self.code = code
     self.category = category
     self.price = price

    def display(products):
         
          print("Product")
          print("Product Name :",products.name)
          print("Product Code :",products.code)
          print("Product Category :",products.category)
          print("Product Price :",products.price)
          print("-"*20)
          print("*"*30)
    
    def Search(products):
     code_name = input("Enter Name here : ")

     if code_name in products.name:
        print("Product Found")
        print("Product Name :", code_name)
        print("*" * 15)
     else:
        print("Product Not Found")
        print("*" * 15)
 
c1 = [
 category("tata","C1",100,"car","tata car","petrol"),
 category("hyundai","C2",200,"car","hundai car","petrol"),
 category("toyota","C3",500,"car","toyota car","petrol"),
 category("volkswagen","C4",150,"car","volkswagen car","petrol"),
 category("BMW","C5",300,"car","BMW car","petrol")
]

print("Insert Value")
products = product([(input("Enter Name :")) for x in range(0,5)],[input("Entar Code :") for x in range(0,5)],[input("Entar Category :") for x in range(0,5)],[input("Entar Price :") for x in range(0,5)])

category.display_name(c1)
product.display(products)

print("Search Value")
product.Search(products)
'''Exercise: E001-V3:
Create one class named “location” with members “name”, “code”.
Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. This method will return all “movement” objects which belong to the passed “product” as an argument.
Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.

Create 4 different location objects.
Create 5 different product objects.

Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 

Display movements of each product using the “movement_by_product” method.
Display product details with its stock at various locations using “stock_at_locations”.
Display product list by location (group by location).'''

class product:
    def __init__(self,name,code,category,price,stock_at_locations):
     self.name = name
     self.code = code
     self.category = category
     self.price = price
     self.stock_at_locations = stock_at_locations


    def display(products):
         for x in products:
          print("Product")
          print("Product Name :",x.name)
          print("Product Code :",x.code)
          print("Product Category :",x.category)
          print("Product Price :",x.price)
          print("Product stock_at_locations :",x.stock_at_locations)
          print("-"*20)
         print("-"*30)

class location:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    
    def display(locations):
     for x in locations:
      print("Location is :",x.name)
      print("Location code is :",x.code)
      print("-"*20)
     print("-"*30)

class movement:
   
   def __init__(self,from_location,to_location,Product,quantity): 
     self.from_location = from_location
     self.to_location = to_location
     self.product = Product
     self.quantity = quantity   

   def movements_by_product(products):
    print("move")

    product_name = input("Enter Product Name : ")
    from_location = input("Enter Product From : ")
    to_location = input("Enter Product To : ")
    quantity = int(input("Enter Product Quantity : "))

    found = 0

    for p in products:
        if p.name.lower() == product_name.lower() and from_location in p.stock_at_locations and to_location in p.stock_at_locations and p.stock_at_locations[from_location] >= quantity:
            found = 1

            print("Product Found")
            print("Product Name :", p.name)
            print("Product From :", from_location)
            print("Product To :", to_location)
            print("Product Quantity :", quantity)
            print("-" * 15)
            p.stock_at_locations[from_location] -= quantity
            p.stock_at_locations[to_location] += quantity
            print("Product")
            print("Product Name :",p.name)
            print("Product Code :",p.code)
            print("Product Category :",p.category)
            print("Product Price :",p.price)
            print("Product stock_at_locations :",p.stock_at_locations)
            print("-"*20)
            break

    if found == 0:
        print("Data is Not Correct")
   
locations = [
   location("Rajkot",360001),
   location("Connaught Place",110001),
   location("Park Street",700016),
   location("T.Nagar",600017),
]

products = [
   product("UltraNoteX","L1","laptop",68500,{"Rajkot":300,"T.Nagar":200,"Connaught Place":170,"Park Street":120}),
   product("Land Cruiser","C1","car",63000,{"Rajkot":150,"T.Nagar":50,"Connaught Place":75,"Park Street":110}),
   product("CoreMaxWorkstation","P1","PC",88000,{"Rajkot":350,"T.Nagar":240,"Connaught Place":150,"Park Street":100}),
   product("Corolla","C2","Car",24975,{"Rajkot":60,"T.Nagar":50,"Connaught Place":75,"Park Street":110}),
   product("VisionBookAir","L2","laptop",59999,{"Rajkot":150,"T.Nagar":50,"Connaught Place":75,"Park Street":120})
]

product.display(products)
location.display(locations)
movement.movements_by_product(products)
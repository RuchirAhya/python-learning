
print("Create one class named category with members name, code, no_of_products")
class category:
   def __init__(self,name,code,no_of_products):
      self.name = name
      self.code = code
      self.no_of_products = no_of_products
   def display(self):
    print("your product Name is :",self.name )
    print(" Product code is :",self.code)
    print("Product no of products :",self.no_of_products)
    print("*"*15)
print("-"*30)

print("Create one class named product with members name, code,category,Price.")
class product:
    def __init__(self,name,code,category,Price):
        self.name = name
        self.code = code
        self.category = category
        self.Price = Price
    def display(self):
         print("your Product Name is",self.name)
         print(" Product code is",self.code)
         print("And category of products is",self.category)
         print("and products price is",self.Price)
         print("*"*15)
    
    def Search(products):
          code_search = input("Enter Code hear :")
          c = 0
          for x in products:
             if x.code == code_search:
                c = c+1
                print("Product Found")
                print("Product Name :",x.name)
                print("Product Code :",x.code)
                print("Product Category :",x.category)
                print("Product Price :",x.Price)
                print("*"*15)
                break

          if c == 0:
              print("Product Not Found")
              print("*"*15)
    
    def Sort_Low_to_High(products):
       d = len(products)

       for x in range(d-1):
          for y in range(d-x-1):
             if products[y].Price > products[y+1].Price:
                products[y],products[y+1]=products[y+1],products[y]

       for x in products:
          print("Product Found")
          print("Product Name :",x.name)
          print("Product Code :",x.code)
          print("Product Category :",x.category)
          print("Product Price :",x.Price)
          print("*"*15) 
    
    def Sort_High_to_Low(products):
       d = len(products)
       for x in range(d-1):
          for y in range(d-x-1):
             if products[y].Price < products[y+1].Price:
                products[y],products[y+1]=products[y+1],products[y]

       for x in products:
          print("Product Found")
          print("Product Name :",x.name)
          print("Product Code :",x.code)
          print("Product Category :",x.category)
          print("Product Price :",x.Price)
          print("*"*15)      
print("-"*30)

print("Create three objects of a category.")
a1 = category("Phone","P1",10)
a2 = category("Laptop","L1",20)
a3 = category("PC","C1",30)
print("-"*30)

print("Create 10 different products. The code must be unique.")
products =[
 product("GalaxyNovaX1","P1.1","Phone",24999),
 product("PixelSpark7","P1.2","Phone",31500),
 product("TitanMobilePro","P1.3","Phone",18999),
 product("AeroBook15","L1.1","Laptop",52000),
 product("UltraNoteX","L1.2","Laptop",68500),
 product("SwiftEdge14","L1.3","Laptop",45999),
 product("PowerStationMini","C1.1","PC",39000),
 product("ThunderDesktopPro","C1.2","PC",72500),
 product("CoreMaxWorkstation","C1.3","PC",88000),
 product("VisionBookAir","L1.4","Laptop",59999)
]
print("-"*30)

print("Print category info with its no_of_products.")
a1.display()
a2.display()
a3.display()
print("-"*30)

print("Search product using its code.")
product.Search(products)
print("-"*30)

print("Sort and Print products based on price (Lo.4w to High) with all details. (without using built-in Function)")   
product.Sort_Low_to_High(products) 
print("-"*30)

print("Sort and Print products based on price (Price High to Low) with all details.") 
product.Sort_High_to_Low(products) 
print("-"*30)   
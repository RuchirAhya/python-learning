'''Create a program that:

Displays the list
Adds a new item
Removes an item
Searches for an item
Sorts the list
Reverses the list
Shows total number of elements'''
l1 = [1,2,3,4,5]
a = int(input("Enter value for Add :"))
y = 0
class list1:
    def __init__(self,l1,a,y):
        self.l1 = l1
        self.a = a
        self.y = y

    def Displays(l1):
        print(l1)
        print("-"*30)

    def Adds(l1,a):
        l1.append(a)
        print(a,"is Added.")
        print(l1)
        print("-"*30)
    
    def Removes(l1,a):
        if l1 == 0:
            print("List is empty")
        else:    
         l1.remove(a)
         print(a,"is Removed.")
        print(l1)
        print("-"*30)

    def Searches(l1):
        b = int(input("Enter a value for Searches:"))
        c = 0
        for x in l1:   
         if b == x:
             c += 1
        if c == 1:
             print(b,"Value found.")
             print(l1)
        else:
              print(b,"Value not found.")
              print(l1)
        print("-"*30)    
    
    def Sorts(l1):
        l1.sort()
        print("Sort the list in Ascending :",l1)
        print("-"*30)
        l1.sort(reverse = True)
        print("Sort the list in Descending :",l1)
        print("-"*30)
    
    def Reverses(l1):
        l2 = []
        for x in range(len(l1),0,-1):
         l2.append(x)  
        print("Reverses the list is :",l2)
        print("-"*30)    

    def total_elements(l1):
        print("total elements in list :",len(l1))
        print("-"*30)

    def total(l1,y):
        for x in l1:
         y += x
        print("total of list's elements :",y)
        print("-"*30)
        
list1.Displays(l1)
list1.Adds(l1,a)
list1.Removes(l1,a)
list1.Searches(l1)
list1.Sorts(l1)
list1.Reverses(l1)
list1.total_elements(l1)
list1.total(l1,y)       
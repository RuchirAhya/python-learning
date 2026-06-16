fruits = {"apple", "banana", "mango", "orange"}
print("Access Set Items Print all elements of the set using a loop.")
print("For Loop :")
for x in fruits:
    print(x)
print("-"*30)
print("Add Set Items Add:grapes,kiwi to the set.")
fruits.add("grapes")
fruits.add("kiwi")
print(fruits)
print("-"*30)
fruits = {"apple", "banana", "mango", "orange"}
print("Remove Set ItemsRemove:banana,Then use another method to remove a random item.")
print("Remove Set ItemsRemove:banana")
fruits.remove("banana")
print(fruits)
print("-"*30)
print("Remove Set ItemsRemove:Then use another method to remove a random item.")
fruits.pop()
print(fruits)
print("-"*30)
fruits = {"apple", "banana", "mango", "orange"}
print("Loop Through Set Print all elements with numbering.")
y = 1
for x in fruits:
    print(y,"->",x)
    y += 1
print("-"*30) 
print("Join Sets Create:Perform:union(),update()")
more_fruits = {"kiwi", "watermelon", "banana"}
a = fruits.copy()
b = fruits.copy()
print("Join Sets Create:Perform:union()")
c = a.union(more_fruits)
print(c)
print("Orijnal Sets is",fruits)
print("-"*30)
print("Join Sets Create:Perform:update()")
b.update(more_fruits)
print(b)
print("Orijnal Sets is",fruits)
print("-"*30)
print("Orijnal Sets is",fruits)
print("-"*30)
print("Frozenset and Set Methods Create a frozenset from fruits.Then find:Length,Check whether apple exists,Difference between set and frozenset")
print("Frozenset and Set Methods Create a frozenset from fruits.")
g = frozenset(fruits)
print("Frozenset :",g)
print("-"*30)
print("find:Length",len(g))
print("-"*30)
print("find:Check whether apple exists")
y = 0
for x in g:
    if x == "apple":
        y == 1
        print("apple exists",x)
        break
if y == 0:
    print("apple not exists")
print("-"*30)
print("Difference between set and frozenset")
print("set is Daynemic")
print("frozenset is static")
print("-"*30)
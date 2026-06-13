numbers = [10, 5, 20, 15, 5, 30, 25, 20] 

print("#Print:First element,Last element,Third element")
print(numbers[0])
print(numbers[-1])
print(numbers[2])
print("-"*30)

print("#Print:Elements from index 2 to 5,Every second element")
print(numbers[2:6])
y = len(numbers)
[print(numbers[x]) for x in range(0,y,2)]
print("-"*30)

print("#Change the first element to 100.")
numbers[0] = 100
print(numbers)
print("-"*30)

print("#Replace elements from index 1 to 3 with:")
numbers[1:3] = [1, 2, 3]
print(numbers)
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Remove the first occurrence of ")
numbers.remove(5)
print(numbers)
print("-"*30)

print("#Remove:Element at index 3,Last element")
numbers.pop(3)
numbers.pop(-1)
print(numbers)
print("-"*30)

print("#Clear the entire list.")
numbers.clear()
print("Clear the entire list.")
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Add 40 at the end of the list.")
numbers.insert(8,40)
print(numbers)

print("#numbers.append(40)")
print(numbers[-1])
print("-"*30)

print("#Insert 99 at index 2.")
numbers.insert(2,99)
print(numbers)
print("-"*30)

print("#Add multiple elements:[50, 60, 70]")
a=[50, 60, 70]
numbers.extend(a)
print(numbers)
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Print all elements using a loop.")
x = 0
while x < len(numbers):
    print(numbers[x])
    x += 1
print("-"*30)    
x= 0
for y in range(len(numbers)):
    print(numbers[y])
print("-"*30)    

print("Print:,0 -> 10,1 -> 5,2 -> 20,(with index and value)")
while x < len(numbers):
    print(x,"->",numbers[x])
    x += 1
print("-"*30)    
for y in range(len(numbers)):
    print(y,"->",numbers[y])
print("-"*30)    

print("#Print only even numbers from the list.")
x=0
while x < len(numbers):
    print(numbers[x])
    x += 2
x=0
print("-"*30)
for y in range(len(numbers)):
    print(numbers[y])
    y += 2
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Create a new list containing only numbers greater than 15.")
y = 0
l1 = []
while y <= 10:
 y += 1  
 x = int(input("Enter Value:"))
 if x > 15:
     l1.insert(y,x)  
y = 0   
print(l1)
print("-"*30)
l1 = []
for y in range(0,10):
   c = int(input("Enter Value:"))
   if c > 15:
    l1.insert(y,c)
y = 0
print(l1)
print("-"*30)

print("#Create a new list containing squares of all elements.")
l1 = []
while y <= 10: 
 a = int(input("Enter Value:"))
 l1.insert(y,a**2)
 y += 1  
y = 0   
print(l1)
print("-"*30)
l1 = []
for y in range(0,10):
   b = int(input("Enter Value:"))
   l1.insert(y,b**2)
y = 0
print(l1)
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Task 16 Sort the list: Ascending,Descending,numbers.sort()")
print("Sort the list in Ascending",numbers)
print("-"*30)
numbers.sort(reverse=True)
print("Sort the list in Descending",numbers)
print("-"*30)
numbers = [10, 5, 20, 15, 5, 30, 25, 20]

print("#Create two copies:,Using .copy(),Using slicing [:]")
print("#Then modify the copy and verify the original list remains unchanged.")
a = numbers.copy()
a1 = numbers[:4]
print("copie Using .copy()",a)
for y in range(0,5):
    d = int(input("Enter value :"))
    a.append(d)
print(a)
print("-"*30)
print("Using slicing [:]",a1)
print("-"*30)
if a == numbers:
    print("Same value")
    print(numbers)
else:
    print("Not same")
    print("original list is",numbers)
print("-"*30)

print("#Join both lists using: + ,append(),extend()")
numbers = [10, 5, 20, 15, 5, 30, 25, 20]
extra = [100, 200, 300]
n1 = []
n2 = numbers.copy()
n1 = numbers + extra
print("Join both lists using: + ",n1)
print("-"*30)
for x in extra:
    n2.append(x)
print("Join both lists using: append()",n2)
print("-"*30)
numbers.extend(extra)
print("Join both lists using: extend()",numbers)
print("-"*30)

print("#Using list methods, find:Count of 5,Index of 30,Maximum value,Minimum value")
numbers = [10, 5, 20, 15, 5, 30, 25, 20]
print("Using list methods, find:Count of 5:",numbers.count(5))
print("-"*30)
print("Using list methods, find:Index of 30:",numbers.index(30))
print("-"*30)
print("Using list methods, find:Maximum value:",max(numbers))
print("-"*30)
print("Using list methods, find:Minimum value:",min(numbers))
print("-"*30)
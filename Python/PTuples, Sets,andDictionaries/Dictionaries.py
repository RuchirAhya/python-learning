student = {
    "id": 101,
    "name": "Ruchir",
    "age": 20,
    "course": "BCA"
}
print("Access Dictionary Items Print:name,age,course using:different access methods.")
print("Access Dictionary Items Print:name,age,course using:key name")
print(student["name"],student["age"],student["course"])
print("-"*30)
print("Access Dictionary Items Print:name,age,course using: get()")
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print("-"*30)
print("Access Dictionary Items Print:name,age,course using: keys()")
for x in student.keys():
 if x == "id":
  pass
 else:
  print(x)
print("-"*30)
print("Access Dictionary Items Print:name,age,course using: values()")
for x in student.values():
 if x == 101:
  pass
 else:
  print(x)
print("-"*30)
print("Access Dictionary Items Print:name,age,course using: items()")
for x in student.items():
 if x == ("id",101):
  pass
 else:
  print(x)
print("-"*30)
print("Change Dictionary Items Change:age → 21,course → MCA Print updated dictionary.")
print("change the value of a specific item by referring to its key name")
student["age"] = 21
student["course"] = "MCA"
for x in student.items():
 print(x)
print("-"*30)
print("using the update() method") 
student.update({"age": 21})
student.update({"course": "MCA"})
for x in student.items():
 print(x)
print("-"*30)
print("Add Dictionary Items Add: city: Rajkot,percentage: 85")
print("using a new index key and assigning a value")
student["city"] = "Rajkot"
student["percentage"] = 85
for x in student.items():
 print(x)
print("-"*30)
student = {
    "id": 101,
    "name": "Ruchir",
    "age": 21,
    "course": "MCA"
}
print("using the update() method") 
student.update({"city": "Rajkot"})
student.update({"percentage": 85})
for x in student:
 print(x,"->",student[x])
print("-"*30)
print("Remove Dictionary Items Remove:percentage using pop(),city using del,last inserted item using popitem()")
print("Remove Dictionary Items Remove:percentage using pop()")
student.pop("percentage")
for x in student:
 print(x,"->",student[x])
print("-"*30)
print("Remove Dictionary Items Remove:city using del")
del student["city"]
for x in student:
 print(x,"->",student[x])
print("-"*30)
print("Remove Dictionary Items Remove:last inserted item using popitem()")
student.popitem()
for x in student:
 print(x,"->",student[x])
print("-"*30)
student = {
    "id": 101,
    "name": "Ruchir",
    "age": 21,
    "course": "MCA"
}
print("oop Through Dictionary Print:id -> 101,name -> Ruchir,age -> 21,course -> MCA Also print:all keys,all values")
print("oop Through Dictionary Print:id -> 101,name -> Ruchir,age -> 21,course -> MCA")
for x in student:
 print(x,"->",student[x])
print("-"*30)
print("print:all keys")
for x in student.keys():
 print(x)
print("-"*30) 
print("print:all values")
for x in student.values():
 print(x)
print("-"*30) 
print("Copy and Nested Dictionary")
a = student.copy()
print(a)
print("-"*30)
students = {
    "student1": student,
    "student2": {
        "id": 102,
        "name": "Amit",
        "age": 21
    }
}
print("Access:student1 name,student2 age")
print(students["student1"]["name"])
print(students["student2"]["age"])
print("-"*30)
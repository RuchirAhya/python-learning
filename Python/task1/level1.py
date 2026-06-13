employee_data = {
    "name": "Amit",
    "age": 28,
    "city": "Rajkot",
    "salary": 45000,
    "department": "IT",
    "experience": 4,
    "is_active": True,
    "email": "amit123@gmail.com",
    "rating": 4.5,
    "projects": 7
}


if "salary" in employee_data:
    print("salary exists")
print("---------")
print(employee_data["city"])
print("---------")
for x in employee_data.keys():
        print(x)
print("---------")
for x in employee_data.values():
    print(x)
print("---------")
for x in employee_data.items():
     print(x)   
print("---------")
print("Keys total is",len(employee_data.values()))
print("---------")
employee_data.update({"country": "India"})
print("---------")



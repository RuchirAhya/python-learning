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
for x in employee_data.values():
   if type(x) == int or type(x) == float:
        print(x)
   
   
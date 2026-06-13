employee_skills = {
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript"
}
for x in employee_skills:
    if x == "Django":
        print("Django Skill Found")
    else:
        print("Django Skill Not Found")
        break
print("----------------")
if "Django" in employee_skills:
    print("Django Skill Found")
else:
    print("Django Skill Not Found")
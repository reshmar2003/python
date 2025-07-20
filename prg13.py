employee={
    "name":"John Smith",
    "age":39,
    "Salary":"$10000",
    "Desgication":"Manager"
}

print(employee['name'],employee['age'])

for i in employee:
    print(i)
    
for i in employee.values():
    print(i)
    
for key in employee:
    print(key+ ":"+str(employee[key]))
import models
emp = ["emp1","emp2","emp3","emp4","emp5"]
Objects = []
for i in range(0,len(emp)):
    print(f"Employee details {i+1} ")
    employee_id = int(input("Enter empoye id"))
    name =  input("Enter employee name: ")
    salary =  int(input("Enter salary: "))
    department = input("Enter department: ")

    emp[i] = models.Employee(employee_id,name,salary,department)
    Objects.append(emp[i])

print("-"*80)

print("All Employee Details ")
for i in range(0,len(emp)):
    emp[i].display()

print("-"*50)
print()

print("Employee with salary Greater then 40000")
for i in range(0,len(emp)):
    if emp[i].salary >= 40000:
        emp[i].display()

print()
print("-"*50)
for i in range(0,len(emp)):
    if emp[i].department == "IT":
        emp[i].display()
print()
print("-"*50)

print("Highest salary employee")
hig = emp[0].salary
ind = 0
for i in range(0,len(emp)):
    if emp[i].salary > hig:
        hig = emp[i].salary
        ind = i
emp[ind].display()

print()
print("-"*50)
print("Total salary: ")
sum = 0
for i in range(0,len(emp)):
    sum = sum + emp[i].salary
print(sum)

print()
print("-"*50)
avg = sum/len(emp)    
print(avg)
        


class Employee:
    def __init__(self,emp_id,emp_name,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.__salary=salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        if value<=0:
            raise ValueError("Salary must be grateer than 0")
        self.salary=value
     
    @salary.deleter
    def salary(self):
        del self.__salary
    
    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Salary: {self.salary}")
        
class Developer(Employee):
    def __init__(self, emp_id, emp_name, salary,program_lang):
        super().__init__(emp_id, emp_name, salary)
        self.program_lang=program_lang
        
    def display_details(self):
        super().display_details()
        print("Role: Developer")
        print(f"Programming language: {self.program_lang}")
        
    def write_code(self):
        print(
            f"{self.emp_name} is developing applications "
            f"using {self.program_lang}")
    
class Manager(Employee):
    def __init__(self, emp_id, emp_name, salary,team_size):
        super().__init__(emp_id, emp_name, salary)
        self.team_size=team_size
        
    def display_details(self):
        super().display_details()
        print("Role: Manager")
        print(f"Team Size: {self.team_size}")
    
    def manage_team(self):
        print(
            f"{self.emp_name} is managing a team of "
            f"{self.team_size} members."
        )
        
emp_id=input("Enter Employee ID: ")
emp_name=input("Enter Employee Name: ")
salary=float(input("Enter Salary: "))

print("\nEnter Employee Type: ")
print("1. Developer")
print("2. Manager")

emp_type=int(input("Enter choice: "))

if emp_type==1:
    program_lang=input("Enter Programing Language: ")
    emp=Developer(emp_id,emp_name,salary,program_lang)
elif emp_type==2:
    team_size=int(input("Enter Team Size: "))
    emp=Manager(emp_id,emp_name,salary,team_size)
else:
    print("Invalid Employee Type.")
    exit()
    
print("\n Employee Details\n")

emp.display_details()

print()
if emp_type==1:
    emp.write_code()
elif emp_type==2:
    emp.manage_team()


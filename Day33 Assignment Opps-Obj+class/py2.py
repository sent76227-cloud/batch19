'''Assignment 2: Employee Salary Calculator'''

class Employee:
    def attribute(self, employee_id, name, basic_salary, hra_percentage, da_percentage):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.hra_percentage = hra_percentage
        self.da_percentage = da_percentage

    def calculate_hra(self):
        self.hra = self.basic_salary * self.hra_percentage / 100

    def calculate_da(self):
        self.da = self.basic_salary * self.da_percentage / 100

    def calculate_gross_salary(self):
        self.gross_salary = self.basic_salary + self.hra + self.da

    def display_salary(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("Gross Salary:", self.gross_salary)


employee = Employee()
employee.attribute(int(input("Enter employee ID: ")), input("Enter employee name: "),
                   float(input("Enter basic salary: ")),
                   float(input("Enter HRA percentage: ")),
                   float(input("Enter DA percentage: ")))
employee.calculate_hra()
employee.calculate_da()
employee.calculate_gross_salary()
employee.display_salary()

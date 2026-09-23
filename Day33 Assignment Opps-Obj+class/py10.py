'''Assignment 10: Personal Expense Calculator'''

class ExpenseTracker:
    def attribute(self, person_name, monthly_salary, rent, food_expenses,
                  travel_expenses, other_expenses):
        self.person_name = person_name
        self.monthly_salary = monthly_salary
        self.rent = rent
        self.food_expenses = food_expenses
        self.travel_expenses = travel_expenses
        self.other_expenses = other_expenses

    def calculate_total_expenses(self):
        self.total_expenses = (self.rent + self.food_expenses +
                               self.travel_expenses + self.other_expenses)

    def calculate_savings(self):
        self.savings = self.monthly_salary - self.total_expenses

    def display_expense_report(self):
        print("Person Name:", self.person_name)
        print("Monthly Salary:", self.monthly_salary)
        print("Total Expenses:", self.total_expenses)
        print("Savings:", self.savings)


tracker = ExpenseTracker()
tracker.attribute(input("Enter person name: "), float(input("Enter monthly salary: ")),
                  float(input("Enter rent: ")), float(input("Enter food expenses: ")),
                  float(input("Enter travel expenses: ")), float(input("Enter other expenses: ")))
tracker.calculate_total_expenses()
tracker.calculate_savings()
tracker.display_expense_report()

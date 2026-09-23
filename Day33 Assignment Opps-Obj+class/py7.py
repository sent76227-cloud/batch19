'''Assignment 7: Mobile Phone Data Usage'''

class MobilePlan:
    def attribute(self, customer_name, mobile_number, total_data, used_data, validity_days):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.total_data = total_data
        self.used_data = used_data
        self.validity_days = validity_days

    def calculate_remaining_data(self):
        self.remaining_data = self.total_data - self.used_data

    def calculate_usage_percentage(self):
        self.usage_percentage = (self.used_data / self.total_data) * 100

    def display_plan(self):
        print("Customer Name:", self.customer_name)
        print("Mobile Number:", self.mobile_number)
        print("Validity:", self.validity_days, "days")
        print("Remaining Data:", self.remaining_data, "GB")
        print("Usage Percentage:", self.usage_percentage, "%")


plan = MobilePlan()
plan.attribute(input("Enter customer name: "), input("Enter mobile number: "),
               float(input("Enter total data in GB: ")), float(input("Enter used data in GB: ")),
               int(input("Enter validity in days: ")))
plan.calculate_remaining_data()
plan.calculate_usage_percentage()
plan.display_plan()

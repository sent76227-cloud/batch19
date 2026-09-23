'''Assignment 4: Rectangle Calculator'''

class Rectangle:
    def attribute(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        self.area = self.length * self.breadth

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.breadth)

    def display_result(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area)
        print("Perimeter:", self.perimeter)


rectangle = Rectangle()
rectangle.attribute(float(input("Enter length: ")), float(input("Enter breadth: ")))
rectangle.calculate_area()
rectangle.calculate_perimeter()
rectangle.display_result()

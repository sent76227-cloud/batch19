'''2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.
'''

def perfectnumber(number):
    sum = 0

    for i in range(1, number):
        if number % i == 0:
            sum = sum + i

    if sum == number:
        return True
    else:
        return False


def primenumber(number):
    if number <= 1:
        return "Not a Prime Number"

    for i in range(2, number):
        if number % i == 0:
            return "Not a Prime Number"

    return "Prime Number"


def reverse(number):
    rev = 0

    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10

    return rev


def factorial(number):
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact


def factors(number):
    result = []

    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)

    return result


while True:
    print("******** NUMBER ANALYSIS SYSTEM ********")
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            number = int(input("Enter number: "))

            if perfectnumber(number):
                print(number, "is a Perfect Number")
            else:
                print(number, "is not a Perfect Number")

        case 2:
            number = int(input("Enter number: "))

            result = primenumber(number)
            print(result)

        case 3:
            number = int(input("Enter number: "))

            result = reverse(number)
            print("Reverse Number :", result)

        case 4:
            number = int(input("Enter number: "))

            result = factorial(number)
            print("Factorial :", result)

        case 5:
            number = int(input("Enter number: "))

            result = factors(number)
            print("Factors :", result)

        case 6:
            print("Thank You. Program Terminated.")
            break

        case _:
            print("You entered a wrong choice.")


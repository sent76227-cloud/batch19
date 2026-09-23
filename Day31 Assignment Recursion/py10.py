'''6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number'''

def isprime(x, num):
    if x == num:
        return True
    if num % x == 0:
        return False
    return isprime(x + 1, num)

value = int(input("Enter Coupon Number: "))
result = isprime(2, value)

if result:
    print("Prime Number")
else:
    print("Not Prime Number")
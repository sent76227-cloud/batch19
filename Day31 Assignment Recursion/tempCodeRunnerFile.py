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

def isprime(x,num):
    if num%x==0:
        return 0
    else :
        return -1 + isprime(x+1,num)

value =  int(input("Enter value: "))
result  = isprime(2,value)

if result == 0 or result == -1:
    print("notPrime number ")
else:
    print("prime")
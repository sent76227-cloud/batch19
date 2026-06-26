'''
Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
'''
pri =  int(input("Enter principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter time: "))
ci = pri * (1+rate/100) ** time

print(f"Amount after interest = {ci}")
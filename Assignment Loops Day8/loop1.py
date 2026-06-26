''' 1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9 '''



num = int(input("Enter a number: "))
check = 0
max = 0 
leng = len(str(num))
for i in range(0,leng)
   check = num%10
   if check > max:
       max = check
   num = num//10
print(max)


'''
while num > 0 :
   check = num%10
   if check > max:
       max = check
   num = num//10

print(max )'''
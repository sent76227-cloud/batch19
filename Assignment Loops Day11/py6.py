'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2 '''


num = int(input("Enter a num: "))
length = len(str(num))



for i in range(2,num):
   if num%i == 0 :
     print("Composite")
     break
else:
   print("Not composite")
 

fac = 0
for i in range(1,num+1):
    if num%i==0:
       sml = i
       fac = fac+1
print("Factors Count",fac)



for i in range(2,num+1):
    if num%i==0:
       sml = i
       break
print("Smallest Factor",sml)











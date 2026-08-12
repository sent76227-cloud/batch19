''' 3. Perfect Number Reward System


A gaming company rewards users if entered number is a Perfect Number.


(Perfect Number = sum of proper factors equals number)


Write a program using for-else loop to:


- Find sum of proper factors

- If sum equals number print Reward Unlocked

- Else print Try Again


Input:

6


Output:

Reward Unlocked '''





num = int(input("Enter a number"))
sum = 0
temp = num

for i in range(1,num):
   if num%i==0:
       sum = sum+i
if temp == sum:
   print("Reward unlock")
else:
   print("Try Again")












'''
num = int(input("Enter a num"))
length = len(str(num))



temp = num
rev = 0
sum = 0
for i in range(1,length+1):
   dig = num%10
   rev = rev*10+dig
   sum = sum+dig
   num = num//10
abstdiff = abs(rev-temp)
finl = abstdiff + sum
print("Sum of digit",sum)
print("Reverse = ",rev)
print("Difference",abstdiff)
print("Final Result = ",finl)




for i in range(2,finl):
   if finl%i == 0:
       print("Not prime")
       break
else:
   print("Prime") '''
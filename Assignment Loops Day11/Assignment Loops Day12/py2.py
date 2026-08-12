

''' 2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime '''

num = int(input("Enter a num"))
length = len(str(num))

pro = 1
sum = 0
for i in range(1,length+1):
   dig = num%10
   pro = int(pro*dig)
   sum = sum+dig
   num = num//10.
 
diff = abs(pro - sum)
diff = int(diff)
diff_count = len(str(diff))
finl = int(diff_count + diff)
print("sum",sum)
print("Product",pro)
print("Difference = ",diff)
print("Digits = ",diff_count)
print("Final Result ",finl)

for i in range(2,finl):
   if finl%i == 0:
       print("Not prime")
       break
else:
   print("Prime")
























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
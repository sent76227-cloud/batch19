''' 1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime ''' 




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
   print("Prime")
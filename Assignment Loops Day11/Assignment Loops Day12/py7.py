'''
7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime
'''
n=int(input("Enter number: "))
sum=0
i=2
while n>0:
  digit=n%10
  n=n//10
  if i%2==0:
    sum+=digit
  i+=1
print("Alternate Sum: ",sum)
for i in range(2,sum//2+1):
   if sum%i==0:
      print("Not Prime")
      break
else:
   print("Prime")

              
       
           
   
 
 
   

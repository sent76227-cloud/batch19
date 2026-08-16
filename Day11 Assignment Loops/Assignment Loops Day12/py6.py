'''
6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29
'''
n=int(input("Enter number: "))
temp=n
isPrime=True
while isPrime:
   temp=temp+1
   i=2
   while i<=5:
      if temp%i==0:
         break
      i+=1
   else:
       isPrime=False
       next=temp
print("Next Prime Cabin: ",next)
      
       
           
   
 
 
   

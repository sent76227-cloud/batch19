'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3 ''' 

num = int(input("Enter a number"))
temp = num
status = True

while status:
   num = num+1
   for i in range(2,num):
       temp2 = num
       if num%i==0:
           break
   else:
        print("Next Prime ID = ",temp2)
        status = False
diff = abs(temp - temp2)
print("Gap ", diff)
        
      

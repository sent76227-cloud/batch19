"""

    1
   22
  333
 4444
55555








"""
num = int(input("Enter n: "))
a = num

i = 1
while i<=num:
         j = a
         while 1<=j:
            print(" ",end="")
            j = j-1
         k = 1
         while k<=i:
             print(i,end="")
             k = k+1
         i = i+1
         a = a-1
         print()
          
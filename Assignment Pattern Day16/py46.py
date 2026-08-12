"""

    A
   AB
  ABC
 ABCD
ABCDE










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
         b = 65
         while k<=i:
             print(chr(b),end="")
             b = b+1
             k = k+1
         i = i+1
         a = a-1
         print()
          
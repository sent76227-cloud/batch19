'''
654321
 65432
  6543
   654
    65
 '''

num = int(input("Enter num"))

i = 1
temp = num
while i<num:
     j = 1
     while j<=i-1:
        print(" ",end="")
        j = j+1
     k = num
     while i<=k:
         print(k,end="")
         k = k-1
     print()
     i = i+1
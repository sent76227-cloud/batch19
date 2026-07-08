'''
    *
   **
  ***
 ****
***** '''

num = int(input("Enter num"))

i = 1
temp = num
while i<=num:
     j = 1
     while j<temp:
        print(" ",end="")
        j = j+1
     k = 1
     while k<=i:
        print("*",end="")
        k = k+1
     print()
      
     temp = temp-1
     i = i+1
'''
    1
   10
  101
 1011
10101 '''

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
        if k%2==0:
            print("0",end="")
        else:
            print("1",end="")
        
        k = k+1
     print()
      
     temp = temp-1
     i = i+1
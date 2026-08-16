"""
    1
   10
  101
 1010
10101



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
             if k == 1:
               print("1",end="")
             elif k%2==0:
               print("0",end="")                  
             k = k+1
             
         i = i+1
         a = a-1
         print()
          
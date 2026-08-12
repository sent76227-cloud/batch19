"""
    1
   11
  1*1
 1**1
11111


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
         b = 1
         while k<=i:
             if k == 1:
                print(b,end="")
             elif i== k:
                print(b,end="")
             elif i == num:
                print(b,end="")
             else:
                print("*",end="")
             k = k+1
         i = i+1
         a = a-1
         print()
          
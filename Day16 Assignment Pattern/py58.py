"""
    1
   12
  123
 1234
12345



"""
num = int(input("Enter n: "))



i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       a = 1
       while 1<=k:
            print(a,end="")
            a = a+1
            k = k-1
       i = i+1
       print()
      
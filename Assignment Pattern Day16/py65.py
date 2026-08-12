"""
    1|
   1 |1
  1 2| 1
 1 3 |3 1
1 4 6| 4 1
"""
num = int(input("Enter n: "))
a = 0
i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = 1
       val = 1
       
       while k<=i:
           print(f"{val} ",end="")
           val = val*(i-k)//k
           k = k+1
       i = i+1
       print()
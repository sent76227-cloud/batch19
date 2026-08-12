"""
    X 
   X X 
   X__X
  X____X
X X X X X
  






"""
num = int(input("Enter n: "))



i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       while 1<=k:
          if k == 1:
              print("x",end="")
          elif  i==k:
               print("x",end="")
          elif i==num:
              print("x",end="")
          else:
             print("_",end="")
          k = k-1
       i = i+1
       print()
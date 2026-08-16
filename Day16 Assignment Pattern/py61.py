"""
    *
   ***
  *****
 *******
*********


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
          print("*",end="")
          k= k-1
       l = i-1
       while 1<=l:
            print("*",end="")
            l = l-1
       i = i+1
       print()
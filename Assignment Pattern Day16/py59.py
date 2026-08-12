"""
     A
    AB
   ABC
 ABCD
ABCDE  






"""
num = int(input("Enter n: "))



i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       a = 65
       while 1<=k:
            print(chr(a),end="")
            a = a+1
            k = k-1
       i = i+1
       print()
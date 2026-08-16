"""
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI
"""
num = int(input("Enter n: "))



i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       a =65
       while 1<=k:
          print(chr(a),end="")
          k= k-1
          a = a+1
       l = i-1
       while 1<=l:
            
            print(chr(a),end="")
            l = l-1
            a = a+1
            
       i = i+1
       print()
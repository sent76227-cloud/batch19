"""

A
BCD
EFGHI
JKLMNOP






"""
num = int(input("Enter n: "))
a = 65

i = 1
while i<=num:
        
        j = i*2-1
        while 1<=j:
           print(chr(a),end="")
           a = a+1
           j = j-1
 
        i=i+1
        
        print()
          
"""


EEEEE
DDDD
CCC
BB
A




"""
num = int(input("Enter n: "))
a = 65+num-1

for i in range(0,num):
   
     
     
     for j in range(num-i,0,-1):
          print(chr(a),end="")
     a = a-1
     print()
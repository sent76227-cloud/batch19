"""

ABCDE
A  D
A C
AB
A




"""
num = int(input("Enter n: "))
a = 65+num-1


i = 5
while 1<=i:
      j = i
      a = 65
      while 1<=j:
          if i == num:
             print(chr(a),end="")
      
          elif i == j:
             print(chr(a),end="") 
          elif j == 1:
             print(chr(a),end="")

          else:
              print(" ",end="")
          a = a+1
          j = j-1
          
      print()
      i = i-1
"""
ABCDE
 ABCD
  ABC
   AB
    A



"""
num = int(input("Enter n: "))



i = num
while 1<=i:
        j = num-i
        while 0<j:
          print(" ",end="")
          j = j-1
        k = 1
        a = 65
        while k<=i:
              print(chr(a),end="")
        
              a = a+1
              k = k+1
              
              
        i = i-1
        
        print()
      
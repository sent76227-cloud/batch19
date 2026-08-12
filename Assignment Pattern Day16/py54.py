"""
ABCDE
 A__D
  A_C
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
              if i == num:
                print(chr(a),end="") 
              elif k == 1:
                print(chr(a),end="")
              elif k == i:
                print(chr(a),end="")
              else:
                print(" ",end="")

        
              a = a+1
              k = k+1
              
              
        i = i-1
        
        print()
      
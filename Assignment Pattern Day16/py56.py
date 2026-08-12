"""
11111
 2222
  333
   44
    5




"""
num = int(input("Enter n: "))



i = num
a = 1
while 1<=i:
        
        j = num-i
        while 0<j:
          print(" ",end="")
          j = j-1
        k = 1
        
        while k<=i:
              print(a,end="")
        
              
              k = k+1
              
        a = a+1     
        i = i-1
        
        print()
      
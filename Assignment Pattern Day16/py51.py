"""
55555
 4444
  333
   22
    1




"""
num = int(input("Enter n: "))
a = num


i = 1
while i<=num:
        j = i-1
        while 0<j:
          print(" ",end="")
          j = j-1
        k = num-i
        
        while 0<=k:
              print(a,end="")
              k = k-1
              
        i = i+1
        a = a-1
        print()
      
"""
*
**
****
*******
***********






"""
num = int(input("Enter n: "))

i = 1
a = 0
b = 3
while i<=num:
        y = i+a
        j = y
        while 0<j:
           print("*",end="")
           j = j-1
         
        if i == 3:
           a =1
        elif i == 4:
           a  = 3
        elif i == 5:
           a = 6
        

        
        i=i+1
        
        print()
          
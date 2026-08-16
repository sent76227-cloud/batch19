"""


*****
*  *
* *
**
*


"""
num = int(input("Enter n: "))
a = 65+num-1


i = 5
while 1<=i:
      j = i
      while 1<=j:
          if i == num:
             print("*",end="")
      
          elif i == j:
             print("*",end="") 
          elif j == 1:
             print("*",end="")

          else:
              print(" ",end="")
          j = j-1
          
      print()
      i = i-1
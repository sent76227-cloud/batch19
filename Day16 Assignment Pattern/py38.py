"""

55555
4  4
3 3
22
1




"""
num = int(input("Enter n: "))
a = 65+num-1


i = 5
while 1<=i:
      j = i
      
      while 1<=j:
          if i == num:
             print(i,end="")
          elif i == j:
            print(i,end="")
          elif j == 1:
            print(i,end="")
          else:
            print(" ",end="")
          j = j-1
          
          
      print()
      i = i-1
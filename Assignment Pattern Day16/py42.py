"""

123456
54321
1234
321
12
1





"""
num = int(input("Enter n: "))
a = 65+num-1

a = 1
i = 5
while 1<=i:
      j = i
      
      while 1<=j:
          if i == num:
             print(a,end="")
          elif i == j:
            print(a,end="")
          elif j == 1:
            print(a,end="")
          else:
            print(" ",end="")
          a = 2
          j = j-1
          
          
      print()
      i = i-1
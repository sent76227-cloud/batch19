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

a = num
i = 1
while i<=num:
      j = a
      x = 1
      
      while 1<=j:
          if i%2 ==0:
            print(j,end="")
          else:
             print(x,end="") 
          x = x+1
          j = j-1 

      a = a-1         
          
      print()
      i = i+1
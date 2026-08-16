"""
    1
   123
  12345
 1234567
123456789



"""
num = int(input("Enter n: "))



i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       a =1
       while 1<=k:
          print(a,end="")
          k= k-1
          a = a+1
       l = i-1
       while 1<=l:
            
            print(a,end="")
            l = l-1
            a = a+1
            
       i = i+1
       print()
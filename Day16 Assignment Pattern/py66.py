"""
    1
   1*1
  1***1
 1*****1
111111111



"""
num = int(input("Enter n: "))
a = 1
i = 1
while i<=num:
       j = num-i
       while 1<=j:
              print(" ",end="")
              j = j-1
       k = i
       
       while 1<=k:
          if k == i:
             print(a,end="")
          elif i == num:
             print(a,end="")
          else:
             print("*",end="")
          k= k-1
          
       l = i-1
       while 1<=l:
            if l ==1:
               print(a,end="")
            elif i == num:
              print(a,end="")
            else:
               print("*",end="")
            
            l = l-1
                        
       i = i+1
       print()
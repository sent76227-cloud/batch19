"""
55555
4__4
3_3
22
1

"""
num = int(input("Enter n: "))



i = num
while 1<=i:
        j = num-i
        while 0<j:
          print(" ",end="")
          j = j-1
        k = 1
        a = 1
        while k<=i:
              if i == num:
                print(i,end="") 
              elif k == 1:
                print(i,end="")
              elif k == i:
                print(i,end="")
              else:
                print(" ",end="")

        
              a = a+1
              k = k+1
              
              
        i = i-1
        
        print()
      
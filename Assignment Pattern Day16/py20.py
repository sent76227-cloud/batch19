"""
1
12
1 3
1  4
12345

"""
num = int(input("Enter n: "))


for i in range(1,num+1):
        
     for j in range(1,i+1):
        if j == 1:
           print("1",end="")
        elif j==i:
           print(j,end="")
        elif i == num:
           print(j,end="")
        else:
           print(" ",end="")
         
         
          
        

     print()
   
    
          
   
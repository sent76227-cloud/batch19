"""
1
22
3 3
4  4
55555


"""
num = int(input("Enter n: "))


for i in range(1,num+1):
        
     for j in range(1,i+1):
        if i == j:
           print(i,end="")
        elif j == 1:
           print(i,end="")
        elif i == num:
           print(i,end="")
        else:
           print(" ",end="")
        
         
         
          
        

     print()
   
    
          
   
"""
*
**
*@*
*@@*
* * * * *
"""
num = int(input("Enter n: "))


for i in range(1,num+1):
        
     for j in range(1,i+1):
        if i == j: 
           print("*",end="")
        elif j == 1:
           print("*",end="")
        elif i == num:
           print("*",end="")
        else:
           print("@",end="")
        
         
         
          
        

     print()
   
    
          
   
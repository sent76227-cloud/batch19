"""
*
** 
* *
*  *
*   *
*    *
*     *
* * * * *
"""
num = int(input("Enter n: "))

print("*")
for i in range(1,num+1):   
     a = 1
     print("*",end="")
     for j in range(1,i+1):
        
        print(" ",end="")
        
        a = 1+a
     print("*",end="")
     print()
num = num +1
print("*"*num)
   
    
          
   
"""
a
bc
d f
g  j
klmno




"""
num = int(input("Enter n: "))

a = 97
for i in range(1,num+1):
        
     for j in range(1,i+1):
        if i == j: 
           print(chr(a),end="")
        elif j == 1:
           print(chr(a),end="")
        elif i == num:
           print(chr(a),end="")
        else:
           print(" ",end="")
        a = a+1
         
         
          
        

     print()
   
    
          
   
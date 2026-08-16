"""
A
AB
A C
A  D
ABCDE



"""
num = int(input("Enter n: "))


for i in range(1,num+1):
     a = 65   
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
   
    
          
   
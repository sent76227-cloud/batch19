""" 
1
01
101
0101
10101
"""
num = int(input("Enter n: "))


for i in range(1,6):
     if i%2==0:
        a = 0
     else: 
        a = 1   
     for j in range(1,i+1):
        print(a,end="")
        if a == 0:
             a = 1
        else:
            a = 0
        
        

   
        
     print()
   
    
          
   
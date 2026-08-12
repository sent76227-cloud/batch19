"""
1
10
1 1
1  0
10101



"""
num = int(input("Enter n: "))


for i in range(1,num+1):
     a = 1
     for j in range(1,i+1):
         
         if j == 1:
              print(a,end="")
         elif i==j and j%2==0:
            a = 0
            print(a,end="")
         
         elif i%2!=0 and j%2==0 and i != num:
             print(a,end="")
         elif i == num:
            if j%2==0:
              a = 0 
              print(a,end="")
            else:
               print(a,end="")
            
         else:
            print(" ",end="")
         a = 1
         
         
         
         
             
         
         
    
       
           
     print()
   
    
          
   
'''WAP to find a leap year betwen two year'''

a = int(input("Enter number a "))
b = int(input("Enter number b "))
leapcount = 0
norcount = 0

for n in range(a,b+1):
   if n%100==0 and n%4==0 and n%100==0:
          print(n," leap year")
          leapcount = leapcount+1
   else:
       if n%4==0:
        print(n," leap year ")
        leapcount = leapcount+1




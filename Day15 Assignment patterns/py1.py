'''WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''



a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
cout = 0
sum = 0
s = 0

for n in range(a,b+1):
    cout = n+1
    if cout%9==0:
        sum = sum+1
        s = cout+s
        print(cout,end=" ")
print()
print("Count is = ",sum)
print("Sum of all number which is divisible by 9 is =  ",s)
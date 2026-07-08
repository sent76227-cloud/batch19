'''WAP to print sqaure, cube and square root of all numbers from 1 to N '''


a = int(input("Enter a num"))
b = int(input("Enter b num"))

for n in range(a,b+1):

    temp = n
    squ = temp*temp
    cub = squ*temp
    squroot = n**0.5
    print("---Start hear---->")
    print(f"Square  of {temp} = {squ} ")
    print(f"Cube root of{temp} = {cub} ")
    print(f"Square root of{temp} = {squroot} ")
    print("-------------------------------")
    


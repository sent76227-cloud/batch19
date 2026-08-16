'''
0
01
012
0123
01234

 '''

num = int(input("Enter num"))

i = 0
while i<num:
    j = 0
    while j<=i:
         print(j,end="")
         j=j+1
    print()
    i = i+1
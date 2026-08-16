'''
1
00
111
0000
11111'''

num = int(input("Enter num"))




i = 1
while i<=num:
    j = i
    while j>0:
        if i%2==0:
           print("0",end="")
        else:
           print("1",end="")
        j = j-1
    print()
    i = i+1
    
    
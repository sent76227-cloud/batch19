''' 
a
ab
abc
abcd
abcde
'''



n = int(input("Enter a : "))


i = 1
while i<=n:
     j = 1
     a = "A"
     while j<=i:
         print(a,end="")
         a =  chr(ord(a.strip()) + 1)
         j = j+1
     print()
     i = i+1
    
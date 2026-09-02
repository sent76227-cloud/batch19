s = input("Enter sting: ")
for i in range(len(s)):
    check =  s[:len(s)-i-1]
    
    if s.startswith(check) and s.endswith(check):
       break
midd = s[len(check):len(s)-len(check)]
print(check)
print(midd)
if check  in midd:
    print(midd)
    
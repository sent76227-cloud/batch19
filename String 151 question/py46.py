'''46Check if a substring appears at both the start and end.'''
#S = "abcabca", Sub="abca" TRUE
s = input("Enter sting: ")
sub = input("Enter sting: ")
temp = False
new = ""
for i in range(len(sub)) :
    for j in range(len(sub)):
        if s[i] == sub[j] :
            new = new +s[i]
            break
    if new == sub:
        break
backnew = ""

if new == sub:
    
    for i in range(-1,-len(sub)-1,-1):
        
        for j in range(-1,-len(sub)-1,-1):
            if s[i] == sub[j]:
                backnew =  s[i]+backnew
                break
else:
    print("New and s is not same")
if backnew == new and sub == backnew and new == sub:
    print(True)
else:
    print(False)
    
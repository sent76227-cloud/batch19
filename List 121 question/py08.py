'''If duplicate element'''
nums = list(map(int,input("Ener list").split()))
for i in range(len(nums)):
    x = 0
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            x = 1
            break
    if x == 1:
        break
if x == 1:
    print(True)
else:
    print(False)
        


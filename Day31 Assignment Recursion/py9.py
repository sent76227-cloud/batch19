'''5.
Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found'''
def patientid(target,digit):
    if digit == 0:
        return 0
    last = digit%10
    if last == target:
        return 1
    else:
        return 0+patientid(target,digit//10)


result = patientid(2,785362156)
if result == 1:
    print("Found")
else:
    print("Not found")
    
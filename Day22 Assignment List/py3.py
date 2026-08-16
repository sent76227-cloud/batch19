'''
3. Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 9125
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0 '''
a = list(map(int,input("enter list: ").split()))

length = len(a)
new = []
peakvalue = -1
for i in range(len(a)):
    if i == 0:
        if len(a) == 1:
            new.append(a[i])
            break
        if len(a) == 1:
            new.append(a[i])
            break
        elif a[i+1] < a[i]:
            new.append(a[i])
    elif i == length-1:
        if a[i-1] < a[i]:
            new.append(a[i])
    else:
        if a[i+1] < a[i] and a[i-1] < a[i]:
            new.append(a[i])
print("Peak value list is: ",new)
sum = 0
avgsum = 0
diff = 0
for i in new:
    squ = i**2
    sum = sum+squ
    avgsum = avgsum +i
if 1 < len(new):
    print("check")
    for i in range(len(new)):
        diff =  new[i+1]-new[i]
        if len(new) == 2:
            break
print("Sum of squre: ",sum)
print("Average is: ",avgsum//len(new))
print("Diffence is: ",diff)
'''1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.

Test Case 2

Input:
elevation = [800, 900, 950, 1000]

Output:
3

Explanation:
Last element can also be a peak because it has no right neighbor.

Test Case 3

Input:
elevation = [3000]

Output:
0

Explanation:
Single element is always a peak.
'''
a = list(map(int,input("Enter list: ").split()))
length = len(a)
peakindex = -1
if 1 < length:
 for i in range(len(a)):
    if i == 0:
        if a[i+1] < a[i] :
            peakindex = i
            break
    elif i == length-1:
        if a[i-1] < a[i]:
            peakindex = i
            break
    else:
        if a[i-1] < a[i] and a[i+1] < a[i] :
            peakindex = i
            break
        
 if peakindex != -1:
    print("Peak Index is ", peakindex)

else:
    print("Peak Index is 0")

        
            
'''WAP to find peak element index and peak element'''

size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    arr.append(int(input("Enter elemt in list: ")))
print(arr)
peakindex = -1
for i in range(arr):
    if i == 0:
        if arr[i] 
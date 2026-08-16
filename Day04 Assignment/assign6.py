'''
Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
'''
data = int(input("Data = "))
mb = float(data*1024)
kb = float(mb * 1024)
print(f"In MB = {mb}\nIn KB = {kb}")
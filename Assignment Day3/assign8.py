'''
 Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
'''
print("Accepts values in MB")
print("Converts into GB")
mb = int(input("Enter input: "))
gb = mb/1024
print(f"GB = {gb}")

'''
Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''
print("Convert total seconds into hours, minutes, and seconds.")
sec = int(input("Enter Seconds: "))
hours = int(sec//3600)
min = int(sec%3600/60)
second = int(sec%60)
print(f"Hours = {hours}\nMinutes = {min}\nSeconds = {second}")
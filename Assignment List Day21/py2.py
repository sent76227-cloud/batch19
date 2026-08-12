'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = [] '''

a = list(map(int,input("Enter salary: ").split()))
length = len(a)
sum = 0
news = []
for i in a:
    sum = sum+i
    if 15000 < i:
        news.append(i)
above = 0
avg = sum//length
for i in a:
    if avg < i:
        above = i
        

print("average = ",avg,"Above average = ",above)
print(news)
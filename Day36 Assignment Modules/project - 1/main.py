import models
std = ["std1","std2","std3","std4","std5"]
objects = []
for i in range(0,len(std)):
    print(f"Student {i+1} details")
    roll_no = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    std[i] = models.Student(roll_no,name,marks)
    objects.append(std[i])

print("-"*50)

print("All Student: ")
for i in range(0,len(std)):
        std[i].display()
print("-"*20)
print()
print("Students having marks greater than 60")
for i in range(0,len(std)):
        if std[i].marks >= 60:
            std[i].display()
print("-"*20)       
print()
print("Highest Marks:")
hig = std[0].marks 
ind = 0
for i in range(0,len(std)):
        if std[i].marks > hig:
            hig = std[i].marks
            ind = i
std[ind].display()
print("-"*20)
print()
sum = 0
for i in range(0,len(std)):
        sum = std[i].marks+sum
avg = sum/len(std)
print(f"Average Marks: {avg}")
            
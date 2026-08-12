from collections import namedtuple
Studnt = namedtuple("field",["rollno","name","marks"])
n = int(input("Enter n: "))
baccho = []
for i in range(n):
    print("Details: ")
    r = int(input("Enter Roll.no: "))
    name = input("Enter name: ")
    m =  float(input("Enter Marks: "))
    s = Studnt(r,name , m)
    baccho.append(s)
print(baccho)
for i in baccho:
    print(i.rollno  ,"and ",i.name,"and",i.marks)
    
    


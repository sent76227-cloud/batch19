row = int(input("Enter row:"))
colom = int(input("Enter colom:"))
matrix = []
sum = 0

for i in range(row):
    row = []
    for j in range(colom):
        row.append(int(input("enter element: ")))
    matrix.append(row)
sum = 0
for i in matrix:
    for j in i:
        sum = sum+j
print("Sum of all elemnets",sum)
        
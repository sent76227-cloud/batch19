r1 = int(input("Enter Row1: "))
c1 = int(input("Enter colom 1 : "))
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Element's :")))
    matrix1.append(row)

print(matrix1)




print("Plindrome Numbers Column-wise: ")
count = 0
add = [0]*c1
colom = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
        Value = matrix1[i][j]
        temp = Value

        x = 0
        rev = 0
        while x<temp:
            dig = temp%10
            rev = rev*10+dig  
            temp=temp//10
        if rev == Value:
            row.append(matrix1[i][j])
            add[j] = add[j]+count+1
        else:
            row.append(0)
    colom.append(row)
print(colom) 
print(add)
            

    
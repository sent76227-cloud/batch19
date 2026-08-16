m1 =[[1,3,4],[6,7,80],[2,5,9]]
m2 =[[1,3,4],[6,7,80],[2,5,9]]
m=[]
for i in range(len(m1)):
    row=[]
    
    for j in range(len(m1[i])):
        row.append(m1[i][j]+m2[i][j])  
    m.append(row)    
print(m)
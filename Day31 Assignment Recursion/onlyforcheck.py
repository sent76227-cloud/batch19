def checkHarshadnumber(numb):
    sum = 0
    temp = numb
    while numb > 0:
        last =  numb%10
        sum = sum + last
        numb = numb //10
    
    if temp%sum == 0:
        return 1
    else:
        return 0
print(checkHarshadnumber(19))
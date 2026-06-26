'''
to check the unit place 
input:
enter digit:
enter power:
enter operation:
enter second digit :
enter power:

output:
what opertion is performed to the given value give the right anser
'''
ent_first_num = int(input("Enter 1st Digit: "))
ent_power = input("Enter power of the given number: ")
ent_operation = input("Enter operation: ")
ent_sec_num = int(input("Enter 2st Digit: "))
ent_power_sec = input("Enter power of the 2nd number: ")
calculation =  ent_first_num **  ent_power ent_operation ent_sec_num ** ent_power_sec
pritn(f" final calculation is = {calculation+}")
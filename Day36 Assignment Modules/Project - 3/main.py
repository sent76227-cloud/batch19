import models
User = ["user1","user2","user3","user4","user5"]
Result = [] 
for i in range(0,len(User)):
    print(f"Enter Product details{i+1}")
    product_id = int(input("Enter product id: "))
    product_name =  input("Enter product name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    User[i] = models.Product(product_id,product_name,price,quantity)
    Result.append(User[i])

print()
print("-"*50)
print("All product's: ")
print()
for i in range(0,len(User)):
    User[i].display()
print()
print("-"*50)
print("Product Total Values: ")
total = []
for i in range(0,len(User)):
    sum = User[i].price * User[i].quantity
    total.append(sum)
print("Laptop = ",total[0])
print("Mouse = ",total[1])
print("Keyboard = ",total[2])
print("Monitor = ",total[3])
print("Printer = ",total[4])

print()
print("-"*50)
print("Low Stock Products: ")
print()
for i in range(0,len(User)):
    if User[i].quantity <= 10:
        print(User[i].product_name)

print()
print("-"*50)
print("Highest Price Product: ")
print()
hig = User[0].price
ind = 0
for i in range(0,len(User)):
    if User[i].price > hig:
        hig = User[i].price
        ind = i
print(f"{User[ind].product_name} = {User[ind].price}")

print()
print("-"*50)
print("Total Inventory value: ")
print()
total_inven = 0
for i in range(0,len(User)):
    total_inven = total_inven +total[i]
print(total_inven)
print()
print("Search Product Id: ")
serch = int(input("Enter id: "))
for i in range(0,len(User)):
    if serch == User[i].product_id:
        User[i].display()
        break
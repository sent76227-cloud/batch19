'''4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000
'''
type = input("Enter Class(business/economy): ").lower()
distance = int(input("Enter Distance: "))
booking = input("Enter booking time(early/later): ").lower()

if type=="business":
   if distance>1000:
      print("Price is 8000")
   else:
      print("Price is 5000")
else:
   if distance>1000:
      if booking=="early":
        print("price is 4000")
      else:
        print("price is 5000")
   else:
      print("price is 2500")
       
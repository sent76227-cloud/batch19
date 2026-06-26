''' 9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!  '''


num = int(input("Enter a num"))
length = len(str(num))
add = 0
for i in range(0,length) : 
   squ = num ** 2
 
while squ > 0:  

   sum = squ%10
   add = add + sum
   squ = squ//10
if add == num:
   print("Glowing Success! You've found the Neon Number! ")
else:
   print("Best of luck for next time")
   










'''
Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
print("In cricket, overs are given in decimal format . Convert overs into total balls and calculate run rate.")
runs =  int(input("Total runs  =  " ))
overs,balls = map(int,input("Total overs  = ").split("."))
total_balls = (overs*6)+balls
total_over = total_balls/6
run_rate = runs/total_over
print(f"Total Balls = {total_balls}\nRun Rate = {run_rate:.2f}")


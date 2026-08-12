import random

print("=" * 60)
print("🏏        ICC CRICKET WORLD CUP 2026")
print("=" * 60)

player_name = input("Enter Your Name : ")

score = 0
wickets = 0
balls = 6
target = 30
difficulty = 1
play_again = "yes"

while play_again.lower() == "yes":

    score = 0
    wickets = 0

    print("\n")
    print("=" * 60)
    print("WELCOME", player_name.upper())
    print("=" * 60)

    print("""
1. Start Match
2. Rules
3. Team Info
4. Exit
""")

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:

            print("\nChoose Difficulty")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")

            difficulty = int(input("Enter Difficulty : "))

            print("\nTOSS TIME")
            print("1. Heads")
            print("2. Tails")

            toss = int(input("Choose : "))

            computer = random.randint(1,2)

            if toss == computer:
                print("\n🎉 You Won The Toss")
                print("You Choose To Bat First")
            else:
                print("\nAustralia Won The Toss")
                print("Australia Sends You To Bat")

            print("\nTarget =", target)
            print("You Have", balls, "Balls")
            print("Need", target, "Runs To Win")

            for ball in range(1,7):

                if wickets == 1:
                    break

                print("\n--------------------------------")
                print("Ball :", ball)
                print("Current Score :", score)
                print("--------------------------------")

                print("""
Choose Shot

1. Defensive Shot
2. Cover Drive
3. Pull Shot
4. Lofted Shot
5. Helicopter Shot
""")

                shot = int(input("Enter Shot : "))

                # EASY MODE

                if difficulty == 1:

                    if shot == 1:
                        run = random.randint(1,2)

                    elif shot == 2:
                        run = random.randint(2,4)

                    elif shot == 3:
                        run = random.randint(3,4)

                    elif shot == 4:
                        run = random.choice([4,6])

                    elif shot == 5:
                        run = 6

                    else:
                        run = 0

                    score = score + run

                    print("Runs Scored :", run)

                # MEDIUM MODE

                elif difficulty == 2:

                    chance = random.randint(1,10)

                    if chance == 10:
                        wickets = wickets + 1
                        print("😢 OUT !!")

                    else:

                        if shot == 1:
                            run = random.randint(0,2)

                        elif shot == 2:
                            run = random.randint(1,4)

                        elif shot == 3:
                            run = random.randint(2,4)

                        elif shot == 4:
                            run = random.choice([0,4,6])

                        elif shot == 5:
                            run = random.choice([0,6])

                        else:
                            run = 0

                        score = score + run

                        print("Runs :", run)
                                    # HARD MODE

                elif difficulty == 3:

                    chance = random.randint(1,5)

                    if chance >= 4:
                        wickets = wickets + 1
                        print("💥 YOU ARE OUT !!")

                    else:

                        if shot == 1:
                            run = random.randint(0,1)

                        elif shot == 2:
                            run = random.randint(1,2)

                        elif shot == 3:
                            run = random.randint(2,4)

                        elif shot == 4:
                            run = random.choice([0,4])

                        elif shot == 5:
                            run = random.choice([0,6])

                        else:
                            run = 0

                        score = score + run

                        print("Runs :", run)

                else:
                    print("Invalid Difficulty")
                    break

                # Live Score

                print("------------------------------")
                print("Score :", score, "/", wickets)
                print("Target :", target)
                print("Runs Needed :", target - score)
                print("Balls Left :", 6 - ball)
                print("------------------------------")

                # Win Check

                if score >= target:
                    print("\n🏆 CONGRATULATIONS")
                    print("INDIA WON THE WORLD CUP")
                    break

            # Match Result

            print("\n")
            print("="*50)
            print("MATCH SUMMARY")
            print("="*50)

            print("Player :", player_name)
            print("Final Score :", score, "/", wickets)
            print("Target :", target)
            print("Balls Played :", ball)

            if score >= target:
                print("\n🎉 RESULT : YOU WON")

            elif wickets == 1:
                print("\n😢 RESULT : ALL OUT")
                print("AUSTRALIA WON")

            else:
                print("\n😢 RESULT : TARGET NOT CHASED")
                print("AUSTRALIA WON")

            # Strike Rate

            strike_rate = (score / ball) * 100

            print("Strike Rate :", round(strike_rate,2))

            # Awards

            if score >= 36:
                print("\n🌟 MAN OF THE MATCH")
                print(player_name)

            elif score >= 25:
                print("\n⭐ Excellent Batting")

            elif score >= 15:
                print("\n👍 Good Innings")

            else:
                print("\n😔 Better Luck Next Time")

        case 2:

            print("\n========== RULES ==========")
            print("1. Target = 36 Runs")
            print("2. Total Balls = 6")
            print("3. One Wicket Ends Match")
            print("4. Choose Correct Shot")
            print("5. Difficulty Changes Out Chance")

        case 3:

            print("\n========== TEAM INDIA ==========")
            print("1. Rohit Sharma")
            print("2. Shubman Gill")
            print("3. Virat Kohli")
            print("4. Shreyas Iyer")
            print("5. KL Rahul")
            print("6. Hardik Pandya")
            print("7. Ravindra Jadeja")
            print("8. Kuldeep Yadav")
            print("9. Mohammed Shami")
            print("10. Jasprit Bumrah")
            print("11. Mohammed Siraj")

        case 4:

            print("\nThank You For Playing ❤️")
            break

        case _:

            print("\nInvalid Choice")

    if choice != 4:

        play_again = input("\nPlay Again? (yes/no) : ")

print("\nProgram Ended Successfully")
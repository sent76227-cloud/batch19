import os


city_name = ""
mayor_name = ""
population = 0
city_score = 100
#variable of Report new acciden
minor_accident = 0
major_accident = 0
fatal_accident = 0
total_accident = 0
total_injured = 0
last_location = "No Accident"
last_type = "None"

#Variable of Chanalan's
helmet_case = 0
seatbelt_case = 0
signal_jump_case = 0
overspeed_case = 0
drink_drive_case = 0
jump_fine = 0
drink_fine = 0
helmet_fine = 0
seatbelt_fine = 0
overspeed_fine = 0

total_challan = 0
total_fine = 0

#variable of signal managment
#===========================
north = "red"
south = "red"
east = "red"
west = "red"
current_stat = "Red"
count_red = 0
count_yellow = 0
count_green = 0
new_east = "red"
new_north = "red"
new_south = "red"
new_west ="red"









print("="*110)
print("Trafic Control Center".center(110))
print("="*110)
print("\nWelcome officer!")
print("\nThis system helps manage:")

print("\n-----> Traffic Department")

input("\nPress Enter to Continue...")

#======================
# TRAFIC VARIABLES
#======================
bike = 0
car = 0
bus = 0
truck = 0
ambulance = 0
total_vechicles = 0
traffic_status = ""


city_name = input("Enter City Name: ")
mayor_name = input("Enter Mayor Name: ")
population = int(input("Enter Population: "))
os.system("cls")
print("\nCity Created Successfully!")

print()


while True:
                    os.system("cls")
                    print("Wellcome Office! ",mayor_name)
                    print("City Name : ",city_name)
                    print("Population of city is ",population)
                    print("="*110)
                    print("Traffic Department".center(110))
                    print("="*110)
                    print("1. Vehicle Entry")
                    print("2. Traffic Signal Control")
                    print("3. Accident Management")
                    print("4. Challan System")
                    print("5. Vehicle Statistics")
                    print("6. For Quit this program")
                    print("="*110)
                    choice = int(input("Enter Your Choice: "))
                    match choice:
                        case 1:
                            os.system("cls")
                            while True:
                                
                                print("="*110)
                                print("Vehicle management".center(110))
                                print("="*110)

                                print("1.Add Vehciles")
                                print("2.View vehicles")
                                print("3.Reset Vehicle Data")
                                print("4.Back")

                                vehicle_choice = int(input("enter choice: "))
                                match vehicle_choice:
                                    case 1:
                                        os.system("cls")
                                        print("="*110)
                                        print("Add Vehciles".center(110))
                                        print("="*110)
                                        new_bike = int(input("Enter No of Bike: "))
                                        new_car = int(input("Enter No of Car: "))
                                        new_bus = int(input("Enter No of Bus: "))
                                        new_truck = int(input("Enter No of Truck: "))
                                        new_ambulance = int(input("Enter No of Ambulance: "))

                                        car = new_car+car
                                        bike = new_bike+bike
                                        bus = new_bus+bus
                                        truck=new_truck+truck
                                        ambulance = ambulance+new_ambulance
                                        total_vechicles = (car+bike+bus+truck+ambulance)
                                        if total_vechicles >= 300:
                                            traffic_status = "low"
                                        elif total_vechicles >= 800:
                                            traffic_status = "Normal"
                                        elif total_vechicles >= 2000:
                                            traffic_status = "High"
                                            
                                    


                                        print("\nVehicle Data added successfully")
                                    case 2:
                                        os.system("cls")
                                        

                                        print("="*110)
                                        print("Vehicle statistics".center(110))
                                        print("="*110)

                                        print("Cars:    ",car)
                                        print("Bikes:    ",bike)
                                        print("Buses:    ",bus)
                                        print("Trucks:   ",truck)
                                        print("Ambulance:",ambulance)

                                        print("-"*110)
                                        print("\nTotal Vehicles: ",total_vechicles)
                                    case 3:
                                        os.system("cls")
                                        print("="*110)
                                        print("Reset your vehcile data".center(110))
                                        print("="*110)
                                        confirm = input("\nDo you want to rest the vehcile data yes/no :").lower()
                                        if confirm == "yes":
                                                car = 0
                                                bike = 0
                                                bus = 0
                                                ambulance = 0
                                                truck = 0
                                                print("\nVechicle Data Rest successfully")
                                        else:
                                            print("Rest Cancelled: ")
                                            
                                    case 4:
                                        
                                        break
                                    case _:
                                        print("Enter valid input")
                        case 2:
                            os.system("cls")
                            while True:
                                
                                print("="*110)
                                print("Signal managment".center(110))
                                print("="*110)

                                print("\n1.North Signal")
                                print("2.South Signal")
                                print("3.East Signal")
                                print("4.West Signal")
                                print("5.View All Signals")
                                print("6. Automatic signal System")
                                print("7.Back")


                                choice = int(input("Enter choice: "))
                                match choice:
                                        case 1:
                                            os.system("cls")
                                            while True:
                                                
                                                
                                                print("-"*110)
                                                print("North Signal".center(110))
                                                print("-"*110)

                                                print("\n1.Red")
                                                print("2.Yellow")
                                                print("3. Green")
                                                print("4. Back")

                                                choice = int(input("Enter your choice: "))
                                                match choice:
                                                        case 3:
                                                            new_north = "Green"
                                                            count_green = count_green+1
                                                            
                                                            print("\nNorth signal chaged successfully.")
                                                            print("\nCurrent Signal ",new_north)
                                                            print("\nVehicle Can Move: ")
                                                            
                                                        case 1:
                                                            new_north = "Red"
                                                            count_red = count_red+1
                                                            print("\nNorth signal chaged successfully.")
                                                            print("\nCurrent Signal ",new_north)
                                                            print("\nVehicle Can't Move: ")             

                                                        case 2:
                                                            new_north = "Yellow"
                                                            count_yellow = count_yellow+1
                                                            print("\nNorth signal chaged successfully.")
                                                            print("\nCurrent Signal ",new_north)
                                                            print("\nSlow Down. ") 
                                                        
                                                        case 4:
                                                            break
                                                        case _:
                                                            print("Invalid input")
                                        case 2:
                                            os.system("cls")
                                            while True:
                                                
                                                print("-"*110)
                                                print("South Signal".center(110))
                                                print("-"*110)

                                                print("1.Red")
                                                print("2.Yellow")
                                                print("3.Green")
                                                print("4.Back")

                                                choice = int(input("Enter your choice: "))
                                                match choice:
                                                    case 3:
                                                        new_south = "Green"
                                                        count_green = count_green+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_south)
                                                        print("\nVehicle Can Move: ")
                                                        
                                                    case 1:
                                                        new_south = "Red"
                                                        count_red = count_red+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_south)
                                                        print("\nVehicle Can't Move: ")   
                                                                                                                
                                                    case 2:
                                                        new_south = "Yellow"
                                                        count_yellow = count_yellow+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_south)
                                                        print("\nSlow Down. ") 
                                                        
                                                    case 4:
                                                        break
                                                    case _:
                                                        print("Invalid input")
                                        case 3:
                                            os.system("cls")
                                            while True:
                                                
                                                print("-"*110)
                                                print("East Signal".center(110))
                                                print("-"*110)

                                                print("1.Red")
                                                print("2.Yellow")
                                                print("3.Green")
                                                print("4.Back")

                                                choice = int(input("Enter your choice: "))
                                                match choice:
                                                    case 3:
                                                        new_east = "Green"
                                                        count_green = count_green+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_east)
                                                        print("\nVehicle Can Move: ")
                                                        
                                                    case 1:
                                                        new_east = "Red"
                                                        count_red = count_red+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_east)
                                                        print("\nVehicle Can't Move: ")                                                         
                                                    case 2:
                                                        new_east = "Yellow"
                                                        count_yellow = count_yellow+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_east)
                                                        print("\nSlow Down. ") 
                                                        
                                                    case 4:
                                                        break
                                                    case _:
                                                        print("Invalid input")
                                        case 4:
                                            os.system("cls")
                                            while True:

                                                print("-"*110)
                                                print("West Signal")
                                                print("-"*110)

                                                print("1.Red")
                                                print("2.Yellow")
                                                print("3.Green")
                                                print("4.Back")

                                                choice = int(input("Enter your choice: "))
                                                match choice:
                                                    case 3:
                                                        new_west = "Green"
                                                        count_green = count_green+1
                                                        
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_west)
                                                        print("\nVehicle Can Move: ")
                                                        
                                                    case 1:
                                                        new_west = "Red"
                                                        count_red = count_red+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_west)
                                                        print("\nVehicle Can't Move: ")   
                                                                                                                
                                                    case 2:
                                                        new_west = "Yellow"
                                                        count_yellow = count_yellow+1
                                                        print("\nNorth signal chaged successfully.")
                                                        print("\nCurrent Signal ",new_west)
                                                        print("\nSlow Down. ") 
                                                        
                                                    case 4:
                                                        break
                                                    case _:
                                                        print("Invalid input")
                                        case 5:
                                                os.system("cls")
                                                print("-"*100)
                                                print("Signal Status".center(110))
                                                print("-"*110)
                                                north = new_north
                                                south = new_south
                                                east = new_east
                                                west = new_west

                                                print("\nNorth singnal status: ",north)
                                                print("\nSouth singnal status: ",south)
                                                print("\nEast singnal status: ",east)
                                                print("\nWest singnal status: ",west)
                                        case 6:
                                            current_signal = 1

                                            while True:
                                            
                                                print("\n" + "="*50)
                                                print("      AUTOMATIC SIGNAL SYSTEM")
                                                print("="*50)
                                            
                                                match current_signal:
                                            
                                                    case 1:
                                            
                                                        print("\nNORTH  : GREEN")
                                                        print(" SOUTH  : RED")
                                                        print(" EAST   : RED")
                                                        print(" WEST   : RED")
                                            
                                                        print("\nVehicles Moving : NORTH")
                                            
                                                    case 2:
                                            
                                                        print("\n NORTH  : RED")
                                                        print(" SOUTH  : GREEN")
                                                        print(" EAST   : RED")
                                                        print(" WEST   : RED")
                                            
                                                        print("\nVehicles Moving : SOUTH")
                                            
                                                    case 3:
                                            
                                                        print("\n NORTH  : RED")
                                                        print(" SOUTH  : RED")
                                                        print(" EAST   : GREEN")
                                                        print(" WEST   : RED")
                                            
                                                        print("\nVehicles Moving : EAST")
                                            
                                                    case 4:
                                            
                                                        print("\n NORTH  : RED")
                                                        print(" SOUTH  : RED")
                                                        print(" EAST   : RED")
                                                        print(" WEST   : GREEN")
                                            
                                                        print("\nVehicles Moving : WEST")
                                            
                                                print("\n-----------------------------------")
                                                print("1. Next Signal")
                                                print("2. Stop Automatic Mode")
                                                print("-----------------------------------")
                                            
                                                choice = int(input("Enter Choice : "))
                                            
                                                match choice:
                                            
                                                    case 1:
                                            
                                                        current_signal += 1
                                            
                                                        if current_signal > 4:
                                                            current_signal = 1
                                            
                                                    case 2:
                                            
                                                        print("\nAutomatic Mode Stopped.")
                                                        break
                                            
                                                    case _:
                                            
                                                        print("\nInvalid Choice")

                                        case 7:
                                            break
                                        case _:
                                            print("Invalid input you enterd")

                        case 3:
                            os.system("cls")
                            while True:
                                print("="*110)
                                print("Accident Management".center(110))
                                print("="*110)

                                print("Today's Total Accidents : ",total_accident)
                                print("Total Injured: ",total_injured)

                                print("="*110)





                                print("1. Report New Accident")
                                print("2. View Accident Report")  
                                print("3. Emergency Response")  
                                print("4. Reset Accident Data")  
                                print("5. Back")

                                
                                
                                choice = int(input("Enter Your Choice: "))
                                match choice:
                                    case 1:
                                        os.system("cls")
                                        print("="*110)
                                        print("REPORT NEW ACCIDENT".center(110))
                                        print("="*110)
                                    
                                        location = input("Enter Accident Location : ")
                                    
                                        print("\nSelect Accident Type")
                                        print("1. Minor")
                                        print("2. Major")
                                        print("3. Fatal")
                                    
                                        accident_type = int(input("Enter Choice : "))
                                    
                                        injured = int(input("Enter Number Of Injured Persons : "))
                                    
                                        total_accident = total_accident + 1
                                        total_injured = total_injured + injured
                                    
                                        last_location = location
                                    
                                        if accident_type == 1:
                                    
                                            minor_accident = minor_accident + 1
                                            last_type = "Minor"
                                    
                                        elif accident_type == 2:
                                    
                                            major_accident = major_accident + 1
                                            last_type = "Major"
                                    
                                        elif accident_type == 3:
                                    
                                            fatal_accident = fatal_accident + 1
                                            last_type = "Fatal"
                                    
                                        else:
                                    
                                            print("Invalid Accident Type")
                                    
                                        print("\nAccident Report Registered Successfully")
                                    case 2:
                                        os.system("cls")
                                        print("="*110)
                                        print("ACCIDENT REPORT".center(110))
                                        print("="*110)
                                    
                                        print("Minor Accidents :", minor_accident)
                                        print("Major Accidents :", major_accident)
                                        print("Fatal Accidents :", fatal_accident)
                                    
                                        print("-"*110)
                                    
                                        print("Total Accidents :", total_accident)
                                        print("Total Injured   :", total_injured)
                                    
                                        print("-"*110)
                                    
                                        print("Last Accident Location :", last_location)
                                        print("Last Accident Type     :", last_type)
                                    
                                        input("\nPress Enter To Continue...")
                                    case 3:
                                        os.system("cls")
                                        print("="*110)
                                        print("EMERGENCY RESPONSE".center(110))
                                        print("="*110)
                                    
                                        if fatal_accident > 0:
                                    
                                            print("Emergency Level : HIGH")
                                            print("Hospital Alert : SENT")
                                            print("Police Alert : SENT")
                                            print("Ambulance : DISPATCHED")
                                            print("Road Closed : YES")
                                    
                                        elif major_accident > 0:
                                    
                                            print("Emergency Level : MEDIUM")
                                            print("Hospital Alert : SENT")
                                            print("Police Alert : SENT")
                                            print("Ambulance : DISPATCHED")
                                    
                                        elif minor_accident > 0:
                                    
                                            print("Emergency Level : LOW")
                                            print("Traffic Police Sent")
                                            print("Road Clearance Team Sent")
                                    
                                        else:
                                    
                                            print("No Accident Reported")
                                            print("City Is Safe")
                                    
                                        input("\nPress Enter To Continue...")

                                    case 4:
                                        print("="*110)
                                        print("RESET ACCIDENT DATA".center(110))
                                        print("="*110)
                                    
                                        confirm = input("Do You Want To Reset All Data (yes/no) : ").lower()
                                    
                                        if confirm == "yes":
                                    
                                            minor_accident = 0
                                            major_accident = 0
                                            fatal_accident = 0
                                    
                                            total_accident = 0
                                            total_injured = 0
                                    
                                            last_location = "No Accident"
                                            last_type = "None"
                                    
                                            print("\nAll Accident Data Reset Successfully.")
                                    
                                        else:
                                    
                                            print("\nReset Cancelled.")
                                    case 5:
                                        break  
                        case 4: 
                            os.system("cls")
                            while True:
                                print("="*110)
                                print("4. Challan System ".center(110))
                                print("="*110)
    
                                print("1.No Helmet")
                                print("2. No Seat Belt")
                                print("3. Signal Jump")
                                print("4. Over Speed")
                                print("5. Drink And Drive")
                                print("6. View Challan Report")
                                print("7. Reset Challan Data")
                                print("8. Back")
    
                                choice = int(input("Enter Your Choice: "))
                                match choice:
                                    case 1 :
                                        os.system("cls")
                                        print("="*110)
                                        print("No Helmet Challan ".center(110))
                                        print("="*110)
    
                                        riders = int(input("Enter Number of Riders: "))
    
                                        helmet_fine = 500*riders
                                        helmet_case+=riders
                                        
    
                                        print("Challan Generated Successfully.")
                                    case 2:
                                        os.system("cls")
                                        print("="*110)
                                        print("No Seat Belt Challan ")
                                        print("="*110)
    
                                        drivers = int(input("Enter No of Challans: "))
                                        seatbelt_fine = 1000*drivers
                                        seatbelt_case+=drivers
                                        
    
                                        print("Seat bealt Challan Generated Successfully.")
                                    case 3:
                                        os.system("cls")
                                        print("="*110)
                                        print("Signal Jump".center(110))
                                        print("="*110)
    
                                        vehicle = int(input("Enter number of vehicle jump signal"))
                                        jump_fine = 2000*vehicle
                                        signal_jump_case+=vehicle
                                        
    
                                        print("Vehicle jump Challan Generate Successfully.")
                                    case 4:
                                        
                                        os.system("cls")
                                        print("="*110)
                                        print("Over Speed ".center(110))
                                        print("="*110)
    
    
                                        overspeed = int(input("Enter overspeed vehile's"))
                                        overspeed_case+=overspeed
                                        overspeed_fine = 1500*overspeed
                                        
    
                                        print("Overspeed fine Create successfully")
                                    case 5:
                                        print("="*110)
                                        print("Drink and Drive".center(110))
                                        print("="*110)
    
                                        drink = int(input("enter Drink and Drive case: "))
                                        drink_drive_case+=drink
                                        drink_fine = 5000*drink
    
                                        print("Overspeed fine Create successfully")
                                    case 6:
                                        print("="*110)
                                        print("View Challan Report".center(110))
                                        print("="*110)
    
                                        print("Helmet Cases :",helmet_case)
                                        print("Seat Belt Cases : ",seatbelt_case)
                                        print("Signal Jump Cases : ",signal_jump_case )
                                        print("Over Speed Cases : ",overspeed_case)
                                        print("Dink and Drive Cases: ",drink_drive_case)
    
                                        print("------------------------------------------------")
                                        total_fine = jump_fine+drink_fine+helmet_fine+seatbelt_fine+overspeed_fine
                                        total_challan = helmet_case+seatbelt_case+drink_drive_case+signal_jump_case+overspeed_case
    
                                        print("Total Challans: ",total_challan)
                                        print("Total fine: ",total_fine)
                                    case 7:
                                        os.system("cls")
                                        print("="*110)
                                        print("Reset Challan Data: ")
                                        print("="*110)
    
    
                                        ask = input("Do you want to Reset yes/no ").lower()
                                        if ask == "Yes":
                            
                                            total_challan = 0
                                            total_fine = 0
                                            helmet_case = 0
                                            seatbelt_case = 0
                                            signal_jump_case = 0
                                            overspeed_case = 0
                                            drink_drive_case = 0
                                        
                                        
                                        print("All Challan Data Reset Successsully")
                                    case 8:
                                        break
                                    case _:
                                        print("Invalid input! please read instruction")

                        case 5:
                            os.system("cls")
                            while True:
                                print("="*110)
                                print("Traffic Statistics".center(110))
                                print("="*110)

                                print("1. Vehicle Statistics")
                                print("2. Signal Statistics")
                                print("3. Accident Statistics")
                                print("4. Challan Statistics")
                                print("5. Overall Traffic Report")
                                print("6. Back")

                                choice1 = int(input("Enter your Choice: "))
                                match choice1 :
                                    case 1:
                                        
                                        os.system("cls")
                                        print("="*110)
                                        print("Vehicle Statistics".center(110))
                                        print("="*110)
                                        

                                        print("Cars:    ",car)
                                        print("Bikes:    ",bike)
                                        print("Buses:    ",bus)
                                        print("Trucks:   ",truck)
                                        print("Ambulance:",ambulance)
                                        print("-"*110)
                                        print("Total Vehicles: ",total_vechicles)
                                        if total_vechicles >=100:
                                            traffic_status = "Low"
                                            print(traffic_status)
                                        elif total_vechicles >=250:
                                            traffic_status = "Normal"
                                            print(traffic_status)
                                        elif total_vechicles >= 500:
                                            traffic_status = "Heavy"
                                            print(traffic_status)
                                        else:
                                            print("All Roads are Block due to very heaavy traffic")

                                    case 2:
                                        os.system("cls")
                                        print("="*110)
                                        print("Signal Stastistics".center(110)) 
                                        print("="*110)

                                        print("North singnal status: ",north)
                                        print("South singnal status: ",south)
                                        print("East singnal status: ",east)
                                        print("West singnal status: ",west)
                                        print("-"*110)
                                        print("Green Signal :",count_green)
                                        print("Red Signals: ",count_red)
                                        print("Yellow Signals: ",count_yellow)
                                        print("="*110)
                                    case 3:
                                        os.system("cls")
                                        print("="*110)
                                        print("Accident Statistics".center(110))
                                        print("="*110)

                                        print("Minor Acidents :",minor_accident)
                                        print("Maor Accidents :",major_accident)
                                        print("Fatal Accidents :",fatal_accident)

                                        print("-"*110)

                                        print("Total Accidents :",total_accident)
                                        print("Total Injured :",total_injured)
                                        print("Last Location",last_location)

                                        print("="*110)

                                    case 4:
                                        os.system("cls")
                                        print("="*110)
                                        print("Challan Statsics".center(110))
                                        print("="*110)

                                        print("Helmet Cases  ",helmet_case)
                                        print("Seat Belt Cases: ",seatbelt_case)
                                        print("Signal Jump Cases: ",jump_fine)
                                        print("Over Speed Cases ",overspeed_case)
                                        print("Drink and Drive cases :",drink_drive_case)

                                        print("-"*110)

                                        print("Total Challans :",total_challan)
                                        print("Total Fine :",total_fine)

                                        print("="*110)
                                    case 5:
                                        os.system("cls")
                                        print("="*110)
                                        print("Overall Traffic Report".center(110))
                                        print("="*110)

                                        print("Total Vehicles :",total_vechicles)
                                        print("Traffic Status :",traffic_status)
                                        print("-"*110)
                                        print("Total Accidents :",total_accident)
                                        print("Total Injured :",total_injured)
                                        print("-"*110)
                                        print("Total Challans :",total_challan)
                                        print("Fine Collected :",total_fine)
                                        print("-"*110)
                                        print("North Signal :",north)
                                        print("South Signal ",south)
                                        print("East Signal",east)
                                        print("West Signal ",west)

                                        print("="*110)
                                    case 6:
                                        break
                                    case _:
                                        print("You enter Wrong Input!! ")

                        
                        case 6:
                            print("You are out of the room ")
                            break
                        case _:
                            print("Invalide input! loding...")


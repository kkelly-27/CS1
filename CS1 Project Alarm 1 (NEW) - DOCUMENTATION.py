print("ALARM!")         #Displays "ALARM!"
while True:             #Forever Loop
    morning_work = str.upper(input("Are you working out this morning? Y/N: "))      #Stores user response to Working Out (str.upper = Both upper and lowercase work)
    if morning_work == "Y":                                                         #If the user says yes to working out (Y)
        print("Get up and workout.")                                                #Display "Get up and workout."
        break                                                                       #Breaks the Forever Loop
    elif morning_work == "N":                                                       #If the user says no to working out (N)
        print("Workout tonight instead.")                                           #Display "Workout tonight instead"
        break                                                                       #Breaks Forever Loop
    else:                                                                           #If the user says Anything else
        print("Error - Invalid Answer")                                             #Display "Error - Invalid Answer"
while True:                                                                         #Forever Loop
    take_shower = str.upper(input("Will you be taking a shower this morning? Y/N: "))   #Stores user response to Taking a Shower (str.upper = Both upper and lowercase work)
    if take_shower == "Y":                                                              #If the user says yes to taking a shower (Y)
        print("Take a shower.")                                                         #Display "Take a shower."
        print("Get changed.")                                                           #Display "Get changed." 
        break                                                                           #Breaks Forever Loop
    elif take_shower == "N":                                                            #If the user says no to taking a shower (N)
        print("Take shower tonight.")                                                   #Display "Take shower tonight." 
        print("Get changed.")                                                           #Display "Get changed."
        break                                                                           #Break Forever Loop
    else:                                                                               #If the user says anything else
        print("Error - Invalid Answer")                                                 #Display "Error - Invalid Answer"    
while True:                                                                             #Forever Loop
    different_clothing = str.upper(input("Is it cold outside? Y/N: "))                  #Stores user response to Temperature Outside (Putting On A Pullover) (str.upper = Both upper and lowercase work)
    if different_clothing == "Y":                                                       #If the user says yes to it's cold outside (Y) 
        print("Put on pullover.")                                                       #Display "Put on pullover."     
        break                                                                           #Break Forever Loop
    elif different_clothing == "N":                                                     #If the user says no to it's cold outside (N)
        print("Keep what you have on.")                                                 #Display "Keep what you have on." 
        break                                                                           #Break Forever Loop    
    else:                                                                               #If the user says anything else 
        print("Error - Invalid Answer")                                                 #Display "Error - Invalid Answer"    
while True:                                                                             #Forever Loop 
    shave = str.upper(input("Do you need to shave this morning? Y/N: "))                #Stores user response to Shaving This Morning (str.upper = Both upper and lowercase work)
    if shave == "Y":                                                                    #If the user says yes to shaving this morning (Y)         
        print("Shave.")                                                                 #Display "Shave."    
        print("Eat Breakfast.")                                                         #Display "Eat Breakfast." 
        print("Go to school.")                                                          #Display "Go to School."     
        break                                                                           #Break Forever Loop
    elif shave == "N":                                                                  #If user says no to shaving this morning (N) 
        print("Eat Breakfast.")                                                         #Display "Eat Breakfast." 
        print("Go to school.")                                                          #Display "Go to school." 
        break                                                                           #Break Forever Loop 
    else:                                                                               #If the user says anything else 
        print("Error - Invalid Answer")                                                 #Display "Error - Invalid Answer" 
while True:                                                                             #Forever Loop 
    days = ["A", "B", "C", "D", "E", "F", "G", "H"]                                     #All of the days (In Order) include: A, B, C, D, E, F, G, H
    periods = ["6", "3", "8", "7", "4", "2", "5", "1"]                                  #All of the periods (In Order) include: 6, 3, 8, 7, 4, 2, 5, 1 
    day = str.upper(input("What block day is it? A/B/C/D/E/F/G/H: "))                   #Stores user response to What Block Day Is It (str.upper = Both upper and lowercase work)
    if day in days:                                                                     #If the day variable is a certain day...         
        index = days.index(day)                                                         #Go through List of Days 
        print(f"Go to Period: {periods[index]}.")                                       #Display "Go to Period" (Selected Day Period (Day List)) "."
    else:                                                                               #If the user says anything else 
        print("Error - Invalid Answer")                                                 #Display "Error - Invalid Answer" 




import random #Import random library
import time
import os
import sys

def colored_text(text, color_name): #Function for given text to be printed in a given color
    color_codes = {
        'black' : '\033[30m', #Black Color
        'red' : '\033[31m', #Red Color
        'yellow' : '\033[33m', #Yellow Color
        'green' : '\033[32m', #Green Color
        'blue' : '\033[34m', #Blue Color
        'purple' : '\033[35m', #Purple Color
        'reset' : '\033[0m' #Reset
    }
    print(f'{color_codes.get(color_name)}{text}{color_codes.get("reset")}') #

color_list = ["red", "yellow", "black", "blue", "purple", "green"] #Makes a list of colors
user_name = input("Hello user! Please enter your name here: ") #Name Interperator
print('Welcome to the game, ' + user_name + '!')
time.sleep(1.5)
print('The rules are simple.') #RULES
time.sleep(1)
print('- Look for the color of the following text.')
print('- You will choose the color of the text, NOT what the test says.')
time.sleep(4)
print('Try not to slip up. Good luck.')
time.sleep(3)
os.system("cls")  # Clear the terminal screen
print("3")
time.sleep(1)
os.system("cls")  # Clear the terminal screen
print("2")
time.sleep(1)
os.system("cls")  # Clear the terminal screen
print("1")
time.sleep(1)
os.system("cls")  # Clear the terminal screen
# TEST: print('- You will have a time limit to get as many numbers as possible (30 Seconds)')

color_round = 0
color_point = 0 
while True:
    text_color = random.choice(color_list) #Choose a random text color
    print_color = random.choice(color_list) #Choose a random print color
    colored_text(text_color, print_color) #Print the text with the given color followed by the reset code to asure no color leaks
    user_choice = input("What color is this?: ") #Prompt user to enter the color of the text
    
    if user_choice == print_color: #If user gets it right
        print("Correct!") #Tell them they are right
        color_point += 1 #Add 1 to the # points
    else:
        print("Incorrect.")  #Else Incorrect 
    color_round += 1 #Add 1 to the # round
      
    print(f"You have gotten {color_point}/{color_round} correct!") #Sum of rounds

    while True:
        play_again = str.lower(input("Would you like to play again? (y/n): ")) #Asks them to play again
        
        if play_again == 'y':
            break #End Forever Loop
        elif play_again == 'n':
            print("Goodbye and thanks for playing!")
            sys.exit() #Exits Game
        else:
            print("Error - Invalid Answer.")

            

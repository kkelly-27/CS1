
import random #Imports Random
import os #Imports OS
import sys #Imports System
weapon_list = ["R", "P", "S"] #Weapon List (Rock (R), Paper (P), Scissors (S))
player1_point_list = 0 #Start with 0 (Player 1)
player2_point_list = 0 #Start with 0 (Player 2)

print("Hello and Welcome to Rock, Paper, Scissors!") #Display (Print) "Hello and Welcome to Rock, Paper, Scissors!"
player1_name = str.upper(input("Player 1, enter your name: ")) #Player 1 Enters Their Name
game_style = str.upper(input(f"{player1_name}, please pick a gamemode - S (Singleplayer) or M (Multiplayer): ")) #Gamemode Pick

if game_style == "S": #Singleplayer (Bot)
    player2_name = "Bot"
else:
    #PlayerNameInserter
    player2_name = str.upper(input("Player 2, enter your name: "))

#MAIN-FRAME
while True:
    player_1 = str.upper(input(f"{player1_name}, please choose a weapon - R, P, S: "))   #Asks Player1 to choose a weapon (R, P, or S)

    if game_style == "S":
        player_2 = random.choice(weapon_list) #Bot List (Singleplayer)
    else:
        os.system("cls") #Clear Terminal
        player_2 = str.upper(input(f"{player2_name}, please choose a weapon - R, P, S: "))  #Asks Player2 to choose a weapon (R, P, or S)
        os.system("cls") #Clear Terminal

    print(player1_name, "has chosen", player_1) #Displays Player Choice 
    print(player2_name, "has chosen", player_2, "\n") #Displays Player Choice  

    if player_1 == player_2:
        print("It’s a tie; Try Again!") #Player 1 = Player 2 (Points) == A Tie
    elif player_1 == "R" and player_2 == "P":
        player2_point_list += 1 #Player 2 Get 1 Point
        print(player2_name, "has won!")
    elif player_1 == "R" and player_2 == "S":
        player1_point_list += 1 #Player 1 Get 1 Point
        print(player1_name, "has won!")
    elif player_1 == "P" and player_2 == "R":
        player1_point_list += 1 #Player 1 Get 1 Point
        print(player1_name, "has won!")
    elif player_1 == "P" and player_2 == "S":
        player2_point_list += 1 #Player 2 Get 1 Point
        print(player2_name, "has won!")
    elif player_1 == "S" and player_2 == "R":
        player2_point_list += 1 #Player 2 Get 1 Point
        print(player2_name, "has won!")
    elif player_1 == "S" and player_2 == "P":
        player1_point_list += 1 #Player 1 Get 1 Point
        print(player1_name, "has won!") #"Player 1 has won" Display
    else:
        print("Error - Invalid Choice") #Error Response

    print(player1_name, "Points:", player1_point_list) #PLayer 1 Points
    print(player2_name, "Points:", player2_point_list) #PLayer 2 Points

    while True:
        play_again = input("PLAY AGAIN? (Y/N): ").lower() #Asks "Play Again"
        
        if play_again == "y": #Yes 
            break
        elif play_again == "n": #No
            exit()
        else:
            print("Error = Invalid Response.") 
        

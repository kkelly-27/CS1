import random

total_rarity = 0
first_name = ["Nate", "Kyle", "Josh", "Jacob", "Jake", "Finn", "George", "Henry", "Danny", "Patrick", "Cooper", "LeBron", "Michael", "Mike", "Jordan", "Erin", "Emma", "Leah", "Raymond", "Jackson", "Jack", "Cody", "Bill", "Muhammad"] #First Name List
first_rarity = [15,30,15,42,10,30,10,20,20,30,20,50,15,15,30,25,15,35,45,15,10,40,20,1] #First Name Rating List
last_name = ["Dominguez","Smith","Neumann","James","Jordan","Perez","Ramirez","Jones","Brown","Miller","Jackson","Rodriguez","Kelly","Lobante"] #Last Name List
last_rarity = [45,5,40,35,40,30,15,20,15,15,20,25,40,45] #Last Name Rarity List

name_generation_quantity = int(input("How many names do you want to generate? ")) #Ask Question 

for i in range(name_generation_quantity): #PRINT WHAT THEY SAID ON THE QUESTION 
    first_name_index = random.randint(0,15)
    last_name_index = random.randint(0,15)
    fn_rarity = first_rarity[first_name_index]
    ln_rarity = last_rarity[last_name_index] #TOTAL RATING 
    print(f'Name: {first_name[first_name_index]} {last_name[last_name_index]}')
    print(f'First Name Rarity: {fn_rarity}%, Last Name Rarity:  {ln_rarity}%')

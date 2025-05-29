import random

total_rating = 0
first_name = ["Window", "Car", "Vacuum", "Fresh", "Green", "Blue", "Yellow", "Red", "Squeekee"] #First Name List
fist_rating = [40,30,20,42,66, , , , 50] #First Name Rating List
last_name = ["Cleen","Star","Srcub","Mini","Canvas","","","",""] #Last Name List
last_rating = [45,20,32,43, 50, ] #Last Name Rating List

name_generation_quantity = int(input("How many names do you want to generate?")) #Ask Question 
print(first_name) #Print Food List
print() #Print Price List

for i in range(name_generation_quantity): #PRINT WHAT THEY SAID ON THE QUESTION 
    index = random.randint(0,8)
    print(f'Name: {first_name[index]} {random.choice(last_name)} | Rating: ${prices[index]}')
    total_rating = fist_rating[index] + last_rating[index] #TOTAL RATING 
print(f'TOTAL RATING: {total_rating}%')
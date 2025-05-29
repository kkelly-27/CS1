import random

total_price = 0
foods = ["Cauliflower", "Tilapia Fillet", "Pork Loin", "Salmon", "Potatoes", "Three Color Squash", "Eggplant", "Steak", "Baguette"] #Food List
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20] #Price List
flairs = ["with Balsamico","with Garlic & Olive Oil","with Minted Yogurt","with Chutney","with Salad","with Salsa","Over Sticky Rice","Au Jus","with Basmati Rice"] #Addons

dish_quantity = int(input("How many dishes do you want on your menu?")) #Ask Question 
print(foods) #Print Food List
print(prices) #Print Price List

for i in range(dish_quantity): #PRINT WHAT THEY SAID ON THE QUESTION 
    index = random.randint(0,8)
    print(f'Food: {foods[index]} {random.choice(flairs)} | Price: ${prices[index]}')
    total_price += prices[index] #TOTAL PRICE 
print(f'TOTAL PRICE: ${total_price}')
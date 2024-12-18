#MAGIC8BALL

import random

answer_list = ["It is certain.", "Reply hazy.", "Try again.", "Don’t count on it.", "It is decidedly so.", "Ask again later.", "My reply is no.", "Without a doubt.", "Better not tell you now.", "My sources say no.", "Yes definitely.", "Cannot predict now.", "Outlook not so good.", "You may rely on it.", "Concentrate and ask again.", "Very doubtful.", "As I see it, Yes.", "Yes.", "Most likely.", "Outlook good.", "Signs point to yes."]          
while True:
    magic_8 = str.lower(input("Magic 8 Ball -- Ask Me A Question!: "))
    random_reply = random.choice(answer_list)
    if "?" in magic_8:                     #There is a "?" in it
        print(random_reply)
    else:
        print("Error - Invalid Question")
                            

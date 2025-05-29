import random

def chorus():
    print('''
If you could see 'em now, you'd be proud
But you'd think they's yuppies
Your funeral was beautiful
I bet God heard you coming
    ''')
def sing_song():
    print('''
The kids are in town for a funeral
So pack the car and dry your eyes
I know they got plenty of young blood left in 'em
And plenty nights under pink skies
You taught 'em to enjoy
          
So clean the house, clear the drawers
Mop the floors, stand tall
Like no one's ever been here before or at all
And don't you mention all the inches
That are scraped on the door frame
We all know you tiptoed up to 4'1" back in '08
    ''')
    chorus()
    print('''
The kids are in town for a funeral
And the grass all smells the same
As the day you broke your arm swingin'
On that kid out on the river
You bailed him out
Never said a thing about Jesus or the way he's living
          
If you could see 'em now, you'd be proud
But you'd think they's yuppies
Your funeral was beautiful
Bet God heard you coming
          
If you could see 'em now, you'd be proud
But you'd think they's yuppies
Your funeral was beautiful
I bet God heard you coming
          
The kids are in town for a funeral
So pack the car and dry your eyes
I know they got of plenty young blood left in 'em
And plenty nights under pink skies
You taught 'em to enjoy
          
They call your hats a race to claim
Like who gets to ride shotgun
Your pocket knife, it went missing
I think we know who got that one
You used to let her cut the ribbons
On all of her own presents
It made me nervous, but now I see
We just taught different lessons
    ''')
   
def add(a, b):
    print(a + b)
def print_list(array):
    for i in array:
        print(i)
def in_list(array, element):
    return element in array
"""
Function Description: 
    Checks if the word is in the list

Args: 
    List (list): A list
    Word (str): A word

Returns:
    Prints boolean for if the word is in the list
"""


def get_integer(order):
    while True:
        try: 
            num = int(input(f"Pick your {order} number "))
            return num
        except:
            print('Not an integer!')
def get_integers():
    integer_1 = get_integer('first')
    integer_2 = get_integer('second')
    return integer_1, integer_2
def get_random():
    a, b = get_integers()
    print(random.randint(a, b))
def count_vowels(word):
    counter = 0
    for char in word:
        if char in ["a", "u", "e", "i", "o"]:
            counter += 1
    return counter

"""
Function Description: 
    1. Gets integers in order
    2. Gets two integers
    3. Gets a random integer
    4. Counts vowels in a word or name
    

Args: 
    1. order: Keeps numbers in order
    2. (No Arg)
    3. (No Arg)
    4. word: Selects the word to count vowels in

Returns:
    1. (Ordered Number)
    2. (Both Integers)
    3. (Random Integers)
    4. (Number of Vowels in Selected Word/Name/Sentence)
"""

def reverse(string1):
    reverse_list = []
    original_list = list(string1)
    for i in range(len(original_list)):
        reverse_list.append(original_list[len(original_list)-i-1])
    reverse_list = "".join(reverse_list)
    print(reverse_list)
reverse("kyle kelly")


def get_initials(fullname):

    """
    Function Description: 
        Displays the initials of a name

    Args: fullname: Holds Your Full Name (Input)
        

    Returns:
        Name Initials
        
    """
    names = fullname.split(' ')
    initials = ''

    for name in names:
        initials += name[0]
    return initials
def main():
    motorcycle_brand_list = ["Yamaha", "Ducati", "Kawasaki", "Suzuki", "BMW"]

    while True:
        option = input('What would you like to do? 1. Sing a song, 2. Add two numbers, 3. Print a list, 4. Check a list, 5. Spin a random integer, 6. Count vowels')

        if option == '1':
            sing_song()
        elif option == '2':
            a, b = get_integers()
            add(a, b)
        elif option == '3':
            print_list(motorcycle_brand_list)
        elif option == '4':
            word = input('Enter a word to check: ')
            in_list(motorcycle_brand_list, word)
        elif option == '5':
            get_random()
        elif option == '6':
            word = input('Enter a word to count: ')
            counter = count_vowels(word)
            print(f"You have {counter} vowels.")
        print(get_initials('Kyle Michael Kelly'))
        fullname = input('Enter your fullname: ')
        print(get_initials(fullname))

        """
    Function Description: 
        Let's you pick a function

    Args: ((No Arg))
    

    Returns:
        (N/A) - The option you selected 
    
    """
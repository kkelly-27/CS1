#(1) websites and their (2) usernames and (3) passwords

def info_input(password_list, username_list, website_list):
    password_list.append(input("ENTER PASSWORD: "))
    username_list.append(input("ENTER USERNAME: "))
    website_list.append(input("ENTER WEBSITE: "))
    return password_list, username_list, website_list

def view_info(password_list, username_list, website_list):

    print(password_list)
    print(username_list)
    print(website_list)


def main():

    password_list, username_list, website_list = [], [], []
    while True:
        option = input('Setup Keep File: 1. Enter Information, 2. View Information, 3. Quit: ')

        if option == '3':
            quit()   
        elif option == '1':
            info_input(password_list, username_list, website_list)  
        elif option == '2':
            view_info(password_list, username_list, website_list)


main()

#Prompt the user to enter websites and their usernames and passwords to store in the parallel arrays above
#print("Fill in your information in the following lists:")

#Allow the user to print out the list of websites along with their usernames and passwords.
#input

#Allow the user to access a specific website's username and password.



#Allow the user to end the program.






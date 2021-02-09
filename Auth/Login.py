import bcrypt, getpass, logging
from Models.User import User



#Declare Global Variables
GlobalUser = None


def login():

    type = input("\n\nEnter the type of user you are: \n\n1)Existing User \n2)New User\n\nYour Input: ")

    if type == "0":
        exit()

    #REMOVE FOR PRODUCTION
    #This is a small clause for testing purposes to bypass the login system.
    elif type == "chase":
        user = User.fetch(Username = 'BYYCHASE')
        return user 

    while type != "1" and type != "2" and type != "0":
        type = input("\n\nThe only choices are '1' or '2': \n\n1)Existing User \n2)New User\n\nYour Input: ")

        if type == "0":
            exit()

        #REMOVE FOR PRODUCTION
        #This is a small clause for testing purposes to bypass the login system.
        elif type == "chase":
            user = User.fetch(Username = 'BYYCHASE')
            return user 
  
    if type == "2":
        create_new_user()
 
    if type == "0":
        exit()

    Username = input("\n\nPlease input your username: ")
    Username = Username.upper()
    Password = getpass.getpass()
    user = User.fetch(Username = Username)
    hashedPassword = user.Password
    
    if bcrypt.checkpw(Password.encode('utf-8'), hashedPassword):
        return user

    else:
       print("\n\n-----------------------------------------\n|Looks like the login failed, try again!|\n-----------------------------------------")
       login()


def create_new_user():

    print("\n\nWelcome to BudgetBuddy!\nBelow we will get you setup with a new account!")

    Username = input("\n\nPlease input a Username: ")
    Username = Username.upper()
    temp_user = User()
    temp_user = User.fetch(Username = Username)
    
    while temp_user != "User Not Found":

        Username = input("\n\nUsername Taken, Please input a new Username: ")
        temp_user = User.fetch(Username = Username)

    First_Name = input("\nPlease input your first name: ")
    First_Name = First_Name.upper()
    First_Name = First_Name.strip()
    Last_Name = input("\nPlease input your last name: ")
    Last_Name = Last_Name.upper()
    Last_Name = Last_Name.strip()
    Password = input("\nPlease input a password: ")
    Password2 = input("\nPlease re-input your password: ")

    if Password == Password2:

        salt = bcrypt.gensalt()
        CryptPassword =  bcrypt.hashpw(Password.encode('utf-8'), salt)
        User(Username = Username.upper(), First_Name = First_Name.upper(), Last_Name = Last_Name.upper(), Password = CryptPassword).commit_user()

    print("\nTIME TO LOGIN\n")    
    

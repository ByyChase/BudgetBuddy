import bcrypt, getpass, logging
from Models.User import User

def login():

    """
    This function is used to log users in. They can chose to login to an existing account
    they can create a new one. This
    """

    try:
        type = input("\n\nEnter the type of user you are: \n\n1)Existing User \n2)New User\n\nYour Input: ")

        if type == "0":
            exit()

        #REMOVE FOR PRODUCTION
        #This is a small clause for testing purposes to bypass the login system.
        elif type == "chase":

            try:

                user = User.fetch(Username = 'BYYCHASE')
                return user 
                logging.info("User Chase have been retreived")

            except Exception as e:

                logging.exception("Unable to retreive user Chase")
                login()

        while type != "1" and type != "2" and type != "0":
            type = input("\n\nThe only choices are '1' or '2': \n\n1)Existing User \n2)New User\n\nYour Input: ")

            if type == "0":
                exit()

            #REMOVE FOR PRODUCTION
            #This is a small clause for testing purposes to bypass the login system.
            elif type == "chase":

                try:

                    user = User.fetch(Username = 'BYYCHASE')
                    return user
                    logging.info("User Chase have been retreived")

                except Exception as e:

                    logging.exception("Unable to retreive user Chase")
                    login()
    
        if type == "2":

            create_new_user()
    
        if type == "0":

            exit()
        
        logging.info("User type input successful")

    except Exception as e:

        logging.exception("Unable to get user input for user type during intial login")
        login()

   

    Username = input("\n\nPlease input your username: ")
    Username = Username.upper()
    Password = getpass.getpass()

    try:

        user = User.fetch(Username = Username)
        logging.info("User was able to be fetched for login validation")

    except Exception as e:

        logging.exception("Unable to fetch user for login")

    if user:

        hashedPassword = user.Password

    else:

        logging.error("Unable to retreive password from user object")
        print("\n\n-----------------------------------------\n|Looks like the login failed, try again!|\n-----------------------------------------")
        login()

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
    try:

        temp_user = User.fetch(Username = Username)
    
    except Exception as e:

        logging.exception("Problem fetching the user from the database")
        print("***ERROR WITH ACCOUNT CREATION PROBLEM***\n\nReturning to login page")
        login()


    
    
    while temp_user != "User Not Found":

        Username = input("\n\nUsername Taken, Please input a new Username: ")
        try:

            temp_user = User.fetch(Username = Username)

        except Exception as e:

            logging.exception("Unable to fetch user from database")
            login()

    First_Name = input("\nPlease input your first name: ")
    First_Name = First_Name.upper()
    First_Name = First_Name.strip()
    Last_Name = input("\nPlease input your last name: ")
    Last_Name = Last_Name.upper()
    Last_Name = Last_Name.strip()
    Password = input("\nPlease input a password: ")
    Password2 = input("\nPlease re-input your password: ")

    if Password == Password2:

        try:

            salt = bcrypt.gensalt()
            CryptPassword =  bcrypt.hashpw(Password.encode('utf-8'), salt)
            User(Username = Username.upper(), First_Name = First_Name.upper(), Last_Name = Last_Name.upper(), Password = CryptPassword).commit_user()

        except Exception as e:

            logging.exception("Unable to commit new user to database")
            login()

    print("\n***TIME TO LOGIN***\n")    
    

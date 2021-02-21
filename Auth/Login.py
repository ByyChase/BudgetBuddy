import bcrypt, getpass, logging
from Models.User import User

def login():

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

    try:

        Username = input("\n\nPlease input your username: ")
        Username = Username.upper()
        Password = getpass.getpass()

        try:

            user = User.fetch(Username = Username)

        except Exception as e:

            logging.exception("Failed Database call")

        if user:

            hashedPassword = user.Password
            logging.info("User login info successful retrieved")

        else:
            logging.error("User does not exist")
            print("\n\n-----------------------------------------\n|Looks like the login failed, try again!|\n-----------------------------------------")
            login()

    except Exception as e:
        logging.exception("Unable to retreive user login info during login")
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
    temp_user = User.fetch(Username = Username)
    
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

    print("\nTIME TO LOGIN\n")    
    

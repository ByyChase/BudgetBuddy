import bcrypt, getpass
from Models.User import User



#Declare Global Variables
GlobalUser = None


def Login():


    Username = input("\n\nPlease input your username: ")

    Username = Username.upper()

    if Username == "NEW":
        createNewUser()
        Login()


    Password = getpass.getpass()
    
    
    user = User(Username = Username)
    
    user = user.fetch()
    
    hashedPassword = user.Password
    
    print(hashedPassword)

    if bcrypt.checkpw(Password.encode('utf-8'), hashedPassword):
        print('Allow Login')
        return
        
        
    
    else:
        exit()
        


def createNewUser():

    print("\n\nWelcome to BudgetBuddy!\nBelow we will get you setup with a new account!")

    Username = input("\n\nPlease input a Username: ")

    #Check to see if username exists

    First_Name = input("\nPlease input your first name: ")

    Last_Name = input("\nPlease input your last name: ")

    Password = input("\nPlease input a password: ")

    Password2 = input("\nPlease re-input your password: ")

    #Check user input

    if Password == Password2:

        salt = bcrypt.gensalt()
        CryptPassword =  bcrypt.hashpw(Password.encode('utf-8'), salt)
        print(CryptPassword)
  
        NewUser = User(Username = Username.upper(), First_Name = First_Name.upper(), Last_Name = Last_Name.upper(), Password = CryptPassword)
        print(NewUser.Username)

        tempUser = NewUser.New_User()



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
    
    user.fetch()

    if bcrypt.checkpw(Password.encode('utf8'), user.fetch(Username1 = Username).Password):
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

        CryptPassword = bcrypt.hashpw(Password.encode('utf8'), bcrypt.gensalt())
  
        NewUser = User(Username = Username, First_Name = First_Name, Last_Name = Last_Name, Password = CryptPassword)

        tempUser = NewUser.New_User(Password)



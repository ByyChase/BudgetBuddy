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

    if bcrypt.checkpw(Password.encode('utf-8'), hashedPassword):
        print('Allow Login')
        return
        
    else:
        exit()
        


def createNewUser():

    print("\n\nWelcome to BudgetBuddy!\nBelow we will get you setup with a new account!")

    Username = input("\n\nPlease input a Username: ")
    Username = Username.upper()
    temp_user = User(Username = Username)
    temp_user = temp_user.fetch()
    
    while temp_user != "User Not Found":
        
        Username = input("\n\nPlease input a Username: ")
        temp_user = User(Username = Username)
        temp_user = temp_user.fetch()
        

    First_Name = input("\nPlease input your first name: ")
    First_Name = First_Name.upper()
    First_Name = First_Name.strip()
    
    Last_Name = input("\nPlease input your last name: ")
    Last_Name = Last_Name.upper()
    Last_Name = Last_Name.strip()
    
    Password = input("\nPlease input a password: ")
    Password2 = input("\nPlease re-input your password: ")

    #Check user input

    if Password == Password2:

        salt = bcrypt.gensalt()
        CryptPassword =  bcrypt.hashpw(Password.encode('utf-8'), salt)
        NewUser = User(Username = Username.upper(), First_Name = First_Name.upper(), Last_Name = Last_Name.upper(), Password = CryptPassword)
        tempUser = NewUser.New_User()



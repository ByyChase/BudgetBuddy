import bcrypt, getpass
from Models.User import User



#Declare Global Variables
GlobalUser = None


def Login():


    Username = input("\n\nPlease input your username: ")

    Username = Username.upper()

    if Username == "NEW":
        createNewUser()

    else: 
        print(getUser(Username))
        Password = getpass.getpass()


    #if bcrypt.checkpw(Password, User.fetch(UserName = UserName).Password):
        #Allow login 
        #User = 
        #pass
    
    #else:
        #Don't allow login
        #pass







def getUser(Username):
    return User.fetch(Username = Username)

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
  
        NewUser = User(UserName = Username, First_Name = First_Name, Last_Name = Last_Name)

        tempUser = NewUser.New_Employee(Password)



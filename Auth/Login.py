import bcrypt
from Models.User import User



#Declare Global Variables 
User = None


def Login():


    UserName = input("\n\nPlease input your username: ")

    Password = input("\nPlease input your password: ")

    #if bcrypt.checkpw(Password, User.fetch(UserName = UserName).Password):
        #Allow login 
        #User = 
        #pass
    
    #else:
        #Don't allow login
        #pass







#def getUser():
    #return User.fetch(User_ID = User_ID)

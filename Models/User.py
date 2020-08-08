from Models.CreateDatabase import cursor

class User:

    def __init__(self, Username=None, First_Name=None, Last_Name=None, Password=None, User_ID=None):
        self.Username = Username       #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name     #String
        self.User_ID = User_ID         #Integer

    def fetch(self, Username):
        statement = "SELECT Username, First_Name, Last_Name, User_ID FROM USER WHERE USERNAME = ?"
        return cursor().execute(statement, (Username))

    def New_Employee(self, Password): 
        statement = "INSERT INTO USER (Username, First_Name, Last_Name, Password) VALUES (?, ?, ?, ?)"
        return cursor().execute(statement, (Username, First_Name, Last_Name, Password))
        




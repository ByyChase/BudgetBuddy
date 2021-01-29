from Models.CreateDatabase import cursor
from Models.CreateDatabase import commit
from Models.CreateDatabase import dict_factory

class User:

    def __init__(self, Username=None, First_Name=None, Last_Name=None, Password=None, User_ID=None):
        self.Username = Username       #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name     #String
        self.User_ID = User_ID         #Integer
        self.Password = Password

    def fetch(self):
        TempCursor = cursor()
        print(self.Username)
        statement = "SELECT Username, First_Name, Last_Name, User_ID, Password FROM USER WHERE USERNAME = ?"
        TempCursor.execute(statement, (self.Username,))
        
        Temp_SQL_Data = TempCursor.fetchone()
        
        Return_User = User(Username = Temp_SQL_Data[0], First_Name = Temp_SQL_Data[1], Last_Name = Temp_SQL_Data[2], User_ID = Temp_SQL_Data[3], Password = Temp_SQL_Data[4])
        
        return Return_User

    def New_User(self): 
        statement = "INSERT INTO USER (Username, First_Name, Last_Name, Password) VALUES (?, ?, ?, ?)"
        
        print(statement)
        cursor().execute(statement, (self.Username, self.First_Name, self.Last_Name, self.Password,))
        commit()

from Models.CreateDatabase import cursor
from Models.CreateDatabase import commit
from Models.CreateDatabase import dict_factory

class User:

    def __init__(self, Username=None, First_Name=None, Last_Name=None, Password=None, User_ID=None):
        
        self.Username = Username       #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name     #String
        self.User_ID = User_ID         #Integer
        self.Password = Password       #String
        
    db_fetch = "SELECT * FROM USER WHERE "

    def fetch(**KWARGS):
        
        elements = []
        db_fetch = User.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)
            
        Temp_SQL_Data = cursor().execute(db_fetch, (elements)).fetchone()
            
        if Temp_SQL_Data:
            return User(Username = Temp_SQL_Data[0], First_Name = Temp_SQL_Data[1], Last_Name = Temp_SQL_Data[2], User_ID = Temp_SQL_Data[4], Password = Temp_SQL_Data[3])
        else:
            return "User Not Found"
        

    def New_User(self): 
        
        statement = "INSERT INTO USER (Username, First_Name, Last_Name, Password) VALUES (?, ?, ?, ?)"
        cursor().execute(statement, (self.Username, self.First_Name, self.Last_Name, self.Password,))
        commit()
        
        

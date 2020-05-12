class User:

    def User(self, Username=None, First_Name=None, Last_Name=None, Password=None, User_ID=None):
        self.Username = Username       #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name     #String
        self.Password = Password       #Hashed String (BCrypt)
        self.User_ID = User_ID         #Integer



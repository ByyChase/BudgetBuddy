class User:

    def User(self, Username, First_Name, Last_Name, Password, User_ID):
        self.Username = Username   #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name   #String
        self.Password = Password   #Hashed String (BCrypt)
        self.User_ID = User_ID   #Integer



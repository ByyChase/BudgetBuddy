from Models.LoadDatabase import cursor
from Models.LoadDatabase import commit
from Models.LoadDatabase import dict_factory

class User:

    """
    A class used to represent a User 

    ...

    Attributes
    ----------
    Username : str
        A string representing the username the user selects. This is not case sensative as it is put into all upper
        case when being put into the database 
    First_Name : str
        A string representing the first name of the user. This is not case sensative as it is all capitolized 
        when being put into the database.
    User_ID : int
        A unique ID used to identify the user in the database. This is the primary key of the user.
    Password : str
        This string is the users password. The password is hashed by bcrypt before being put in so it is 
        not stored in plain text. It will require Bcrypt to compare the entered password and stored
        password at login.  
    """ 


    def __init__(self, Username=None, First_Name=None, Last_Name=None, Password=None, User_ID=None):

        """

        Parameters
        ----------
        Username : str
            A string representing the username the user selects. This is not case sensative as it is put into all upper
            case when being put into the database 
        First_Name : str
            A string representing the first name of the user. This is not case sensative as it is all capitolized 
            when being put into the database.
        User_ID : int
            A unique ID used to identify the user in the database. This is the primary key of the user.
        Password : str
            This string is the users password. The password is hashed by bcrypt before being put in so it is 
            not stored in plain text. It will require Bcrypt to compare the entered password and stored
            password at login.  
        """ 

        
        self.Username = Username       #String  
        self.First_Name = First_Name   #String
        self.Last_Name = Last_Name     #String
        self.User_ID = User_ID         #Integer
        self.Password = Password       #String
        
    db_fetch = "SELECT * FROM USER WHERE "

    def fetch(**KWARGS):

        """
        This method is used to fetch Users objects from the database.


        Parameters
        ----------
        Username : str
            A string representing the username the user selects. This is not case sensative as it is put into all upper
            case when being put into the database 
        First_Name : str
            A string representing the first name of the user. This is not case sensative as it is all capitolized 
            when being put into the database.
        User_ID : int
            A unique ID used to identify the user in the database. This is the primary key of the user.
        Password : str
            This string is the users password. The password is hashed by bcrypt before being put in so it is 
            not stored in plain text. It will require Bcrypt to compare the entered password and stored
            password at login.  
        """ 
        
        elements = []
        db_fetch = User.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)
            
        temp_SQL_data = cursor().execute(db_fetch, (elements)).fetchone()
            
        if temp_SQL_data:
            return User(Username = temp_SQL_data[0], First_Name = temp_SQL_data[1], Last_Name = temp_SQL_data[2], User_ID = temp_SQL_data[4], Password = temp_SQL_data[3])
        else:
            return "User Not Found"
        

    def commit_user(self): 

        """
        This method is used to input a new User into the database.


        Parameters
        ----------
        self : IncomeStatement Object 
            A fully created/populated User object
        """ 
        
        statement = "INSERT INTO USER (Username, First_Name, Last_Name, Password) VALUES (?, ?, ?, ?)"
        cursor().execute(statement, (self.Username, self.First_Name, self.Last_Name, self.Password,))
        commit()

        
        
        

from Models.LoadDatabase import cursor
from Models.LoadDatabase import commit
import datetime, logging
from money import Money

class BankAccount:
    """
    A class used to represent a Bank Account. This will hold users money and allow them to
    attribute certain incomes, expenses, and budgets towards them.
    
    ...
    
    Attributes
    ----------
    Name : str
        This variable holds a user entered value to describe and identify the name of the bank account  
    Description : str
        This variables holds a user entered value to describe and identify their bank account
    Amount : float 
        This variable holds the the amount of money inside of the bank account
    Account_ID : int
        This is a unique value given by the database to identify the account. This is the primary 
        key of the object 
    User_ID : int
        This is the unique value of the user that the account belongs to 
    """

    def __init__(self, Name=None, Description=None, Amount=None, Account_ID=None, User_ID=None):
        """
        Parameters
        ----------
        Name : str
            This variable holds a user entered value to describe and identify the name of the bank account  
        Description : str
            This variables holds a user entered value to describe and identify their bank account
        Amount : float 
            This variable holds the the amount of money inside of the bank account
        Account_ID : int
            This is a unique value given by the database to identify the account. This is the primary 
            key of the object 
        User_ID : int
            This is the unique value of the user that the account belongs to 
        """

        self.Name = Name                 #String
        self.Description = Description   #String
        self.Amount = Amount             #float
        self.Account_ID = Account_ID     #Integer
        self.User_ID = User_ID           #Integer

    db_fetch = "SELECT * FROM BANKACCOUNT WHERE "

    def fetch(**KWARGS):
        """
        This method is used to fetch BankAccount objects from the database. It will mainly 
        be used with the User_ID being what is searched on or the BankAccount_ID. It can accept 
        any of the parameters from the BankAccount class though for searching functionality. 

        ...

        Parameters
        ----------
        Name : str
            This variable holds a user entered value to describe and identify the name of the bank account  
        Description : str
            This variables holds a user entered value to describe and identify their bank account
        Amount : float 
            This variable holds the the amount of money inside of the bank account
        Account_ID : int
            This is a unique value given by the database to identify the account. This is the primary 
            key of the object 
        User_ID : int
            This is the unique value of the user that the account belongs to 

        ...

        Returns
        -------
        temp_bank_account_object: BankAccount Object
            This is returned if the fetch was successful in finding the requested 
            object in the database 
        
        --or--

        0 : int
            This is returned if the object was not found in the database
        """

        #I have no idea what this stuff does, it was written by a classmate for 
        # another class project we worked on together
        elements = []
        db_fetch = BankAccount.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)

        #Pulling data from database for an Income Statement 
        temp_SQL_data = cursor().execute(db_fetch, (elements)).fetchone()

        #If something was able to be found it will return an IncomeStatement object 
        if temp_SQL_data:

            temp_bank_account_object = BankAccount()
            return temp_bank_account_object

        #If nothing was found a 0 will be returned
        else:
            return 0

    def commit_bank_accout(self): 
        """
        This method is used to input a new BankAccount into the database.

        ...

        Parameters
        ----------
        self : BankAccount Object 
            A fully created/populated BankAccount Object
        """ 

        statement = "INSERT INTO BANKACCOUNT (Name, Amount, Description, Account_ID, User_ID) VALUES (?, ?, ?, ?, ?)"
        cursor().execute(statement, (self.Name, self.Amount, self.Description, self.Account_ID, self.User_ID))
        commit()

    def create_bank_account(user):
        """
        This method will be used to walk the user through creating a new bank account. 

        ...

        Parameters
        ----------
        user : Fully initialized User object 
            This will be used to get the User_ID 
        """

        print("\n\n-------------------------------\n|Lets Make a New Bank Account!|\n-------------------------------")

        name = input("\n\nPlease enter the name you would like to call this account!\n\n*DISCLAIMER*: This will be the main way you identify this account, please chose the name wisly!\n\nYour Input: ")

        while name == "" or name.strip() == "":
            name = input("\n\nA blank input is not allowed for this value, Please enter an account name!\n\n*DISCLAIMER*: This will be the main way you identify this account, please chose the name wisly!\n\nYour Input: ")

        description = input("\n\nPlease enter a description for this account!\n\n*DISCLAIMER*: This will be one of the main ways you identify this account, please describe it well!\n\nYour Input: ")

        while description == "" or description.strip() == "":
            description = input("\n\nA blank input is not accepted, please input a description for the account!\n\n*DISCLAIMER*: This will be one of the main ways you identify this account, please describe it well!\n\nYour Input: ")








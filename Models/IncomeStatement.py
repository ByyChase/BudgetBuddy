from Models.LoadDatabase import cursor
from Models.LoadDatabase import commit
from Models.LoadDatabase import dict_factory
import datetime
from money import Money


class IncomeStatement:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    Date : str
        a date time object formated as a string to store in the data base
    Amount : float
        A float used to store the initial amount of the income statement
    Description : str
        The user inputed description of the income statement 
    IncomeStatement_ID : int
        the unique identifier and primary key of the income statement 
    UnBudgeted : float   
        the amount of money in the income statement that has not been put towards 
        a budget 
    User_ID : int
        The unique identifier of the user that owns the income statement
    """  


    def __init__(self, Date=None, Amount=None, Description=None, IncomeStatement_ID=None, UnBudgeted=None, User_ID=None):
        """
        Parameters
        ----------
        Date : str
            a date time object formated as a string to store in the data base
        Amount : float
            A float used to store the initial amount of the income statement
        Description : str
            The user inputed description of the income statement 
        IncomeStatement_ID : int
            the unique identifier and primary key of the income statement 
        UnBudgeted : float   
            the amount of money in the income statement that has not been put towards 
            a budget 
        User_ID : int
            The unique identifier of the user that owns the income statement        
        """  
        
        self.Date = Date                                #String
        self.Amount = Amount                            #Double
        self.Description = Description                  #String
        self.IncomeStatement_ID = IncomeStatement_ID    #Integer
        self.UnBudgeted = UnBudgeted                    #Double
        self.User_ID = User_ID                          #Integer

    db_fetch = "SELECT * FROM INCOMESTATEMENT WHERE "

    def fetch(**KWARGS):
        """
        This method is used to fetch IncomeStatement objects from the database.
        In all reality this method requires the User_ID to be passed in to work well.
        But to be safe and to cover all of the options I may need to look up different
        types of look ups.

        ...

        Parameters
        ----------
        Date : str
            a date time object formated as a string to store in the data base
        Amount : float
            A float used to store the initial amount of the income statement
        Description : str
            The user inputed description of the income statement 
        IncomeStatement_ID : int
            the unique identifier and primary key of the income statement 
        UnBudgeted : float   
            the amount of money in the income statement that has not been put towards 
            a budget 
        User_ID : int
            The unique identifier of the user that owns the income statement

        ...

        Returns
        -------
        temp_income_statement_object: IncomeStatement Object
            This is returned if the fetch was successful in finding the requested 
            object in the database 
        
        --or--

        0 : int
            This is returned if the object was not found in the database
        """ 
        
        #I have no idea what this stuff does, it was written by a classmate for 
        # another class project we worked on together
        elements = []
        db_fetch = IncomeStatement.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)

        #Pulling data from database for an Income Statement   
        temp_SQL_data = cursor().execute(db_fetch, (elements)).fetchone()
            
        #If something was able to be found it will return an IncomeStatement object 
        if temp_SQL_data:
            temp_income_statement_object = IncomeStatement(Date = temp_SQL_data[0], Amount = temp_SQL_data[1], UnBudgeted = temp_SQL_data[2], Description = temp_SQL_data[3], IncomeStatement_ID = temp_SQL_data[4], User_ID = temp_SQL_data[5])
            return temp_income_statement_object
        #If nothing was found a 0 will be returned
        else:
            return 0
        

    def get_users_statements(user):
        """
        This method is used to retreive all of the IncomeStatement IDs from the database for a particular user 
        and then returns a list of IncomeStatement objects that belong to the user

        ...

        Parameters
        ----------
        user: User Object
            This is a user object mainly used to get the User_ID from the user

        ...

        Returns
        -------
        income_statements : List of IncomeStatement Objects 
            this is returned if the database call was successful in finding any IncomeStatements for the User_ID provided

        --or--

        0 : int
            This is returned if no data was able to be found or if something went wrong
        """ 

        #SQL statement for the database call 
        statement = "SELECT * FROM INCOMESTATEMENT WHERE User_ID = ?"
        #Call to the database 
        rows = cursor().execute(statement, (user.User_ID,)).fetchall()
        #Checking to see if data was returned from the database. If it is the data will be parsed and returned in a list 
        #of IncomeStatement objects. If nothing is found 0 is returned
        if rows:
            income_statements = []
            for x in rows:
                temp_IncomeStatement = IncomeStatement(Date = x[0], Amount = x[1], UnBudgeted = x[2], Description = x[3], IncomeStatement_ID = x[4], User_ID = x[5])
                income_statements.append(temp_IncomeStatement)
            
            return income_statements

        else:
            return 0

           
    def commit_incomestatement(self): 
        
        """
        This method is used to input a new IncomeStatement into the database.

        ...

        Parameters
        ----------
        self : IncomeStatement Object 
            A fully created/populated income statement object

        """ 

        statement = "INSERT INTO INCOMESTATEMENT (Date, Amount, UnBudgeted, Description, User_ID) VALUES (?, ?, ?, ?, ?)"
        cursor().execute(statement, (self.Date, self.Amount, self.UnBudgeted, self.Description, self.User_ID))
        commit()

        
    def create(user):

        """
        This method is used to walk a user through inputting the info needed to create 
        an income statement 

        ...

        Parameters
        ----------
        user : User Object 
            A fully created/populated user object. This is gotten and passed from the Auth.Login file.
            This is mainly needed for the User_ID to tie the income statement to the user

        """ 

        
        #Asking the user for their input for the date of their income
        Date = input("\nPlease input the date you received the income (Please use the MM/DD/YYYY format): ")
        GoodDate = False
        
        #Trying to turn the date the user put in into a date time object 
        #If it works then GoodDate is set to True and the program won't fall into the while 
        #loop below for checking user data
        try:
            Date = datetime.datetime.strptime(Date,'%m/%d/%Y')
            GoodDate = True
            print(Date)

        #This is just here so the try command doesn't yell at me    
        except:
            pass
        
        #If the date entered by the user wasn't able to be put into a date time object this loop will run 
        #It will run the same code above but will keep running until the object is able to be created 
        #by the users input
        while GoodDate == False:
            Date = input("\nPlease input the date using the correct formatting (Please use the MM/DD/YYYY format)\n\nInput: ")

            try:
                Date = datetime.datetime.strptime(Date,'%m/%d/%Y')
                GoodDate = True

            except:
                pass

        #Asking the user to enter in the money amount of their income statement
        Amount = input("\nPlease input the amount of the income (Please use standard money input)\n\nInput: $")
        GoodMoney = False

        #This will try to format the input into the ##.## format. If it can not format it into a two decimal format then it will fail
        #and will run the accept statement bwloe
        try: 
            Amount = "{:.2f}".format(float(Amount))
            GoodMoney = True
        
        #This will only run if the amount the user input wasn't able to be formated correctly 
        except Exception as e:
            #This loop will run until the input of the user is able to be formated correctly for storage
            while GoodMoney == False: 
                Amount = input("\nThat format didn't work, please try again (Please use standard money input without commas)\n\nInput: $")
                
                try: 
                    Amount = "{:.2f}".format(float(Amount))
                    GoodMoney = True

                except Exception as e:
                    print(e)

        #Asking the user to input a description for their paycheck. This is one of the key ways that users will use determine what the paycheck is       
        Description = input("\nPlease enter a short description of the income.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")

        #creation of the new income statement
        Temp_IncomeStatement = IncomeStatement(Date = str(Date), Amount = float(Amount), UnBudgeted = float(Amount), Description = Description, User_ID = user.User_ID).commit_incomestatement()   
        
        #printing the income statement out to the user
        print("\n\nHere is your statement:\n")
        print("Date: " + IncomeStatement.format_date(Date) + "\nDescription: " + Description + "\nAmount: $" + Amount + "\n\n")
        
    
    def format_date(date):

        """
        This method is used to convert a Date Time Object into a MM/DD/YYYY formated string. This 
        is really only ever used to convert the info for output purposes. This may get moved to 
        another file if it gets used for multiple other classes, or it may just stay here.

        ...

        Parameters
        ----------
        Date : DateTime Object 
            A date time object that stores the date a user received an income

        ... 

        Returns
        -------
        Date : str
            A string that is used to print out to the user in a readable format. The format is MM/DD/YYYY

        --or--

        0 : int
            This is returned if something went wrong with the date conversion

        """
        try:

            date_split_from_DateTime_object = str(Date.date()).split(' ')
            date = date_split_from_DateTime_object[0].split('-')
            date = date[1] + "/" + date[2] + "/" + date[0]
        
        except:
            pass

        if date:
            return date

        else:
            return 0


    

        

    
    
        
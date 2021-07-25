from Models.LoadDatabase import cursor
from Models.LoadDatabase import commit
from Models.IncomeStatement import IncomeStatement
import datetime, logging
from money import Money

class Budget:
    """
    A class used to represent a budget item. This will hold an amount of money that is spent on a specific item
    or put aside for something specific. All money in budgets will be able to be tracked back to an 
    income statement. 

    ...

    Attributes
    ----------
    Name : str
        This variable stores the name given to the budget by the user 
    Amount : float
        This variables stores the amount given to the budget by the user 
    UnSpent : float
        The amount that has not been spent from the budget 
    Description : str
        Description given to the budget by the user
    IncomeStatement_ID : int
        Foreign Key to the owning IncomeStatement 
    Budget_ID : int
        Primary Key to indentify the budget object 
    User_ID : int
        Foreign Key to the owning User
    """

    def __init__(self, Name=None, Amount=None, UnSpent=None, Description=None, Paycheck_ID=None, Budget_ID=None):
        """
        Parameters
        ----------
        Name : str
            This variable stores the name given to the budget by the user 
        Amount : float
            This variables stores the amount given to the budget by the user 
        UnSpent : float
            The amount that has not been spent from the budget 
        Description : str
            Description given to the budget by the user
        IncomeStatement_ID : int
            Foreign Key to the owning IncomeStatement 
        Budget_ID : int
            Primary Key to indentify the budget object 
        User_ID : int
            Foreign Key to the owning User
        """

        self.Name = Name                                #String
        self.Amount = Amount                            #Double    
        self.UnSpent = UnSpent                          #Double  
        self.Description = Description                  #String 
        self.IncomeStatement_ID = IncomeStatement_ID    #Integer
        self.Budget_ID = Budget_ID                      #Integer
        self.User_ID = User_ID                          #Integer

    db_fetch = "SELECT * FROM BUDGET WHERE "

    def fetch(self, **KWARGS):
        """
        This method is used to fetch Budget objects from the database. It will mainly 
        be used with the User_ID being what is searched on or the Budget_ID. It can accept 
        any of the parameters from the Budget class though for searching functionality. 

        ...

        Parameters
        ----------
        Name : str
            This variable stores the name given to the budget by the user 
        Amount : float
            This variables stores the amount given to the budget by the user 
        UnSpent : float
            The amount that has not been spent from the budget 
        Description : str
            Description given to the budget by the user
        IncomeStatement_ID : int
            Foreign Key to the owning IncomeStatement 
        Budget_ID : int
            Primary Key to indentify the budget object 
        User_ID : int
            Foreign Key to the owning User

        ...

        Returns
        -------
        temp_budget_object: Budget Object
            This is returned if the fetch was successful in finding the requested 
            object in the database 
        
        --or--

        0 : int
            This is returned if the object was not found in the database
        """

        #I have no idea what this stuff does, it was written by a classmate for 
        # another class project we worked on together
        elements = []
        db_fetch = Budget.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)

        #Pulling data from database for an Income Statement 
        temp_SQL_data = cursor().execute(db_fetch, (elements)).fetchone()

        #If something was able to be found it will return an IncomeStatement object 
        if temp_SQL_data:

            temp_bank_account_object = Budget(Name = temp_SQL_data[0], Amount = temp_SQL_data[1], UnSpent = temp_SQL_data[2], Description = temp_SQL_data[3], IncomeStatement_ID = temp_SQL_data[4], Budget_ID = temp_SQL_data[5], User_ID = temp_SQL_data[6])
            return temp_bank_account_object

        #If nothing was found a 0 will be returned
        else:
            return 0


    def commit_budgets(self):
        """
        This method is used to input a new Budget into the database.

        ...

        Parameters
        ----------
        self : Budget Object 
            A fully created/populated Budget Object
        """

        statement = "INSERT INTO BUDGET (Name, Amount, UnSpent, Description, IncomeStatement_ID, Budget_ID, User_ID) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor().execute(statement, (self.Name, self.Amount, self.UnSpent, self.Description, self.IncomeStatement_ID, self.Budget_ID, self.User_ID))
        commit()

    def create_users_budgets(self):
        """
        This method is used to walk a user through creating a new Budget
        
        ...

        Parameters
        ----------
        self : Budget object
            An empty budget object
        """


    def get_users_budgets(self, user, income_statement_id = None):
        """
        This method is used to retreive all of the Budgets from the database for a particular user 
        and then returns a list of Budget objects that belong to the user

        ...

        Parameters
        ----------
        user: User Object
            This is a user object mainly used to get the User_ID from the user

        ...

        Returns
        -------
        budget_object : List of BankAccount Objects 
            this is returned if the database call was successful in finding any BankAccounts for the User_ID provided

        --or--

        0 : int
            This is returned if no data was able to be found or if something went wrong
        """     

        if income_statement_id == None:

            #SQL statement for the database call 
            statement = "SELECT * FROM BUDGET WHERE User_ID = ?"
            #Call to the database 
            rows = cursor().execute(statement, (user.User_ID,)).fetchall()
            #Checking to see if data was returned from the database. If it is the data will be parsed and returned in a list 
            #of Budget objects. If nothing is found 0 is returned
            if rows:

                budget_objects = []

                for x in rows:

                    temp_budget = Budget(Name = x[0], Amount = x[1], UnSpent = x[2], Description = x[3], IncomeStatement_ID = x[4], Budget_ID = x[5], User_ID = x[6])
                    budget_objects.append(temp_budget)
                
                return budget_objects

            else:
                return 0

        elif income_statement_id:

            #SQL statement for the database call 
            statement = "SELECT * FROM BUDGET WHERE IncomeStatement_ID = ?"
            #Call to the database 
            rows = cursor().execute(statement, (income_statement_id,)).fetchall()
            #Checking to see if data was returned from the database. If it is the data will be parsed and returned in a list 
            #of Budget objects. If nothing is found 0 is returned
            if rows:

                budget_objects = []

                for x in rows:

                    temp_budget = Budget(Name = x[0], Amount = x[1], UnSpent = x[2], Description = x[3], IncomeStatement_ID = x[4], Budget_ID = x[5], User_ID = x[6])
                    budget_objects.append(temp_budget)
                
                return budget_objects

            else:
                return 0



    def view_user_budgets(self, user, list_all_budgets = None):

        print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
        user_view_budgets_choice = input("\nHow would you like to view your budgets? \n\n1)All Budgets \n2)Budgets for a Specific Income Statement \n\nYour Input: ")
        user_view_budgets_choice = user_view_budgets_choice.strip()

        while user_view_budgets_choice == '' or user_view_budgets_choice != "1" and user_view_budgets_choice != "2":

            user_view_budgets_choice = input("\n\n**INVALID INPUT**\n\nHow would you like to view your budgets? \n\n1)All Budgets \n2)Budgets for a Specific Income Statement \n\nYour Input: ")

        user_budgets = Budget.get_users_budgets(user)

        if user_budgets == 0:

            print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
            print("It looks like you don't have any budgets yet\n")
            return


        if user_view_budgets_choice == '1':

            print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
            print('Here are your Budgets: ')

            count = 1

            for x in user_budgets:
                print('Budget #' + str(count))
                print('Name: ' + x.Name)
                print('Description: ' + x.Description)
                print('Amount: $' + x.Amount)
                print('UnSpent: $' + x.UnSpent)

                count += 1
                print('----------------------------------------------------------------------------------------------\n')    
            

        elif user_view_budgets_choice == '2':

            print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
            

            income_statement_number = 1

            user_income_statements = IncomeStatement.get_users_statements(user)

            if user_income_statements == 0:

                print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
                print("Looks like you dont have any Income Statements yet!\n\n")
                return

            print("\nHere are your Income Statements: \n\n")
            print("\n--------------------------------------------------------------------------\n")

            for x in user_income_statements:

                print("Budgets for Income Statement #" + str(income_statement_number))
                print("Income Statement Description: " + x.Description)
                print("Income Statement Date: " + x.Date)
                print("Income Statement Amount: " + str(x.Amount))
                print("\n--------------------------------------------------------------------------\n")
                
                income_statement_number += 1


            user_choice_view_budgets = input("\nPlease select which Income Statement's budgets you would like to look at!\n\nYour Input: ")

            user_choice_view_budgets = user_choice_view_budgets.strip()
            


                








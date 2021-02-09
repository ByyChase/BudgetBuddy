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


    def view_user_statements(user):
        """
        This method is used to output user Incomestatements to the command line

        ...

        Parameters
        ----------
        user: User Object
            This is a user object mainly used to get the User_ID from the user'

        show_ouput : literally anything toq
            
        ...
        
        Returns
        -------
        user_statements : List of IncomeStatements
            This return is only used for the edit_user_statement function. 
        """

        user_statements = IncomeStatement.get_users_statements(user)
        print("\n\n----------------------------------------------------------\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n----------------------------------------------------------\n\n")
        print("Here are your statements: \n")
        count = 1

        for x in user_statements:
            print("\nStatement " + str(count) + ":")
            print("Date: " + str(x.Date))
            print("Description: " + str(x.Description))
            print("Amount: $" + str(x.Amount))
            print("Unbudgeted: $" + str(x.UnBudgeted))
            count += 1

        input("\nPlease hit enter when you would like to continue....")
        return user_statements
    
        
    def edit_user_statements(user, edit_single_statement = None):
        """
        This method is used to edit user IncomeStatement. If the user edits an IncomeStatement's amount, any Budget that is associated 
        with the IncomeStatement will need to be reallocated. 

        ...

        Parameters
        ----------
        user : User Object 
            A fully created/populated user object. This is gotten and passed from the Auth.Login file.
            This is mainly needed for the User_ID to tie the income statement to the user

        edit_single_statement : int
            This parmeter is used only if the last entry to the database needs changed. THis will not give the user the option to edit all their 
            statements. The standard value is None, if it is set to anything else it will only allow editing on the last IncomeStatement Entry
        """ 

        user_still_editing_income_statements = True

        if edit_single_statement == None:

            user_statements = IncomeStatement.view_user_statements(user)
        
        else:

            print("Only One Edit")
            user_statements = IncomeStatement.get_users_statements(user)


        def edit_incomestatement_instance(user_selected_statement):
            
            user_still_editing_selected_income_statement = True

            while user_still_editing_selected_income_statement:
                #Printing the Income Statement the user is editng 
                print("\n-----------------------\n|Income Statement Info|\n-----------------------")
                print("\n\nDate: " + str(user_statements[user_selected_statement].Date))
                print("Description: " + str(user_statements[user_selected_statement].Description))
                print("Amount: $" + str(user_statements[user_selected_statement].Amount))

                user_edit_choice = input("\nPlease enter the number of what you would like to enter: \n\n1)Date\n2)Description\n3)Amount\n4)Done Editing\n\nYour Input: ")

                while user_edit_choice == "":
                    user_edit_choice = input("\nPlease enter one of the valid options: \n\n1)Date\n2)Description\n3)Amount\n4)Done Editing\n\nYour Input: ")

                user_edit_choice = int(user_edit_choice)

                if user_edit_choice == 4:

                    user_still_editing_selected_income_statement = False
                    statement = "UPDATE INCOMESTATEMENT SET Date = ?, Amount = ?, Description = ?, IncomeStatement_ID = ?, UnBudgeted = ?, User_ID = ? WHERE  IncomeStatement_ID = ?"
                    cursor().execute(statement, (user_statements[user_selected_statement].Date, user_statements[user_selected_statement].Amount, user_statements[user_selected_statement].Description, user_statements[user_selected_statement].IncomeStatement_ID, user_statements[user_selected_statement].UnBudgeted, user_statements[user_selected_statement].User_ID, user_statements[user_selected_statement].IncomeStatement_ID,))
                    commit()

                    #TODO : When the user edits an IncomeStatement, all of the budgets associated with the income statement have to be edited as well so money that doesn't
                    # exist for the user is not sitting inside of budgets 

                elif user_edit_choice == 1:
                    #Asking the user for their input for the date of their income
                    print("\n----------------------------------------------------------\n")
                    date = input("\nPlease input the new date you received the income (Please use the MM/DD/YYYY format): ")
                    gooddate = False
                    
                    #Trying to turn the date the user put in into a date time object 
                    #If it works then GoodDate is set to True and the program won't fall into the while 
                    #loop below for checking user dataBud
                    try:
                        date = datetime.datetime.strptime(date,'%m/%d/%Y')
                        gooddate = True
                        
                    #This is just here so the try command doesn't yell at me    
                    except:
                        pass
                    
                    #If the date entered by the user wasn't able to be put into a date time object this loop will run 
                    #It will run the same code above but will keep running until the object is able to be created 
                    #by the users input
                    while gooddate == False:
                        print("\n----------------------------------------------------------\n")
                        date = input("\nPlease input the date using the correct formatting (Please use the MM/DD/YYYY format)\n\nInput: ")

                        try:
                            date = datetime.datetime.strptime(date,'%m/%d/%Y')
                            gooddate = True

                        except:
                            pass

                    user_statements[user_selected_statement].Date = date

                elif user_edit_choice == 2:
                    #Asking the user to input a description for their paycheck. This is one of the key ways that users will use determine what the paycheck is
                    # print("\n----------------------------------------------------------\n")       
                    description = input("\nPlease enter a short description of the income.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")
                    
                    while description == "":
                        print("\n----------------------------------------------------------\n")
                        description = input("\nPlease enter something, an empty input is not allowed.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")

                    user_statements[user_selected_statement].Description = description

                elif user_edit_choice == 3:
                    #Asking the user to enter in the money amount of their income statement
                    print("\n----------------------------------------------------------\n")
                    amount = input("\nPlease input the amount of the income (Please use standard money input)\n\nInput: $")
                    goodmoney = False

                    #This will try to format the input into the ##.## format. If it can not format it into a two decimal format then it will fail
                    #and will run the accept statement bwloe
                    try: 
                        amount = "{:.2f}".format(float(amount))
                        goodmoney = True
                        change_income = True
                    
                    #This will only run if the amount the user input wasn't able to be formated correctly 
                    except Exception as e:

                        #This loop will run until the input of the user is able to be formated correctly for storage
                        while goodmoney == False:
                            print("\n----------------------------------------------------------\n")
                            amount = input("\nThat format didn't work, please try again (Please use standard money input without commas)\n\nInput: $")
                            
                            try: 
                                amount = "{:.2f}".format(float(amount))
                                goodmoney = True
                                change_income = True

                            except Exception as e:
                                print(e)

                    user_statements[user_selected_statement].Amount = amount
                    user_statements[user_selected_statement].UnBudgeted = amount

        user_still_editing_income_statements = True

        if edit_single_statement != None:
            edit_incomestatement_instance(len(user_statements) -1)
            return
        
        #This while loop allows users to edit multiple Income Statements 
        while user_still_editing_income_statements:

            #This variable is used to determine if the user changed the money amount in a statement
            #If it is set to true the user will have to edit all the budgets related to the income statement
            change_income = False
            #Asking for user input
            user_selected_statement = input("\nPlease enter the statement number you would like to edit (Enter 0 to return to the previous menu): \n\nYour Input: ")

            #User input validation. If its a space it just re prints the output
            while user_selected_statement == "":
                user_selected_statement = input("\nPlease enter one of the valid options (Enter 0 to return to the previous menu): \n\nYour Input: ")

            user_selected_statement = int(user_selected_statement)
        
            #User input validation
            while user_selected_statement < 0 or user_selected_statement > len(user_statements):
                user_selected_statement = input("\nSorry, that input wasn't a statement above, please enter another. \n\nYour Input: ")
            #If you enter zero the program resturns to the previous menu
            if user_selected_statement == 0:
                return
            
            user_selected_statement =-1
            edit_incomestatement_instance(user_selected_statement)
            count = 1

            for x in user_statements:
                print("\nStatement " + str(count) + ":")
                print("Date: " + str(x.Date))
                print("Description: " + str(x.Description))
                print("Amount: $" + str(x.Amount))
                print("Unbudgeted: $" + str(x.UnBudgeted))
                count += 1


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
        print("\n----------------------------------------------------------\n")
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
            print("\n----------------------------------------------------------\n")
            Date = input("\nPlease input the date using the correct formatting (Please use the MM/DD/YYYY format)\n\nInput: ")

            try:
                Date = datetime.datetime.strptime(Date,'%m/%d/%Y')
                GoodDate = True

            except:
                pass

        #Asking the user to enter in the money amount of their income statement
        print("\n----------------------------------------------------------\n")
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
                print("\n----------------------------------------------------------\n")
                Amount = input("\nThat format didn't work, please try again (Please use standard money input without commas)\n\nInput: $")
                
                try: 
                    Amount = "{:.2f}".format(float(Amount))
                    GoodMoney = True

                except Exception as e:
                    print(e)

        #Asking the user to input a description for their paycheck. This is one of the key ways that users will use determine what the paycheck is 
        print("\n----------------------------------------------------------\n")       
        Description = input("\nPlease enter a short description of the income.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")
         
        while Description == "":
            print("\n----------------------------------------------------------\n")
            Description = input("\nPlease enter something, an empty input is not allowed.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")

        #creation of the new income statement
        Temp_IncomeStatement = IncomeStatement(Date = str(Date), Amount = float(Amount), UnBudgeted = float(Amount), Description = Description, User_ID = user.User_ID).commit_incomestatement()   
        
        #printing the income statement out to the user
        print("\n\nHere is your statement:\n")
        print("Date: " + str(IncomeStatement.format_date(Date)) + "\nDescription: " + Description + "\nAmount: $" + Amount + "\n\n")
        user_accepts_entered_statement = True
        user_accepts_entered_statement_input = input("Does this statement look right to you? \n\n1) Yes \n2) No \n\nYour Input (Yes or No): ").lower()
        while user_accepts_entered_statement_input !=  "yes" and user_accepts_entered_statement_input != "no":
            user_accepts_entered_statement_input = input("\n\nPlease only enter accepted values...\nDoes this statement look right to you? \n\n1) Yes \n2) No \n\nYour Input (Yes or No): ")

        if user_accepts_entered_statement_input == "no":
            IncomeStatement.edit_user_statements(user, 1)


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


    

        

    
    
        
import sqlite3, time, os
from Models.LoadDatabase import load_DB
from Auth.Login import login
from Models.LoadDatabase import close
from Models.LoadDatabase import commit
from LogModule import logger
from Models.IncomeStatement import IncomeStatement
from Models.BankAccount import BankAccount
from Models.Budget import Budget

#Global Variables 


def RunApp(user):

    #Loading the global defaults for logging
    logger()
    
    #If the user object is empty, the the user is asked to login
    if user == None:
        logger()
        load_DB(os.getcwd() + '/BudgetBuddy.db')
        user = None
        print('--------------------------\n|WELCOME TO BUDGET BUDDY!|\n--------------------------') 
        user = login()
        cont = True
    
    #If the user object is filled, the program will continue to the main menu
    elif user != None:
        cont = True

    #If for something else happens, the program will be reset and start over
    else:
        user = None
        RunApp(user)

    #Loop for the main menu
    while cont == True:
        
        Menu_Choice = input("\n\n-----------------------------------------------------\n|Please choose what you would like to interact with:|\n----------------------------------------------------- \n\n1)Income Statements\n2)Expenses \n3)Budgets \n4)Bank Accounts \n5)Your Account \n6)Exit the Program \n\nYour Input:")
        
        while Menu_Choice == '':
            Menu_Choice = input("\n\n-----------------------------------------------------\n|Please choose what you would like to interact with:|\n----------------------------------------------------- \n\n1)Income Statements\n2)Expenses \n3)Budgets \n4)Bank Accounts \n5)Your Account \n6)Exit the Program \n\nYour Input:")

        Menu_Choice = int(Menu_Choice)

        if Menu_Choice == 1:

            cont1 = True

            while cont1:
            
                IncomeStatement_Choice = int(input("\n\n\n------------------------------------------\n|Please select what you would like to do:|\n------------------------------------------ \n\n1)Create a New Income Statement \n2)Edit an Existing Income Statement \n3)View Your Existing Income Statements \n4)Return to the Main Menu\n\nYour Input:"))

                while IncomeStatement_Choice != 1 and IncomeStatement_Choice != 2 and IncomeStatement_Choice != 3 and IncomeStatement_Choice != 4:

                    IncomeStatement_Choice = int(input("\n\n\n------------------------------------------\n|Please only select one of these choices:|\n------------------------------------------ \n\n1)Create a New Income Statement \n2)Edit an Existing Income Statement \n3)View Your Existing Income Statements \n4)Return to the Main Menu\n\nYour Input:"))

                if IncomeStatement_Choice == 1:

                    IncomeStatement.create(user)

                elif IncomeStatement_Choice == 2:

                    IncomeStatement.edit_user_statements(user)

                elif IncomeStatement_Choice == 3:

                    IncomeStatement.view_user_statements(user)
                    
                elif IncomeStatement_Choice == 4:

                    RunApp(user)

        elif Menu_Choice == 2:
            
            pass

        elif Menu_Choice == 3:
            
                       
            cont3 = True 

            while cont3:

                budget_choice = input("\n\n\n------------------------------------------\n|Please select what you would like to do:|\n------------------------------------------ \n\n1)Create a New Budget \n2)Edit an Existing Budget \n3)View Your Existing Budgets \n4)Return to the Main Menu\n\nYour Input:")

                while budget_choice == "" or budget_choice != '1' and budget_choice != '2' and budget_choice != '3' and budget_choice != '4':

                    budget_choice = input("\n\n\n--------------------------------------------\n|Please only select one of these statements:|\n--------------------------------------------\n\n1)Create a New Budget \n2)Edit an Existing Budget \n3)View Your Existing Budgets \n4)Return to the Main Menu\n\nYour Input:")
        
                if budget_choice == '1':
                
                    pass

                elif budget_choice == '2':
                    
                    pass

                elif budget_choice == '3':

                    Budget.view_user_budgets(user)

                elif budget_choice == '4':

                    RunApp(user)

        elif Menu_Choice == 4:

            cont4 = True
            
            while cont4:
            
                bank_account_choice = input("\n\n\n------------------------------------------\n|Please select what you would like to do:|\n------------------------------------------ \n\n1)Create a New Bank Account \n2)Edit an Existing Bank Account \n3)View Your Existing Bank Accounts \n4)Return to the Main Menu\n\nYour Input:")

                while bank_account_choice == "" or bank_account_choice != '1' and bank_account_choice != '2' and bank_account_choice != '3' and bank_account_choice != '4':

                    bank_account_choice = input("\n\n\n--------------------------------------------\n|Please only select one of these statements:|\n--------------------------------------------\n\n1)Create a New Bank Account \n2)Edit an Existing Bank Account \n3)View Your Existing Bank Accounts \n4)Return to the Main Menu\n\nYour Input:")
        

                if bank_account_choice == '1':
                
                    BankAccount.create(user)

                elif bank_account_choice == '2':
                    
                    BankAccount.edit_user_bank_accounts(user)

                elif bank_account_choice == '3':

                    BankAccount.view_user_bank_accounts(user)

                elif bank_account_choice == '4':

                    RunApp(user)
            
        
        elif Menu_Choice == 5:
            pass

        
        elif Menu_Choice == 6:
            cont = False

        



    commit()
    print("\n\nClosing DataBase...")
    print("\nHave a nice day! ")
    close()
    exit()


user = None
RunApp(user)















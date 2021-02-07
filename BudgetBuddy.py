import sqlite3, time, os
from Models.LoadDatabase import load_DB
from Auth.Login import login
from Models.LoadDatabase import close
from Models.LoadDatabase import commit
from Models.IncomeStatement import IncomeStatement

#Global Variables 


def RunApp(user):
    
    if user == None:
        load_DB(os.getcwd() + '/BudgetBuddy.db')
        user = None
        print('--------------------------\n|WELCOME TO BUDGET BUDDY!|\n--------------------------') 
        try:   
            user = login()
            cont = True
            
        except Exception as e:
            print(e)
            print("Looks like the program ran into a bad error, we are going to restart the app for you")
            user = None
            RunApp(user)

    elif user != None:
        cont = True

    else:
        user = None
        RunApp(user)

    while cont == True:
        
        
        Menu_Choice = int(input("\nPlease choose what you would like to interact with: \n\n1)Income Statements\n2)Expenses \n3)Budgets \n4)Bank Accounts \n5)Your Account \n\nYour Input:"))
        
        if Menu_Choice == 1:

            cont1 = True

            while cont1 == True:
            
                IncomeStatement_Choice = int(input("\n\nPlease select what you would like to do: \n\n1)Create a New Income Statement \n2)Edit an Existing Income Statement \n3)View Your Existing Income Statements \n4)Return to the Main Menu\n\nYour Input:"))

                while IncomeStatement_Choice != 1 and IncomeStatement_Choice != 2 and IncomeStatement_Choice != 3 and IncomeStatement_Choice != 4:
                    IncomeStatement_Choice = int(input("\n\nPlease only select one of these choices: \n\n1)Create a New Income Statement \n2)Edit an Existing Income Statement \n3)View Your Existing Income Statements \n4)Return to the Main Menu\n\nYour Input:"))

                if IncomeStatement_Choice == 1:
                    IncomeStatement.create(user)

                elif IncomeStatement_Choice == 2:
                    pass

                elif IncomeStatement_Choice == 3:
                    IncomeStatement.view_user_statements(user)
                    
                    pass

                else:
                    RunApp(user)

        elif Menu_Choice == 2:
            
            pass

        elif Menu_Choice == 3:
            
            pass

        elif Menu_Choice == 4:
            
            pass

        else:
            
            cont = False



    commit()
    print("\n\nClosing DataBase...")
    print("\nHave a nice day! ")
    close()


user = None
RunApp(user)















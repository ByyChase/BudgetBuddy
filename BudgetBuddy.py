import sqlite3, time, os
from Models.CreateDatabase import LoadDB
from Auth.Login import Login
from Models.CreateDatabase import close
from Models.CreateDatabase import commit


def RunApp():
    
    LoadDB(os.getcwd() + '/BudgetBuddy.db')
    user = Login()

    #Create Variables 
    cont = True

    while cont == True:
        
        print("\n\nWelcome " + user.First_Name)
        Menu_Choice = int(input("Please chose one of the options: \n\n1) Create new Income Statement \n2) Split your Income Statement \n3) Add New Expense \n4) View an Income Statement \n5) Quit the Program \n\n\tYour Choice: "))
        
        if Menu_Choice == 1:
            
            #CreatePaycheck()
            pass

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

RunApp()















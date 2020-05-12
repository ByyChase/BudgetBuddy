import sqlite3, time
from Models.CreateDatabase import CreateDB
from Models.CreateDatabase import LoadDB
from ObjectManipulation import CreatePaycheck
from Auth.Login import Login


def RunApp():
    print("Connecting to Database")
    db = sqlite3.connect('EasyBudget.db')
    c = db.cursor()

    LoadDB()

    Login()


    #Create Variables 
    cont = True

    while cont == True:
        print("\n\nWelcome to Easy Budget")
        Menu_Choice = int(input("Please chose one of the options: \n\n1) Create new PayCheck \n2) Split your PayCheck \n3) Add New Expense \n4) View a PayCheck \n5) Quit the Program \n\n\tYour Choice: "))

        if Menu_Choice == 1:
            CreatePaycheck()

        elif Menu_Choice == 2:
            pass

        elif Menu_Choice == 3:
            pass

        elif Menu_Choice == 4:
            pass

        else:
            cont = False



    db.commit()
    print("\n\nClosing DataBase...")
    print("0%")
    time.sleep(1)
    print("\n20%")
    time.sleep(1)
    print("\n40%")
    time.sleep(1)
    print("\n60%")
    time.sleep(1)
    print("\n80%")
    time.sleep(1)
    print("\n100%")
    print("\nHave a nice day! ")
    db.close()




RunApp()















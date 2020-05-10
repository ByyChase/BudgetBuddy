import sqlite3

def CreateDB():
    
    db = sqlite3.connect('EasyBudget.db')
    c = db.cursor()

    try:
        
        c.execute("""CREATE TABLE Paycheck (
                        Date text,
                        Amount real,
                        UnBudgeted real,
                        Description text, 
                        PayCheck_ID integer,
                        User_ID integer
                        )""")

        c.execute("""CREATE TABLE Budget (
                        Name text,
                        Amount real,
                        UnSpent real,
                        Description text,
                        PayCheck_ID integer,
                        Budget_ID integer,
                        User_ID integer 
                        )""")

        c.execute("""CREATE TABLE Expense (
                        Name text,
                        Description text,
                        Amount real,
                        PayCheck_ID integer,
                        Budget_ID integer,
                        Expense_ID integer,
                        User_ID integer
                        )""")

        c.execute("""CREATE TABLE User (
                        Username text,
                        First_Name text,
                        Last_Name text,
                        Password text
                        User_ID integer
                        )""")

        print("Creating Database")

    except:
        print("Database already created")


    print("Database Connected")








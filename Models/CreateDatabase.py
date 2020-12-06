import sqlite3, os

db = None

def LoadDB(db_file):

    global db

    if os.path.isfile('BudgetBuddy.db'):
        print("Connecting to Database")
        db = sqlite3.connect(db_file)
    
    else:
        db = sqlite3.connect(db_file)
        CreateDB(db.cursor())

    return db.cursor()


def CreateDB(c):

    try:  
        c.execute("""CREATE TABLE PAYCHECK (
                        Date text,
                        Amount real,
                        UnBudgeted real,
                        Description text, 
                        PayCheck_ID integer,
                        User_ID integer PRIMARY KEY,
                        foreign key(User_ID) references User(User_ID)
                        )""")

        c.execute("""CREATE TABLE BUDGET (
                        Name text,
                        Amount real,
                        UnSpent real,
                        Description text,
                        PayCheck_ID integer,
                        Budget_ID integer PRIMARY KEY,
                        User_ID integer,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(PayCheck_ID) references Paycheck(PayCheck_ID) 
                        )""")

        c.execute("""CREATE TABLE EXPENSE (
                        Name text,
                        Description text,
                        Amount real,
                        PayCheck_ID integer,
                        Budget_ID integer,
                        Expense_ID integer PRIMARY KEY,
                        User_ID integer,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(PayCheck_ID) references Paycheck(PayCheck_ID) ,
                        foreign key(Budget_ID) references Budget(Budget_ID) 
                        )""")

        c.execute("""CREATE TABLE USER (
                        Username text,
                        First_Name text,
                        Last_Name text,
                        Password text,
                        User_ID integer PRIMARY KEY
                        )""")

        c.execute("""CREATE TABLE BANKACCOUNT (
                        Name text,
                        Ammount real,
                        Description text,
                        Account_ID integer PRIMARY KEY,
                        User_ID integer,
                        foreign key(User_ID) references User(User_ID)
                        )""")

        print("Creating Database")

    except Exception as error:
        print(error)
    
    return

def cursor():
    if not db:
        LoadDB()

    else:
        return db.cursor()

def commit():
    db.commit()

def close():
    db.close()


    








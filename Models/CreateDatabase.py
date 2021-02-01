import sqlite3, os

db = None

def LoadDB(db_file):

    global db

    if os.path.isfile('BudgetBuddy.db'):
        print("Connecting to Database... \n\n")
        db = sqlite3.connect(db_file)
    
    else:
        db = sqlite3.connect(db_file)
        CreateDB(db.cursor())

    return db.cursor()


def CreateDB(c):

    try:
        c.execute("""CREATE TABLE INCOMESTATEMENT (
                        Date text,
                        Amount real,
                        UnBudgeted real,
                        Description text,
                        IncomeStatement_ID integer PRIMARY KEY,
                        User_ID int,
                        foreign key(User_ID) references User(User_ID)
                        )""")

        c.execute("""CREATE TABLE BUDGET (
                        Name text,
                        Amount real,
                        UnSpent real,
                        Description text,
                        IncomeStatement_ID integer,
                        Budget_ID integer PRIMARY KEY,
                        User_ID int,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(IncomeStatement_ID) references INCOMESTATEMENT(IncomeStatement_ID) 
                        )""")

        c.execute("""CREATE TABLE EXPENSE (
                        Name text,
                        Description text,
                        Amount real,
                        IncomeStatement_ID integer,
                        Budget_ID integer,
                        Expense_ID integer PRIMARY KEY,
                        User_ID integer,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(IncomeStatement_ID) references INCOMESTATEMENT(IncomeStatement_ID),
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
    
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


    








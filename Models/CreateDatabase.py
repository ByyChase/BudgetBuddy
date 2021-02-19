import logging
def create_DB(c):

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
                        Amount real,
                        Description text,
                        Account_ID integer PRIMARY KEY,
                        User_ID integer,
                        foreign key(User_ID) references User(User_ID)
                        )""")

        logging.info("Database created sucessfully")

    except Exception as error:
        logging.exception("Error Creating Database")
    
    return


    








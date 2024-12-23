import logging
def create_DB(c):

    try:
        
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
        
        c.execute("""CREATE TABLE INCOMESTATEMENT (
                        Date text,
                        Amount real,
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
                        Budget_ID integer PRIMARY KEY,
                        User_ID int,
                        foreign key(USER_ID) references User(User_ID)
                        )""")

        c.execute("""CREATE TABLE BUDGET_INCOME_STATEMENT_TIE (
                        Budget_IncomeStatement_ID int PRIMARY KEY,
                        Budget_ID int,
                        IncomeStatement_ID int,
                        User_ID integer,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(Budget_ID) references Budget(Budget_ID)
                        foreign key(IncomeStatement_ID) references INCOMESTATEMENT(IncomeStatement_ID)
                        )""")

        c.execute("""CREATE TABLE LINE_ITEM (
                        LineItem_ID int PRIMARY KEY,
                        Amount real,
                        UnSpent real,
                        Budget_ID int,
                        User_ID integer,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(Budget_ID) references Budget(Budget_ID)
                        )""")

        c.execute("""CREATE TABLE EXPENSE (
                        Name text,
                        Description text,
                        Amount real,
                        Budget_ID integer,
                        Expense_ID integer PRIMARY KEY,
                        User_ID integer,
                        LineItem_ID int,
                        foreign key(USER_ID) references User(User_ID),
                        foreign key(LineItem_ID) references Line_Item(LineItem_ID)
                        )""")

        logging.info("Database created sucessfully")

    except Exception as error:
        logging.exception("Error Creating Database")
    
    return


    







 
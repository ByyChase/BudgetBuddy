import sqlite3

def CreateDB():
    
    db = sqlite3.connect('EasyBudget.db')
    c = db.cursor()

    try:
        
        c.execute("""CREATE TABLE PayCheck (
                        Date text,
                        Amount real,
                        UnBudgeted real,
                        Description text, 
                        PayCheck_ID integer
                        )""")

        #c.execute("""CREATE TABLE PayCheck (
        #                Date text,
        #                Amount real,
        #                Description text, 
        #                PayCheck_ID integer
        #                )""")

        print("Creating Database")

    except:
        print("Database already created")


    





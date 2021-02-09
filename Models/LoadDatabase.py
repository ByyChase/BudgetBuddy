import sqlite3, os, logging
from Models.CreateDatabase import create_DB

db = None


def load_DB(db_file):

    global db
    

    if os.path.isfile('BudgetBuddy.db'):

        try:

            db = sqlite3.connect(db_file)
            logger.info("Database successfully loaded")

        except Exception as e:

            logging.exception("Unable to connect to database, attempting to create database")
            pass
    
    else:

        try:

            db = sqlite3.connect(db_file)
            create_DB(db.cursor())

        except Exception as e:

            logging.exception("Unable to create database, closing program")
            print("Critial error creating database, see logs for more information.\n\nExiting Program")
            exit()

    return db.cursor()

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


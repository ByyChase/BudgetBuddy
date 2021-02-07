import sqlite3, os
from Models.CreateDatabase import create_DB

db = None

def load_DB(db_file):

    global db

    if os.path.isfile('BudgetBuddy.db'):
        print("Connecting to Database... \n\n")
        db = sqlite3.connect(db_file)
    
    else:
        db = sqlite3.connect(db_file)
        CreateDB(db.cursor())

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
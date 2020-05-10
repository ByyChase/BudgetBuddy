import sqlite3
from Models.CreateDatabase import CreateDB


def RunApp():
    print("Connecting to Database")
    db = sqlite3.connect('EasyBudget.db')
    c = db.cursor()

    CreateDB()

    db.commit()
    db.close()

    


RunApp()









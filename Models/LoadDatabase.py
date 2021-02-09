import sqlite3, os, logging
from Models.CreateDatabase import create_DB

db = None


def load_DB(db_file):
    """
    This function is used to load the database at program start.

    ...

    Parameters
    ----------

    db_file : string
        The location that the database file should be. It should be located in the root directory of the program

    ...

    Returns
    -------

    db.cursor() : function
        This calls the cursor function that returns the cursor for the database
    """

    global db
    
    #Checks to see if the database file exists. If it does not the database will be created 
    if os.path.isfile('BudgetBuddy.db'):

        try:

            #create connection with the database 
            db = sqlite3.connect(db_file)
            logging.info("Database successfully loaded")

        except Exception as e:

            logging.exception("Unable to connect to database, attempting to create database")
            pass
    
    else:

        try:

            #Creates the database files
            db = sqlite3.connect(db_file)
            #Calls the create_db method to create the database tables 
            create_DB(db.cursor())

        except Exception as e:

            logging.exception("Unable to create database, closing program")
            print("Critial error creating database, see logs for more information.\n\nExiting Program")
            exit()

    return db.cursor()

def cursor():
    """
    This function is used to retreive the database cursor

    ...

    Returns
    -------

    db.cursor() : function
        This calls the cursor function that returns the cursor for the database
    """

    if not db:
        LoadDB()

    else:
        return db.cursor()

def commit():
    """
    This method is used to commit the database
    """

    db.commit()

def close():
    """
    This method is used to close the database connection
    """

    db.close()



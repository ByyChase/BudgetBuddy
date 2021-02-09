import logging, os


def logger():
    """
    This class is used to setup global logging in the program. It will create the folder/file on first launch of the program
    and will set the correct global variables for logging. This totally could be a function in the main program but I felt 
    having it seperate just for the sake of being clean and tiddy was the best idea. I also originally thought you had to 
    create a logger object and use that to call which is what this functions original purpose was. It may potentially get
    depricated once the program grows in size.
    """

    #Trys to make the */logs/ file directory 
    try:

        os.makedirs(os.getcwd() + '/logs/')

    #If the folder already exists just skip over the step
    except Exception as e:

        pass

    #Setting the correct global logging variables. Set to DEBUG for dev, will be set to error for prod   
    logging.basicConfig(filename= os.getcwd() + '/logs/BudgetBuddy.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
   
    
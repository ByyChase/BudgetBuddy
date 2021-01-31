from Models.CreateDatabase import cursor
from Models.CreateDatabase import commit
from Models.CreateDatabase import dict_factory


class IncomeStatement:

    def __init__(self, Date=None, Amount=None, Description=None, IncomeStatement_ID=None, UnBudgeted=None, User_ID=None):
        
        self.Date = Date                                #String
        self.Amount = Amount                            #Double
        self.Description = Description                  #String
        self.IncomeStatement_ID = IncomeStatement_ID    #String
        self.UnBudgeted = UnBudgeted                    #Double
        self.User_ID = User_ID                          #Integer

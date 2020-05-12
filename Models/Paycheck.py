class Paycheck:

    def __init__(self, Date=None, Amount=None, Description=None, Paycheck_ID=None, UnBudgeted=None, User_ID=None):
        self.Date = Date                 #String
        self.Amount = Amount             #Double
        self.Description = Description   #String
        self.Paycheck_ID = Paycheck_ID   #String
        self.UnBudgeted = UnBudgeted     #Double
        self.User_ID = User_ID           #Integer
        
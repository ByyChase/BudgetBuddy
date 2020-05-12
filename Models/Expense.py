class Expense:

    def __init__(self, Name=None, Description=None, Amount=None, Expense_ID=None, Budget_ID=None, Paycheck_ID=None, User_ID=None):
        self.Name = Name                 #String
        self.Description = Description   #String
        self.Amount = Amount             #Double 
        self.Expense_ID = Expense_ID     #Integer
        self.Budget_ID = Budget_ID       #Integer
        self.Paycheck_ID = Paycheck_ID   #Integer
        self.User_ID = User_ID           #Integer

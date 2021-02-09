class Budget:

    def __init__(self, Name=None, Amount=None, UnSpent=None, Description=None, Paycheck_ID=None, Budget_ID=None):
        self.Name = Name                 #String
        self.Amount = Amount             #Double    
        self.UnSpent = UnSpent           #Double  
        self.Description = Description   #String 
        self.IncomeStatement_ID = IncomeStatement_ID   #Integer
        self.Budget_ID = Budget_ID       #Integer
        self.User_ID = User_ID           #Integer
from Models.LoadDatabase import cursor
from Models.LoadDatabase import commit
from Models.LoadDatabase import dict_factory
import datetime
from money import Money


class IncomeStatement:

    def __init__(self, Date=None, Amount=None, Description=None, IncomeStatement_ID=None, Budget_ID = None, UnBudgeted=None, User_ID=None):
        
        self.Date = Date                                #String
        self.Amount = Amount                            #Double
        self.Description = Description                  #String
        self.IncomeStatement_ID = IncomeStatement_ID    #String
        self.UnBudgeted = UnBudgeted                    #Double
        self.User_ID = User_ID                          #Integer

    db_fetch = "SELECT * FROM INCOMESTATEMENT WHERE "

    def fetch(**KWARGS):
        
        elements = []
        db_fetch = IncomeStatement.db_fetch
        
        for k,v in KWARGS.items():
            
            db_fetch += "\"{}\"=?".format(k)
            elements.append(v)
            
        Temp_SQL_Data = cursor().execute(db_fetch, (elements)).fetchone()
            
        if Temp_SQL_Data:
            return IncomeStatement(Date = Temp_SQL_Data[0], Amount = Temp_SQL_Data[1], UnBudgeted = Temp_SQL_Data[2], Description = Temp_SQL_Data[3], IncomeStatement_ID = Temp_SQL_Data[4], User_ID = Temp_SQL_Data[5])
        
        else:
            return "Income Statement Not Found"
        
        
    def New_IncomeStatement(self): 
        
        statement = "INSERT INTO INCOMESTATEMENT (Date, Amount, UnBudgeted, Description, User_ID) VALUES (?, ?, ?, ?, ?)"
        cursor().execute(statement, (self.Date, self.Amount, self.UnBudgeted, self.Description, self.User_ID))
        commit()
        
    def Create(user):
        
        #Asking the user for their input 
        Date = input("\nPlease input the date you received the income (Please use the MM/DD/YYYY format): ")
        GoodDate = False
        
        try:
            Date = datetime.datetime.strptime(Date,'%m/%d/%Y')
            GoodDate = True
            print(Date)
            
        except:
            pass
        
        while GoodDate == False:
            Date = input("\nPlease input the date using the correct formatting (Please use the MM/DD/YYYY format)\n\nInput: ")

            try:
                Date = datetime.datetime.strptime(Date,'%m/%d/%Y')
                GoodDate = True

            except:
                pass
            
        Amount = input("\nPlease input the amount of the income (Please use standard money input)\n\nInput: $")
        GoodMoney = False
        try: 
            Amount = "{:.2f}".format(float(Amount))
            GoodMoney = True
        
            
        except Exception as e:
            print(e)
            while GoodMoney == False: 
                Amount = input("\nThat format didn't work, please try again (Please use standard money input without commas)\n\nInput: $")
                
                try: 
                    Amount = "{:.2f}".format(float(Amount))
                    GoodMoney = True

                except Exception as e:
                    print(e)
                
        Description = input("\nPlease enter a short description of the income.\nThis, along with the date, will be how you have to recognize the income statement. Please be descriptive.\n\nInput:")
        Date_String = str(Date)
        print(Date_String)
        Temp_IncomeStatement = IncomeStatement(Date = Date_String, Amount = float(Amount), UnBudgeted = float(Amount), Description = Description, User_ID = user.User_ID)    
        Temp_IncomeStatement.New_IncomeStatement() 
        
        print("\n\nHere is your statement:\n")
        print("Date: " + IncomeStatement.Format_Date(Date) + "\nDescription: " + Description + "\nAmount: $" + Amount + "\n\n")
        
        return
    
    def Format_Date(Date):
        Date_Split_From_DateTime_Object = str(Date.date()).split(' ')
        Date = Date_Split_From_DateTime_Object[0].split('-')
        Date = Date[1] + "/" + Date[2] + "/" + Date[0]
        return Date
        
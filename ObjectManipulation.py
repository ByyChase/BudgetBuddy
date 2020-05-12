from Models.Paycheck import Paycheck
from Models.Budget import Budget 
from Models.User import User
from Models.Expense import Expense
from Models.BankAccount import BankAccount 


def CreatePaycheck():
    print("\nCreate a Paycheck")

    Date = input("\nPlease input a date for the paycheck: ")

    Description = input("\nPlease input a description of the Paycheck: ")

    Amount = input("\nPlease input a Paycheck ammount: $")

    

    PaycheckTemp = Paycheck(Date = Date, Amount = Amount, Description = Description, Paycheck_ID = 123, UnBudgeted = Amount, User_ID = 12)

    print("\nPaycheck Created")



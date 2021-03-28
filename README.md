# BudgetBuddy

BudgetBuddy is a Python program that allows for easy budgeting of funds that you receive. 
<br></br>
## Running Budget Buddy ##

 Download the repository from the Web GUI or clone it using the following command:
 
 `git clone https://github.com/ByyChase/BudgetBuddy.git` 
 
 You can then run the `BudgetBuddy.py` file from your GUI or use the following command in the main directory: 
 
 `python3 BudgetBuddy.py`
 <br></br>
 ## Requirements ##
 
 All the requirements to run the program are located in the `Requirements.txt` file in the repository. 
 
 You can install the requirements using the following command from the main directory:
 
 `pip install -r requirements.txt`
 <br></br>
 ## What Currently Works ##

* Creation of the Database 
* Creation of User Accounts
* Logging into Accounts
* Creation of Income Statements
* Viewing of Income Statements
* Editing of Income Instances
* Logging errors to external error log
* Creation of Bank Accounts
* Viewing Bank Accounts
* Editing of Bank Accounts
<br></br>
 ## What is being Worked On ##

* Creation of Budget
* Viewing of Budgets 
* Editing of Budgets 
<br></br>
## In the Queue ##

* Deleting of IncomeStatements and Budgets
* Linking IncomeStatement to Bank Account 
* Deleting Budgets
* Creation of Buckets 
* Editing of Buckets 
* Viewing of Buckets 
* Deleting of Buckets
* Creation of Expenses
* Viewing of Expenses
* Editing of Expenses
* Deleting of Expenses
<br></br>
<br></br>
 # BudgetBuddy 2.0 #
* This will be an new release with the use of a full blown GUI! 
* I am going back and forth between doing a janky way with Electron or something Python Native
<br></br>
<br></br>
# How Budget Buddy Works # 
Here is an overview of how Budget Buddy works and helps you budget and keep track of your money! 
<br></br>
## The Different Parts of Budget Buddy ##
</br>
Budget Buddy has a couple different objects to help you budget:

* Bank Accounts
* Income Statements
* Buckets
* Budgets
* Expenses
	
### Bank Accounts ###

Bank Accounts are the sole place that you store your money. These accounts 
cannot edit the contents of the bank account once the user creates it. All 
changes to a bank accounts balance must be done through Income Statements and 
Expenses.

### Income Statements ###

Income Statements are how you add income into your bank accounts. These statements 
can be edited but if you edit the amounts in the Income Statement anything that has money 
from the income statement in it will need to be edited as well. Income Statements are not tied 
to anything directly and stand on their own. You are able to split your Income Statements between different accounts. 

### Budgets ###

Budgets are how you can split up your income into how you plan on spending it. Budgets are one time use expenses, once you put so much money into a budget to be spent you can't add any more. It's main purpose is to be used for things that you don't plan on rolling over month to month, week to week, or however often you chose to budget your money. This can be used for things like someone's birthday, a dinner you plan on going to, or any other onetime expense. Budgets are tied to Income Statements and have an original budgeted amount and the amount left to be spent. 

### Buckets ###

Buckets are like budgets but are for long term. Things like Food, electric, car payments, rent, car insurance, or anything else that you want to roll over continually and add money to the pile.  They act the same was as budgets and are attached to Income Statements but they are meant to be used, and treated, as persistent entities instead of one time savings events. 

### Expenses ###

Expenses are just as they sound, expenses. Expenses allow you to keep track of any money that you spend.  Expenses take money directly out of something. You can't make a purchase without attaching it to something. You can attach and expense to a Bucket, Budget, or out of a bank account.


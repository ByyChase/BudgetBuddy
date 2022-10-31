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

Bank accounts are just like they sound, these represent your real bank accounts! They can be edited through adding income statements or expenses to them. Once you create a bank account you can not manually edit the amount of money in them so be careful when you set them uip! 

### Income Statements ###

Income statements are one of the ways you can edit the amount of money in your bank account. These typically represent payments from your friends, paychecks from work, or gifts given to you for special events! These are what your budgeting is is based off of as well! You are able to edit these, however any budgets, expenses, or additions to buckets that are made from that income statement get deleted and have to be reentered. 

### Budgets ###

Budgets are how you split up your money for one time expenses! These represent things like birthdays, special dinners out, or one off purchases that you don't make often and don't want to roll over month to month. These budgets are attached to specific Income Statements

### Buckets ###

Buckets are like budgets but are for long term. Things like Food, electric, car payments, rent, car insurance, or anything else that you want to roll over continually and add money to the pile.  They act the same was as budgets  but they are meant to be used, and treated, as persistent entities instead of one time savings events. These are not attached to a specific income statement

### Expenses ###

Expenses are just as they sound, expenses. Expenses allow you to keep track of any money that you spend.  Expenses take money directly out of something. You can't make a purchase without attaching it to something. You can attach and expense to a Bucket, Budget, or out of a bank account.


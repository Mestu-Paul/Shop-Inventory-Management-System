import tkinter as tk
from tkinter import Menu

def getMenubar(root):
    # create a menubar
    menubar = Menu(root)
    root.config(menu=menubar)


    # add a menu item to the menu
    # task_menu.add_command(
    #     label='Exit',
    #     command=root.destroy
    # )


    # create a menu
    Tasks_menu = Menu(menubar)
    Accounting_menu = Menu(menubar)
    Database_menu = Menu(menubar)
    Setting_menu = Menu(menubar)
    User_menu = Menu(menubar)
    Panel_menu = Menu(menubar)
    Email_SMS_menu = Menu(menubar)
    Help_menu = Menu(menubar)

    # add the File menu to the menubar
    menubar.add_cascade(
        label="Tasks",
        menu=Tasks_menu
    )
    menubar.add_cascade(
        label="Accounting",
        menu=Accounting_menu
    )
    menubar.add_cascade(
        label="Database",
        menu=Database_menu
    )
    menubar.add_cascade(
        label="Setting",
        menu=Setting_menu
    )
    menubar.add_cascade(
        label="User",
        menu=User_menu
    )
    menubar.add_cascade(
        label="Panel",
        menu=Panel_menu
    )
    menubar.add_cascade(
        label="Email & SMS",
        menu=Email_SMS_menu
    )
    menubar.add_cascade(
        label="Help",
        menu=Help_menu
    )

    # add a menu item to the setting menu
    Setting_menu.add_command(
        label = 'General Setting',
        command = General_Setting
    )
    Setting_menu.add_command(
        label = 'Email Setting',
        command = Email_Setting
    )
    
    # add menu item to the Accounting_menu
    Accounting_menu.add_command(
	label = 'Manage Account',
	command = manage_account
    )

    Accounting_menu.add_command(
        label = 'Transaction Entry',
        command = transaction_entry
    )

    Accounting_menu.add_command(
        label = 'Bank Transaction Entry',
        command = bank_transaction_entry
    )

    Accounting_menu.add_command(
        label = 'Transaction Report',
        command = transaction_report
    )

    Accounting_menu.add_command(
        label = 'Account Ladger',
        command = account_ladger
    )

    Accounting_menu.add_command(
        label = 'Summary Sheet',
        command = summary_sheet
    )


    return menubar

# ------------- setting command ------------- #
def General_Setting():
    print("General setting")

def Email_Setting():
    print("Email setting")
    
# ------------- accounting command ------------- #
def manage_account():
	print('Manage Account')

def transaction_entry():
	print('Transaction Entry')

def bank_transaction_entry():
	print('Bank Transaction Entry')

def transaction_report():
	print('Transaction Report')

def account_ladger():
	print('Account Ladger')

def summary_sheet():
	print('Summary Sheet')


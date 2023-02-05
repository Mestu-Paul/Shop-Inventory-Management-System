import tkinter as tk
from tkinter import Menu


import basic_info_setting as bscinf
from user_panal import User_Panel
# from home import addHome
import help_functions as _help
import DAO as dao
import color_code as color

def getMenubar(root):
    
    # create object for user panel
    global upanel
    upanel = User_Panel(root)

    # create a menubar
    menubar = Menu(root)
    root.config(menu=menubar)


    # add a menu item to the menu
    # task_menu.add_command(
    #     label='Exit',
    #     command=root.destroy
    # )


    # create a menu
    File_menu = Menu(menubar)
    Accounting_menu = Menu(menubar) # ,tearoff=0
    Database_menu = Menu(menubar)
    Setting_menu = Menu(menubar)
    User_panel_menu = Menu(menubar)
    Email_SMS_menu = Menu(menubar)
    Help_menu = Menu(menubar)

    # add the File menu to the menubar
    menubar.add_cascade(
        label="File",
        menu=File_menu
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
    menubar.add_command(
        label="User Panel",
        command=lambda:user_panel(root)
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
        command = lambda: General_Setting(root)
    )
    Setting_menu.add_command(
        label = 'Email Setting',
        command = Email_Setting
    )
    Setting_menu.add_command(
        label = 'Customize Color',
        command = lambda:color.color_change(root)
    )
    
    # add menu item to the Accounting_menu
    Accounting_menu.add_command(
        label = 'Manage Account',
        command = lambda:manage_account(root)
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

    # add menu item to user panel
    User_panel_menu.add_command(
        label='Manage User',
        command=lambda:user_panel(root)
    )
    
    # add menu item to file menu
    File_menu.add_command(
        label='Main Balance',
        command=showMainBalance
    )

    return menubar

def user_panel(root):
    print("user")
    if root.session['role']>1:
        _help.show_message('warning','Without owner you can not access it')
        return
    upanel.user_panel()
    

# ------------- setting command ------------- #
def General_Setting(root):
    print("Basic info >",root.session['role'])
    if root.session['role']>2:
        _help.show_message('warning','As a manager role you can not access it')
        return
    bscinf.basic_info_setting(root)

def Email_Setting():
    print("Email setting")
    
# ------------- accounting command ------------- #
def manage_account(root):
    print('Manage Account')
    # mngbnkac.manage_bank_account(root)

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

# ------------- main balance file menu command ------------- #
def showMainBalance():
    message = dao.get_rows("SELECT total_amount FROM basic;",[])
    if message[0]==0:
        _help.show_message('error',f'While query for total balance {message[1]}')
        return
    print(message[1][0])
    _help.show_message('balance',f"Your current balance is {format(float(message[1][0][0]),'0.2f')}")
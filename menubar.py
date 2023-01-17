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

    # add a menu item to the menu
    Setting_menu.add_command(
        label = 'General Setting',
        command = General_Setting
    )
    Setting_menu.add_command(
        label = 'Email Setting',
        command = Email_Setting
    )
    return menubar

def General_Setting():
    print("General setting")

def Email_Setting():
    print("Email setting")
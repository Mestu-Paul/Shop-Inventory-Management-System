import tkinter as tk

# local 
import menubar as menubar
import home as home
import login as login

# authentication
# a = login.user_login()
# role = a.user_login()

# # if a==None:
# #     exit()
# print("hello -->> ",role)

# root window
root = tk.Tk()
root.title('Shopping Inventory Management System')
root.geometry('1100x650+10+10')
root.minsize(1100,650)

# root.session = 'Owner'

# menubar
MenuBar = menubar.getMenubar(root)

# Home window
home.addHome(root)




root.mainloop()
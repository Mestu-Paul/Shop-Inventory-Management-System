import tkinter as tk

# local 
from menubar import *
from home import *
from login import *

# authentication
# a = user_login()

# root window
root = tk.Tk()
root.title('Shopping Inventory Management System')
root.geometry('1100x650+10+10')
root.minsize(1100,650)

# menubar
MenuBar = getMenubar(root)

# Home window
addHome(root)




root.mainloop()
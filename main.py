import tkinter as tk

# local 
import menubar as menubar
import home as _home
import login as _login

# authentication
role = ['Owner']
# a = _login.UserLogin(role)
# a.userLogin()

if len(role)==0:
    exit()
print("hello -->> ",role)

# root window
root = tk.Tk()
root.title('Shopping Inventory Management System')
root.geometry('1100x650+10+10')
root.minsize(1100,650)

temp = 1 if role[0]=='Owner' else 3
if role[0]=='Admin':
    temp = 2    

root.session = {'role':temp}


# menubar
MenuBar = menubar.getMenubar(root)

# Home window
purchase = _home.Home(root)
purchase.addHome()




root.mainloop()
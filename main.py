import tkinter as tk

# local 
import menubar as menubar
import home as _home
import login as _login

class Main:
    def __init__(self) -> None:
        pass
    def main(self):
        print("hello")
        # authentication
        role = ['Owner','m']
        # a = _login.UserLogin(role)
        # a.userLogin()

        # if len(role)==0:
        #     exit()
        # print("hello -->> ",role)

        # root window
        root = tk.Tk()
        root.title('Shopping Inventory Management System')
        root.geometry('1100x650+10+10')
        root.minsize(1100,650)

        temp = 1 if role[0]=='Owner' else 3
        if role[0]=='Admin':
            temp = 2    

        root.session = {'role':temp,'userName':role[1]}


        # menubar
        MenuBar = menubar.getMenubar(root)

        # Home window
        home_obj = _home.Home(root)
        home_obj.addHome()
        
        root.mainloop()

if __name__ == "__main__":
    obj = Main()
    obj.main()
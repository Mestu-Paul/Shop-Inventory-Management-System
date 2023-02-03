import tkinter as tk
from PIL import ImageTk, Image
import tkcalendar as tkcal
# from datetime import date
import datetime as dt 
import color_code as color
import DAO as dao

class user_login:
    def __init__(self):
        
        # root window
        self.root = tk.Tk()
        self.root.title('Shopping Inventory Management System Login')
        self.root.geometry('600x300+300+200')
        self.root.resizable(False,False)
        self.authenticated = False
        self.role = None
    def authentication(self,user_name,user_password):
        command = f"SELECT user_name,role FROM user_panel WHERE user_name = '?' AND user_password = '?';"
        result = dao.get_rows(command,[user_name.get(),user_password.get()])
        print(result)
        if(result[0]==0):
            tk.Label(self.right_frame,text='Authentication Error!', font=("Comic Sans MS", 10, "italic"), bg=color.color_list[7], fg='red').place(relx=0.53,rely=0.6)
        else:
            self.authenticated=True
            self.role=result[1][0][1]
            print("role ",self.role)
            self.user_login()
            # user name and password 
        # print(user_name)
        # print(user_password)
    def reset_password(self):
        pass
    def user_login(self):
        if self.authenticated:
            print("authe")
            self.root.destroy()
            print("authe 1",self.role)
            return self.role

        self.root.login = ImageTk.PhotoImage(Image.open("img/login.jpg").resize((300,300)))

        self.root.login_image = tk.Label(self.root,image=self.root.login)
        self.root.login_image.place(x=0,y=0,relwidth=0.5,relheight=1)
        
        self.right_frame = tk.Frame(self.root,bg=color.color_list[7]).place(relx=0.5,rely=0,relwidth=0.5,relheight=1)

        tk.Label(self.right_frame,text='Login', font=("Comic Sans MS", 20, "bold"), bg=color.color_list[7], fg='green').place(relx=0.68,rely=0.05)
        
        tk.Label(self.right_frame,text='User name', font=("Comic Sans MS", 12, "italic"), bg=color.color_list[7], fg='black').place(relx=0.53,rely=0.2)
        user_name = tk.Entry(self.right_frame)
        user_name.place(relx=0.51,rely=0.3,width=200)
        tk.Label(self.right_frame,text='User password', font=("Comic Sans MS", 12, "italic"), bg=color.color_list[7], fg='black').place(relx=0.53,rely=0.4)
        user_password = tk.Entry(self.right_frame)
        user_password.place(relx=0.51,rely=0.5,width=200)

        login_button = tk.Button(self.right_frame,text='Login',command=lambda:self.authentication(user_name,user_password), font=("Comic Sans MS", 12, "italic"))
        login_button.place(relx=0.58,rely=0.7,width=150,height=30)
        
        forgot_button = tk.Button(self.right_frame,text='Forgot password?', font=("Comic Sans MS", 12, "italic"),command=self.reset_password)
        forgot_button.place(relx=0.748,rely=0.83,width=150,height=30)
        
        self.root.mainloop()
        
# user_login()
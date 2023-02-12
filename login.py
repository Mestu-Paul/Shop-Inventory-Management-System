import tkinter as tk
from PIL import ImageTk, Image
import tkcalendar as tkcal
# from datetime import date
import re as regex


import datetime as dt 
import color_code as color
import DAO as dao
import help_functions as _help
from tkinter import messagebox

class UserLogin:
    def __init__(self,role):
        
        # root window
        self.root = tk.Tk()
        self.root.title('Shopping Inventory Management System Login')
        self.root.geometry('600x300+300+200')
        self.root.resizable(False,False)
        self.authenticated = False
        self.role = role
    def authentication(self,user_name,user_password):
        command = f"SELECT user_name,role FROM user_panel WHERE user_name = ? AND user_password = ?;"
        result = dao.get_rows(command,[user_name.get(),user_password.get()])
        print(result)
        if(result[0]==0) or len(result[1])==0:
            tk.Label(self.right_frame,text='Authentication Error!', font=("Comic Sans MS", 10, "italic"), bg=color.color_list[7], fg='red').place(relx=0.53,rely=0.6)
        else:
            self.authenticated=True
            self.role.append(result[1][0][1])
            self.role.append(result[1][0][0])
            print("role ",self.role)
            self.userLogin()
        
    def reset_password(self):
        pass
    
    def toggle_password(self):
        if self.user_password["show"] == "*":
            self.user_password["show"] = ""
            self.toggle_button.config(image=self.open_eye)
        else:
            self.user_password["show"] = "*"
            self.toggle_button.config(image=self.closed_eye)
            
    
    def login(self):
        for child in self.right_frame.winfo_children():
            child.destroy()
        tk.Label(self.right_frame,text='Login', font=("Helvic", 20, "bold"), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.4,rely=0.05)
        
        tk.Label(self.right_frame,text='User name', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.2)
        tk.Label(self.right_frame,text='User password', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.4)
        
        self.entries_frame = [tk.Frame(self.right_frame, bg=color.getColor('bd_input')) for i in range(2)]
        self.entries_frame[0].place(relx=0.01,rely=0.3,relwidth=0.78, relheight=0.1)
        self.user_name = tk.Entry(self.entries_frame[0], bd=0)
        self.user_name.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.input_hover(self.entries_frame[0],self.user_name)
        self.entries_frame[1].place(relx=0.01,rely=0.5,relwidth=0.78, relheight=0.1)
        self.user_password = tk.Entry(self.entries_frame[1],show='*', bd=0)
        self.user_password.place(relx=0.006,rely=0.03,relwidth=0.9,relheight=0.94)
        _help.input_hover(self.entries_frame[1],self.user_password)
        
        # password toggle icon
        self.open_eye = ImageTk.PhotoImage(Image.open("img/eye_open.png").resize((20,17)))
        self.closed_eye = ImageTk.PhotoImage(Image.open("img/eye_close.png").resize((20,17)))
        # password toggle button
        self.toggle_button =  tk.Button(self.entries_frame[1], image=self.closed_eye, command=self.toggle_password, bd=0,bg=color.color_list[1])
        self.toggle_button.place(relx=0.9,rely=0.03,relwidth=0.094,relheight=0.94)


        button_frame = [tk.Frame(self.right_frame,bg=color.getColor('bd_button')) for i in range(2)]
        button_frame[0].place(relx=0.23,rely=0.7,width=150,height=30)
        button_frame[1].place(relx=0.46,rely=0.88,width=150,height=30)
        
        self.add_btn = tk.Button(button_frame[0],text='Login', font=("helvic", 12), bd=0, command=lambda:self.authentication(self.user_name,self.user_password))
        self.delete_btn = tk.Button(button_frame[1],text='Forgot password?', font=("helvic", 12), bd=0, command=self.reset_password)
        self.add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        self.delete_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(button_frame[0],self.add_btn)
        _help.button_hover_del(button_frame[1],self.delete_btn)
        
     
    def addNewUserDB(self):
        user_info = [self.user_name.get(),self.user_password.get(),self.user_full_name.get(),"Owner"]
        message_type=['error','success']
        if len(user_info)!=4:
            _help.show_message(message_type[0],"Please fill all the fields")
            return
        for info in user_info:
            print(info)
        for info in user_info:
            if len(info)==0:
                _help.show_message(message_type[0],"Please fill all the fields")
                print(user_info)
                return
            elif regex.match("^[a-zA-Z0-9\s]+$",info)==None:
                _help.show_message(message_type[0],"You can not use any special character")
                return
        message = dao.set_user_panel(user_info)
        print(message)
        self.login()
        _help.show_message(message_type[message[0]],message[1])
        
    def createNew(self): 
        for child in self.right_frame.winfo_children():
            child.destroy()
        tk.Label(self.right_frame,text='Create New User', font=("Helvic", 14, "bold"), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.2,rely=0.01)
        
        tk.Label(self.right_frame,text='User name', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.1)
        tk.Label(self.right_frame,text='User password', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.3)
        tk.Label(self.right_frame,text='Full name', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.5)
        tk.Label(self.right_frame,text='Role', font=("Helvic", 12), bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')
            ).place(relx=0.03,rely=0.7)
        
        self.entries_frame = [tk.Frame(self.right_frame, bg=color.getColor('bd_input')) for i in range(4)]
        self.entries_frame[0].place(relx=0.01,rely=0.2,relwidth=0.78, relheight=0.08)
        self.entries_frame[1].place(relx=0.01,rely=0.4,relwidth=0.78, relheight=0.08)
        self.entries_frame[2].place(relx=0.01,rely=0.6,relwidth=0.78, relheight=0.08)
        self.entries_frame[3].place(relx=0.01,rely=0.8,relwidth=0.78, relheight=0.08)
        
        self.user_name = tk.Entry(self.entries_frame[0], bd=0)
        self.user_name.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.input_hover(self.entries_frame[0],self.user_name)
        self.user_name.focus_set()
        self.user_password = tk.Entry(self.entries_frame[1],show='*', bd=0)
        self.user_password.place(relx=0.006,rely=0.03,relwidth=0.9,relheight=0.94)
        _help.input_hover(self.entries_frame[1],self.user_password)
        self.user_full_name = tk.Entry(self.entries_frame[2], bd=0)
        self.user_full_name.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.input_hover(self.entries_frame[2],self.user_full_name)
        self.user_role = tk.Entry(self.entries_frame[3], bd=0)
        self.user_role.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        self.user_role.insert(0,'Owner')
        self.user_role.config(state='disabled')
        _help.input_hover(self.entries_frame[3],self.user_role)
        
        
        
        # password toggle icon
        self.open_eye = ImageTk.PhotoImage(Image.open("img/eye_open.png").resize((20,17)))
        self.closed_eye = ImageTk.PhotoImage(Image.open("img/eye_close.png").resize((20,17)))
        # password toggle button
        self.toggle_button =  tk.Button(self.entries_frame[1], image=self.closed_eye, command=self.toggle_password, bd=0,bg=color.color_list[1])
        self.toggle_button.place(relx=0.9,rely=0.03,relwidth=0.094,relheight=0.94)


        button_frame = [tk.Frame(self.right_frame,bg=color.getColor('bd_button')) for i in range(2)]
        button_frame[0].place(relx=0.15,rely=0.91,width=90,height=22)
        button_frame[1].place(relx=0.55,rely=0.91,width=90,height=22)
        
        self.add_btn = tk.Button(button_frame[0],text='create', font=("helvic", 12), bd=0, command=self.addNewUserDB)
        self.add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        self.cancel_btn = tk.Button(button_frame[1],text='cancel', font=("helvic", 12), bd=0, command=self.root.destroy)
        self.cancel_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(button_frame[0],self.add_btn)
        _help.button_hover(button_frame[1],self.cancel_btn)
        
                    
    def userLogin(self):
        if self.authenticated:
            print("authe")
            self.root.destroy()
            print("authe 1",self.role)
            return 

        self.root.login = ImageTk.PhotoImage(Image.open("img/login1.png").resize((300,300)))

        self.root.login_image = tk.Label(self.root,image=self.root.login, bg='#ffffff')
        self.root.login_image.place(x=0,y=0,relwidth=0.5,relheight=1)
        
        self.right_frame = tk.Frame(self.root,bg=color.getColor('bg_frame'))
        self.right_frame.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)
        self.login()
        command = 'SELECT * FROM user_panel;'
        result = dao.get_rows(command,[])
        print(result)
        if len(result[1])==0:
            self.createNew()
            
        
        self.root.mainloop()
        
    
        
# role = None
# obj = UserLogin(role)
# obj.userLogin()
import tkinter as tk
from PIL import ImageTk, Image
import tkcalendar as tkcal
# from datetime import date
import datetime as dt 

authenticated = False
def authentication(user_email,user_password):
    # print(user_email)
    # print(user_password)
    tk.Label(right_frame,text='Authentication Error!', font=("Comic Sans MS", 10, "italic"), bg='#e1e1e1', fg='red').place(relx=0.53,rely=0.6)
def reset_password():
    pass
def user_login():
    # root window
    root = tk.Tk()
    root.title('Shopping Inventory Management System')
    root.geometry("600x300+300+200")
    root.resizable(False,False)

    root.login = ImageTk.PhotoImage(Image.open("img/login.jpg").resize((300,300)))

    login_image = tk.Label(root,image=root.login)
    login_image.place(x=0,y=0,relwidth=0.5,relheight=1)
    global right_frame
    right_frame = tk.Frame(root,bg='#e1e1e1').place(relx=0.5,rely=0,relwidth=0.5,relheight=1)

    tk.Label(right_frame,text='Login', font=("Comic Sans MS", 20, "bold"), bg='#e1e1e1', fg='green').place(relx=0.68,rely=0.05)
    
    tk.Label(right_frame,text='User email', font=("Comic Sans MS", 12, "italic"), bg='#e1e1e1', fg='black').place(relx=0.53,rely=0.2)
    user_email = tk.Entry(right_frame)
    user_email.place(relx=0.51,rely=0.3,width=200)
    tk.Label(right_frame,text='User password', font=("Comic Sans MS", 12, "italic"), bg='#e1e1e1', fg='black').place(relx=0.53,rely=0.4)
    user_password = tk.Entry(right_frame)
    user_password.place(relx=0.51,rely=0.5,width=200)

    login_button = tk.Button(right_frame,text='Login',command=lambda:authentication(user_email,user_password), font=("Comic Sans MS", 12, "italic"))
    login_button.place(relx=0.58,rely=0.7,width=150,height=30)
    
    forgot_button = tk.Button(right_frame,text='Forgot password?', font=("Comic Sans MS", 12, "italic"),command=reset_password)
    forgot_button.place(relx=0.748,rely=0.83,width=150,height=30)
    
    
    root.mainloop()
    
# user_login()
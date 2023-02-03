import tkinter as tk
from PIL import ImageTk, Image
import re as regex

def show_message(message_type,message):
    messagebox = tk.Toplevel()
    messagebox.geometry('300x200+200+100')
    messagebox.resizable(False,False)
    message_icon = ImageTk.PhotoImage(Image.open(f"img/{message_type}.png").resize((50,50)))
    tk.Label(messagebox,image=message_icon).place(relx=0.4,rely=0.01)
    text = tk.Text(messagebox,wrap=tk.WORD)
    text.place(relx=0,rely=0.3,relwidth=1,relheight=0.55)
    text.insert(tk.END,message)
    tk.Button(messagebox,text='Ok',command=messagebox.destroy).place(relx=0.46,rely=0.85,relwidth=0.15)
    messagebox.mainloop()

def is_number(var):
    for v in var:
        if regex.match("^[0-9]+([.][0-9]{2})?$",v)==None:
            return False
        return True
def is_alpha(var):
    for v in var:
        if regex.match("^[a-zA-Z\s]+$",v)==None:
            return False
        return True
def is_alphanum(var):
    for v in var:
        if regex.match("^[a-zA-Z0-9\s]+$",v)==None:
            return False
        return True
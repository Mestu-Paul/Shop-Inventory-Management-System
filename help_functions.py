import tkinter as tk
from PIL import ImageTk, Image
import re as regex

def show_message(message_type,message):
    messagebox = tk.Toplevel()
    messagebox.geometry('300x200+200+100')
    messagebox.resizable(False,False)
    message_icon = ImageTk.PhotoImage(Image.open(f"img/{message_type}.png").resize((50,50)))
    tk.Label(messagebox,image=message_icon).pack(side=tk.TOP)
    text = tk.Text(messagebox,wrap=tk.WORD)
    text.pack(side=tk.TOP,fill=tk.X)
    text.insert(tk.END,message)
    tk.Button(messagebox,text='Ok',command=messagebox.destroy).pack(side=tk.TOP)
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
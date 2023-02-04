import tkinter as tk
from PIL import ImageTk, Image
import re as regex

def on_enter(event):
    global btn
    btn.config(bg='#dcfbf6',bd=2)
    print('enter')
    
def on_leave(event):
    global btn
    btn.config(bg='#f1f1f1',bd=1)
    print('leave')
    
def show_message(message_type,message):
    messageBox = tk.Toplevel()
    screen_width = messageBox.winfo_screenwidth()
    screen_height = messageBox.winfo_screenheight()
    # calculate the position to center the frame
    x = (screen_width - 200) // 2
    y = (screen_height - 200) // 2
    messageBox.geometry('300x200+{}+{}'.format(x, y))
    messageBox.title(message_type)
    messageBox.resizable(False,False)
    messageBox.grab_set()
    
    message_icon = ImageTk.PhotoImage(Image.open("img/error.png").resize((50,50)))
    tk.Label(messageBox,bg='#ffffff', image=message_icon).place(relx=0,rely=0.0,relwidth=0.3,relheight=0.75)

    text = tk.Text(messageBox,wrap=tk.WORD,bd=0)
    text.place(relx=0.3,rely=0,relwidth=1,relheight=0.75)
    text.insert(tk.END,message)
    global btn
    btn = tk.Button(messageBox,text='Ok', bd=1, bg='#f1f1f1', relief=tk.SUNKEN, highlightbackground="red", command=messageBox.destroy)
    btn.place(relx=0.7,rely=0.8,width=80)

    btn.bind("<Enter>",on_enter)
    btn.bind("<Leave>",on_leave)
    messageBox.mainloop()

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
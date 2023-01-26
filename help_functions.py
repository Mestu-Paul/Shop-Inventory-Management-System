import tkinter as tk
from PIL import ImageTk, Image

def show_message(message_type,message):
    messagebox = tk.Toplevel()
    messagebox.geometry('300x200+200+100')
    messagebox.resizable(False,False)
    message_icon = ImageTk.PhotoImage(Image.open(f"img/{message_type}.png").resize((50,50)))
    tk.Label(messagebox,image=message_icon).pack(side=tk.TOP)
    tk.Label(messagebox,text=message).pack(side=tk.TOP,fill=tk.X)
    tk.Button(messagebox,text='Ok',command=messagebox.destroy).pack(side=tk.TOP)
    messagebox.mainloop()
    
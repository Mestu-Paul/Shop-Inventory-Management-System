import tkinter as tk
from PIL import ImageTk, Image
import re as regex
import datetime as dt 

import DAO as dao 
import color_code as color

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
    
    message_icon = ImageTk.PhotoImage(Image.open(f"img/{message_type}.png").resize((50,50)))
    tk.Label(messageBox,bg='#ffffff', image=message_icon).place(relx=0,rely=0.0,relwidth=0.3,relheight=0.75)

    text = tk.Text(messageBox,wrap=tk.WORD,bd=0)
    text.place(relx=0.3,rely=0,relwidth=0.7,relheight=0.75)
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
    

shop_name = None
phone = None
email = None
owner = None   
def init_page(root,page_name):
    # ============================ top frame 0 ============================
    top_frame_0 = tk.Frame(root,bg=color.color_list[0])
    top_frame_0.place(relx=0,rely=0,relwidth=1,relheight=0.12)
    # ---------------------------------------------------------------------
    # logo  (at frame 0)
    
    global shop_name,phone,email,owner
    if shop_name==None:
        print('retrieve')
        message = dao.get_rows("SELECT * FROM basic;",[])
        if message[0]==0:
            show_message('error',f'While retreiving basic info {message[1]}')
            return
        message= message[1][0]
        print(message)
        shop_name = message[0]
        owner = message[1]
        phone = message[2]
        email = message[3]

    
    root.shop_logo = ImageTk.PhotoImage(Image.open("img/logo.png").resize((50,50)))
    top0_frame_0_lbl_0 = tk.Label(top_frame_0, image = root.shop_logo)
    top0_frame_0_lbl_0.place(relx=0.01, rely=0.1, relwidth=0.05, relheight=0.7)

    # shop name (at frame 0)
    top0_frame_0_lbl_1 = tk.Label(top_frame_0,text=shop_name , fg=color.color_list[1], bg=color.color_list[0], font=("Comic Sans MS", 20, "bold"))
    top0_frame_0_lbl_1.place(relx=0.07, rely=0.2)

    # shop owner's info (at frame 0)
    top0_frame_0_lbl_2 = tk.Label(top_frame_0,text=f"Mobile: {phone}\nEmail: {email}\nOwner: {owner}" , fg=color.color_list[1], bg=color.color_list[0], font=("Times New Roman", 12))
    top0_frame_0_lbl_2.place(relx=0.8, rely=0.1)
    
    # page name 
    top0_frame_0_lbl_3 = tk.Label(top_frame_0,text=page_name , fg=color.color_list[1], bg=color.color_list[0], font=("Times New Roman", 17,"bold"))
    top0_frame_0_lbl_3.place(relx=0.43, rely=0.3)




    # ============================ top frame 1 ============================
    top_frame_1 = tk.Frame(root,bg=color.color_list[2])
    top_frame_1.place(relx=0,rely=0.12,relwidth=1,relheight=0.05)
    # ---------------------------------------------------------------------
    # welcome  (at frame 1)
    top_frame_1_lbl_0 = tk.Label(top_frame_1,text="Welcome to abc Fasion House" , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_0.pack(side=tk.LEFT,padx=50)

    # date (at frame 1)
    cur_date = dt.date.today().strftime("%B %d, %Y")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_date , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # time (at frame 1)
    cur_time = dt.datetime.now().strftime("%I:%M:%S %p")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_time , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # tittle (at frame 1)
    # top_frame_1_lbl_1 = tk.Label(top_frame_1,text="Home" , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    # top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

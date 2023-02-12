import tkinter as tk
from PIL import ImageTk, Image
import re as regex
import datetime as dt 
import time
import threading


import DAO as dao 
import color_code as color
    
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
    
    button_frame = [tk.Frame(messageBox,bg=color.getColor('bd_button')) for i in range(1)]
    button_frame[0].place(relx=0.7,rely=0.8,width=80)
    
    btn = tk.Button(button_frame[0],text='Ok',bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), bd=0, font=('helvic',10), command=messageBox.destroy)
    btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
    button_hover(button_frame[0],btn)
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
    

def hover(event,l1,c1,l2=None,c2=None):
    l1.config(bg=c1)
    if l2:
        l2.config(bg=c2)
    
def button_hover(frame,button):
    button.bind("<Enter>",lambda e,l1=frame, c1=color.getColor('bd_button-h'),l2=button, c2=color.getColor('bg_button-h'):hover(e, l1, c1, l2, c2))
    button.bind("<Leave>",lambda e,l1=frame, c1=color.getColor('bd_button'),l2=button, c2=color.getColor('bg_button'):hover(e, l1, c1, l2, c2))

def button_hover_menu(frame,button):
    button.bind("<Enter>",lambda e,l1=frame, c1=color.getColor('bd_menu-button-h'),l2=button, c2=color.getColor('bg_menu-button-h'):hover(e, l1, c1, l2, c2))
    button.bind("<Leave>",lambda e,l1=frame, c1=color.getColor('bd_menu-button'),l2=button, c2=color.getColor('bg_menu-button'):hover(e, l1, c1, l2, c2))

def button_hover_del(frame,button):
    button.bind("<Enter>",lambda e,l1=frame, c1=color.getColor('bd_button_del-h'),l2=button, c2=color.getColor('bg_button_del-h'):hover(e, l1, c1, l2, c2))
    button.bind("<Leave>",lambda e,l1=frame, c1=color.getColor('bd_button'),l2=button, c2=color.getColor('bg_button'):hover(e, l1, c1, l2, c2))

def input_hover(frame,entry):
    entry.bind("<FocusIn>",lambda e,l1=frame, c1=color.getColor('bd_input-h'):hover(e, l1, c1))
    entry.bind("<FocusOut>",lambda e,l1=frame, c1=color.getColor('bd_input'):hover(e, l1, c1))


shop_name = None
phone = None
email = None
owner = None   

        
        
def init_page(root,page_name):
    try:
        # ============================ top frame 0 ============================
        top_frame_0 = tk.Frame(root,bg=color.getColor('bg_main1'))
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
        top0_frame_0_lbl_1 = tk.Label(top_frame_0,text=shop_name , bg=color.getColor('bg_main1'), fg=color.getColor('fg_main1'), font=("Comic Sans MS", 20, "bold"))
        top0_frame_0_lbl_1.place(relx=0.07, rely=0.2)

        # shop owner's info (at frame 0)
        top0_frame_0_lbl_2 = tk.Label(top_frame_0,text=f"Mobile: {phone}\nEmail: {email}\nOwner: {owner}" , bg=color.getColor('bg_main1'), fg=color.getColor('fg_main1'), font=("Times New Roman", 12))
        top0_frame_0_lbl_2.place(relx=0.8, rely=0.1)
        


        # ============================ top frame 1 ============================
        top_frame_1 = tk.Frame(root,bg=color.getColor('bg_main2'))
        top_frame_1.place(relx=0,rely=0.12,relwidth=1,relheight=0.05)
        # ---------------------------------------------------------------------
        
        cur_date = dt.date.today().strftime("%B %d, %Y")
        cur_time = dt.datetime.now().strftime("%I:%M:%S %p")
        name_list = [f'Welcome to {shop_name}',cur_date,cur_time,page_name]
        
        lbl_list = [tk.Label(top_frame_1, bg=color.getColor('bg_main2'), fg=color.getColor('fg_main2'), font=("Comic Sans MS",12)
                ) for i in range(len(name_list))]
    except Exception as e:
        show_message('error',f'Found an exception while set init page {e}')
    
    def show_time():
        current_time = time.strftime("%H:%M:%S %p")
        lbl_list[2].config(text=current_time)
        root.after(1000,show_time)
    show_time()

    for i,lbl in enumerate(lbl_list):
        lbl.pack(side=tk.LEFT,padx=50)
        lbl.config(text=name_list[i])

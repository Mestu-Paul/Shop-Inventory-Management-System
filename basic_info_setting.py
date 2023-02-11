import tkinter as tk

import color_code as color
import DAO as dao 
import help_functions as _help

def close_basic_setting(root):
    root.destroy()
    
def updateBasicInfo():
    global basic_info_entries
    values = [entry.get() for entry in basic_info_entries]
    for value in values:
        if len(value)==0:
            _help.show_message('warning','Please all fields')
            return
    
    command = "UPDATE basic SET shop_name=?,owner_name=?,phone=?,email=?"
    message = dao.set_rows(command,values)
    m = 'error' if message[0]==0 else 'success'
    _help.show_message(m,message[1])
    pass

def basic_info_setting(root):
    try:
        root.root = tk.Tk()
        root.root.title('Shopping Inventory Management System')
        root.root.geometry('600x300+300+200')
        # ================= main frame =============== #
        main_frame = tk.Frame(root.root,bg='#ffffff')
        main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        # ================= top frame =============== #
        top_frame = tk.Frame(main_frame,bg=color.color_list[0])
        top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.3)

        # ----------------- label ------------------- #
        top_frame_lbl = tk.Label(top_frame,fg=color.color_list[1],text='Basic Info Setting',font=('Comic Sans MS',20), bg=color.color_list[0])
        top_frame_lbl.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.4)


        # ================= bottom frame =============== #
        botom_frame = tk.Frame(main_frame,bg=color.color_list[7])
        botom_frame.place(relx=0,rely=0.35,relwidth=1,relheight=1-0.35)
        name_list = ['Shop Name :','Owner Name :', 'Phone :','Email :']
        for i,name in enumerate(name_list):
            tk.Label(botom_frame,bg=color.color_list[7],anchor='w', text=name,font=('Times New Roman',12)
                ).place(relx=0.05,rely=0.01+0.17*i,relwidth=0.18,relheight=0.12)

        global basic_info_entries
        basic_info_entries = [tk.Entry(botom_frame) for i in range(len(name_list))]
        for i,entry in enumerate(basic_info_entries):
            entry.place(relx=0.23,rely=0.01+0.17*i,relwidth=0.6,relheight=0.12)
        

        # update button
        tk.Button(botom_frame,text='Update', font=('Times New Roma',14), bg=color.color_list[2], command=updateBasicInfo
            ).place(relx=0.6,rely=0.7,height=30)

        # close button
        tk.Button(botom_frame,text='Close', font=('Times New Roma',14), bg=color.color_list[2], command=lambda :close_basic_setting(root.root)
            ).place(relx=0.8,rely=0.7,height=30)
    except Exception as e:
        _help.show_message('error',f'Exception in basic info setting {e}')
        
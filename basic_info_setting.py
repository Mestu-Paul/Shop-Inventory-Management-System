import tkinter as tk
import color_code as color


def close_basic_setting(root):
    root.destroy()
def basic_info_setting(root):
    
    root.root = tk.Tk()
    root.root.title('Shopping Inventory Management System')
    root.root.geometry('600x300+300+200')
    # ================= main frame =============== #
    main_frame = tk.Frame(root.root,bg=color.color_list[2])
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

    botom_frame_shop_name_lbl = tk.Label(botom_frame,bg=color.color_list[7],anchor='w', text='Shop Name :',font=('Times New Roman',12))
    botom_frame_shop_name_lbl.place(relx=0.05,rely=0.01,relwidth=0.18,relheight=0.12)

    botom_frame_owner_detail_lbl = tk.Label(botom_frame,bg=color.color_list[7],anchor='w',text='Owner Details :',font=('Times New Roman',12))
    botom_frame_owner_detail_lbl.place(relx=0.05,rely=0.14,relwidth=0.18,relheight=0.12)

    botom_frame_shop_name_entry = tk.Entry(botom_frame)
    botom_frame_shop_name_entry.place(relx=0.23,rely=0.01,relwidth=0.4,relheight=0.12)

    botom_frame_owner_detail_text = tk.Text(botom_frame,height=3)
    botom_frame_owner_detail_text.place(relx=0.23,rely=0.18,relwidth=0.4,relheight=0.35)

    # update button
    botom_frame_update_btn = tk.Button(botom_frame,text='Update', font=('Times New Roma',14), bg=color.color_list[2])
    botom_frame_update_btn.place(relx=0.6,rely=0.6,height=30)

    # close button
    botom_frame_close_btn = tk.Button(botom_frame,text='Close', font=('Times New Roma',14), bg=color.color_list[2], command=lambda :close_basic_setting(root.root))
    botom_frame_close_btn.place(relx=0.8,rely=0.6,height=30)
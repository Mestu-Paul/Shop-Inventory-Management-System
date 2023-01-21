import tkinter as tk

from home import *
import color_code as color


def back_home(main_frame):
    print("back home")
    main_frame.place_forget()

def check_demage_stock(root):
    # item manage main frame
    main_frame = tk.Frame(root,bg='white')
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

    # ======================== top frame ===================== #
    top_frame = tk.Frame(main_frame,bg=color.light_grey)
    top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.35)

    # search type
    top_frame_search_lbl = tk.Label(top_frame,bg=color.light_grey, anchor='w', font=('Times New Roman',12), text='Search by :')
    top_frame_search_lbl.place(relx=0.01, rely=0.08, relwidth=0.08, relheight=0.1)

    product_search_type = tk.StringVar()
    search_type_list = ['name', "code", "company",'group']
    product_search_type.set(search_type_list[0]) # default value
    search_type = tk.OptionMenu(top_frame, product_search_type, *search_type_list)
    search_type.place(relx=0.09, rely=0.08, relwidth=0.1, relheight=0.12)

    # search box
    top_frame_lbl_1 = tk.Label(top_frame,bg=color.light_grey, anchor='w', font=('Times New Roman',12), text='Query :')
    top_frame_lbl_1.place(relx=0.01, rely=0.25, relwidth=0.08, relheight=0.1)

    query = tk.Entry(top_frame)
    query.place(relx=0.09, rely=0.25, relwidth=0.1, relheight=0.1)

    # search button
    top_frame_search_btn = tk.Button(top_frame,fg=color.color4, bg=color.color3, font=('Times New Roman',12), text='Search')
    top_frame_search_btn.place(relx=0.05, rely=0.42, relwidth=0.1, relheight=0.12)

    top_frame_refresh_btn = tk.Button(top_frame,fg=color.color4, bg=color.color3, font=('Times New Roman',12), text='Refresh')
    top_frame_refresh_btn.place(relx=0.8, rely=0.15, relwidth=0.1, relheight=0.14)

    top_frame_preview_btn = tk.Button(top_frame,fg=color.color4, bg=color.color3, font=('Times New Roman',12), text='Preview')
    top_frame_preview_btn.place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.14)

    top_frame_back_btn = tk.Button(top_frame,fg=color.color4, bg=color.color3, font=('Times New Roman',12), text='Back',command=lambda:back_home(main_frame))
    top_frame_back_btn.place(relx=0.8, rely=0.55, relwidth=0.1, relheight=0.14)


    # ======================== bottom frame ===================== #
    bottom_frame = tk.Frame(main_frame,bg=color.light_grey)
    bottom_frame.place(relx=0,rely=0.35,relwidth=1,relheight=0.65)

    # scroll bar
    scrollbar = tk.Scrollbar(bottom_frame)

    # # treeview
    tree = tk.ttk.Treeview(bottom_frame, column=("c1", "c2", "c3"), show='headings', yscrollcommand=scrollbar.set)
    # # tree.column("# 1", anchor=tk.CENTER)
    # # tree.heading("# 1", text="ID")
    # # tree.column("# 2", anchor=tk.CENTER)
    # # tree.heading("# 2", text="Company")
    # # tree.column("# 3", anchor=tk.CENTER)
    # # tree.heading("# 3", text="Company1")

    # # Insert the data in Treeview widget
    # # tree.insert('', 'end', values=('1', 'Honda', "hello"))

    tree.place(relx=0.01,rely=0,relwidth=0.97,relheight=1)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
    scrollbar.config( command = tree.yview )

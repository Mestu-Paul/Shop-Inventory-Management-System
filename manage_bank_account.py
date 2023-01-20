import tkinter as tk

from home import *

def back_home(main_frame):
    print("back home")
    main_frame.place_forget()

def manage_bank_account(root):
    # item manage main frame
    main_frame = tk.Frame(root,bg='white')
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

    # ======================== left frame ===================== #
    left_frame= tk.Frame(main_frame,bg=light_grey)
    left_frame.place(relx=0,rely=0,relwidth=0.29,relheight=1)

    account_option_list = ['Openning Date','A/C number','A/C name','A/C category',
                        'Current balance','A/C area','Contact number','Address']

    # ----------------------- label --------------------- #
    for i in range(0,len(account_option_list)):
        left_frame_lbl_0 = tk.Label(left_frame,text=account_option_list[i], bg=light_grey, font=('Times New Roman',14), anchor='w')
        left_frame_lbl_0.place(relx=0.02, rely=0.01+(0.08)*i, relwidth=0.45, relheight=0.06)

    # ---------------------- item info input ------------ #
    left_frame_entry_account_number = tk.Entry(left_frame)
    left_frame_entry_account_number.place(relx=0.48,rely=0.01,relwidth=0.5,relheight=0.06)

    left_frame_entry_account_number = tk.Entry(left_frame)
    left_frame_entry_account_number.place(relx=0.48,rely=0.09,relwidth=0.5,relheight=0.06)

    left_frame_entry_account_name = tk.Entry(left_frame)
    left_frame_entry_account_name.place(relx=0.48,rely=0.17,relwidth=0.5,relheight=0.06)

    account_type = tk.StringVar()
    account_type_list = ['Bank A/C','Customer', 'Supplier']
    account_type.set(account_type_list[0]) # default value
    account_type = tk.OptionMenu(left_frame, account_type, *account_type_list)
    account_type.place(relx=0.48,rely=0.25,relwidth=0.5,relheight=0.06)

    left_frame_entry_current_balance = tk.Entry(left_frame)
    left_frame_entry_current_balance.place(relx=0.48,rely=0.33,relwidth=0.5,relheight=0.06)

    left_frame_entry_account_area = tk.Entry(left_frame)
    left_frame_entry_account_area.place(relx=0.48,rely=0.41,relwidth=0.5,relheight=0.06)

    left_frame_entry_contact_number = tk.Entry(left_frame)
    left_frame_entry_contact_number.place(relx=0.48,rely=0.49,relwidth=0.5,relheight=0.06)

    left_frame_entry_address = tk.Text(left_frame,height=3)
    left_frame_entry_address.place(relx=0.48,rely=0.57,relwidth=0.5)

    # update button
    left_frame_btn_update = tk.Button(left_frame,text='Update', font=('Times New Roma',14), bg=color3)
    left_frame_btn_update.place(relx=0.02,rely=0.8,relwidth=0.4)

    # add button
    left_frame_btn_update = tk.Button(left_frame,text='Add A/C', font=('Times New Roma',14), bg=color3)
    left_frame_btn_update.place(relx=0.54,rely=0.8,relwidth=0.4)

    # delete button
    left_frame_btn_update = tk.Button(left_frame,text='Delete A/C', font=('Times New Roma',14,'bold'), bg='#dd0000', fg='#ffffff')
    left_frame_btn_update.place(relx=0.26,rely=0.9,relwidth=0.45)


    # ======================== right frame ===================== #
    right_frame= tk.Frame(main_frame,bg='green')
    right_frame.place(relx=0.3,rely=0,relwidth=0.7,relheight=1)

    # ======================== top frame ===================== #
    top_frame = tk.Frame(right_frame,bg=light_grey)
    top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.35)

    # search type
    top_frame_search_lbl = tk.Label(top_frame,bg=light_grey, anchor='w', font=('Times New Roman',12), text='Search by :')
    top_frame_search_lbl.place(relx=0.01, rely=0.08, relwidth=0.12, relheight=0.1)

    product_search_type = tk.StringVar()
    search_type_list = ['name', "code", "company",'group']
    product_search_type.set(search_type_list[0]) # default value
    search_type = tk.OptionMenu(top_frame, product_search_type, *search_type_list)
    search_type.place(relx=0.12, rely=0.08, relwidth=0.15, relheight=0.14)

    # search box
    top_frame_lbl_1 = tk.Label(top_frame,bg=light_grey, anchor='w', font=('Times New Roman',12), text='Query :')
    top_frame_lbl_1.place(relx=0.01, rely=0.25, relwidth=0.12, relheight=0.1)

    query = tk.Entry(top_frame)
    query.place(relx=0.12, rely=0.27, relwidth=0.15, relheight=0.12)

    # search button
    top_frame_search_btn = tk.Button(top_frame,fg=color4, bg=color3, font=('Times New Roman',12), text='Search')
    top_frame_search_btn.place(relx=0.05, rely=0.42, relwidth=0.1, relheight=0.12)

    top_frame_refresh_btn = tk.Button(top_frame,fg=color4, bg=color3, font=('Times New Roman',12), text='Refresh')
    top_frame_refresh_btn.place(relx=0.8, rely=0.15, relwidth=0.1, relheight=0.14)

    top_frame_preview_btn = tk.Button(top_frame,fg=color4, bg=color3, font=('Times New Roman',12), text='Preview')
    top_frame_preview_btn.place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.14)

    top_frame_back_btn = tk.Button(top_frame,fg=color4, bg=color3, font=('Times New Roman',12), text='Back',command=lambda:back_home(main_frame))
    top_frame_back_btn.place(relx=0.8, rely=0.55, relwidth=0.1, relheight=0.14)


    # ======================== bottom frame ===================== #
    bottom_frame = tk.Frame(right_frame,bg=light_grey)
    bottom_frame.place(relx=0,rely=0.25,relwidth=1,relheight=0.75)

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

    tree.place(relx=0.,rely=0,relwidth=0.97,relheight=1)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
    scrollbar.config( command = tree.yview )
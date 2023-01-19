import tkinter as tk



# color code 
left_bg = '#e1e1e1'
left_fg = left_bg
left_btn_bg = '#3bbd75'
right_bg = left_bg
right_fg = left_fg

def back_home(main_frame):
    print("back home")
    main_frame.place_forget()
    

def item_manage(root):
    # item manage main frame
    main_frame = tk.Frame(root,bg='white')
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
    
    item_info_list = ['Item Name :', 'Item Code :','Item Group :', 'Company :',
                    'Shelf No. :', 'Quantity :','Sale Price :','Purchase Price :']
    
    # =================== frame ========================= #
    left_frame = tk.Frame(main_frame,bg=left_bg)
    left_frame.place(relx=0.005,rely=0,relwidth=0.25, relheight=1)

    # ----------------------- label --------------------- #
    for i in range(0,len(item_info_list)):
        left_frame_lbl_0 = tk.Label(left_frame,text=item_info_list[i], bg=left_fg, font=('Times New Roman',14), anchor='w')
        left_frame_lbl_0.place(relx=0.02, rely=0.01+(0.08)*i, relwidth=0.45, relheight=0.06)
    
    # ---------------------- item info input ------------ #
    left_frame_entry_item_name = tk.Entry(left_frame)
    left_frame_entry_item_name.place(relx=0.48,rely=0.01,relwidth=0.5,relheight=0.06)

    left_frame_entry_item_code = tk.Entry(left_frame)
    left_frame_entry_item_code.place(relx=0.48,rely=0.09,relwidth=0.5,relheight=0.06)

    left_frame_entry_item_group = tk.Entry(left_frame)
    left_frame_entry_item_group.place(relx=0.48,rely=0.17,relwidth=0.5,relheight=0.06)

    left_frame_entry_company = tk.Entry(left_frame)
    left_frame_entry_company.place(relx=0.48,rely=0.25,relwidth=0.5,relheight=0.06)

    left_frame_entry_shelf_no = tk.Entry(left_frame)
    left_frame_entry_shelf_no.place(relx=0.48,rely=0.33,relwidth=0.5,relheight=0.06)

    left_frame_entry_quantity = tk.Entry(left_frame)
    left_frame_entry_quantity.place(relx=0.48,rely=0.41,relwidth=0.5,relheight=0.06)

    left_frame_entry_sale_price = tk.Entry(left_frame)
    left_frame_entry_sale_price.place(relx=0.48,rely=0.49,relwidth=0.5,relheight=0.06)

    left_frame_entry_purchase_price = tk.Entry(left_frame)
    left_frame_entry_purchase_price.place(relx=0.48,rely=0.57,relwidth=0.5,relheight=0.06)



    # update button
    left_frame_btn_update = tk.Button(left_frame,text='Update', font=('Times New Roma',14), bg=left_btn_bg)
    left_frame_btn_update.place(relx=0.02,rely=0.8,relwidth=0.4)

    # add button
    left_frame_btn_update = tk.Button(left_frame,text='Add Item', font=('Times New Roma',14), bg=left_btn_bg)
    left_frame_btn_update.place(relx=0.54,rely=0.8,relwidth=0.4)

    # delete button
    left_frame_btn_update = tk.Button(left_frame,text='Delete Item', font=('Times New Roma',14,'bold'), bg='#dd0000', fg='#ffffff')
    left_frame_btn_update.place(relx=0.26,rely=0.9,relwidth=0.45)

    # =================== frame ========================= #
    right_frame = tk.Frame(main_frame,bg=right_bg)
    right_frame.place(relx=0.26,rely=0,relwidth=0.738, relheight=1)

    right_frame_table_caption_lbl = tk.Label(right_frame,text='Item Table', font=('Times New Roma',16,'bold'),bg=right_bg)
    right_frame_table_caption_lbl.place(relx=0.4,relwidth=0.2,relheight=0.06)

    # ---------------------------- scroll table frame ----------------------------- #
    right_frame_table_frame = tk.Frame(right_frame,bg=right_bg)
    right_frame_table_frame.place(relx=0,rely=0.07,relwidth=1,relheight=0.7)

    right_frame_lbl_1 = tk.Label(right_frame,text='Search By: ',bg=right_bg,anchor='w',font=('Times New Roma',12))
    right_frame_lbl_1.place(relx=0.01,rely=0.8,relwidth=0.12)

    product_search_type = tk.StringVar()
    search_type_list = ['name', "code", "company",'group']
    product_search_type.set(search_type_list[0]) # default value
    search_type = tk.OptionMenu(right_frame, product_search_type, *search_type_list)
    search_type.config(font=('Times New Roma',12))
    search_type.place(relx=0.14, rely=0.8, relwidth=0.18,relheight=0.06)

    right_frame_lbl_2 = tk.Label(right_frame,text='Query: ',bg=right_bg,anchor='w',font=('Times New Roma',12))
    right_frame_lbl_2.place(relx=0.01,rely=0.87,relwidth=0.12)

    right_frame_entry_query = tk.Entry(right_frame)
    right_frame_entry_query.place(relx=0.14,rely=0.87,relwidth=0.18,relheight=0.05)

    # search button
    right_frame_btn_search = tk.Button(right_frame,text='Search',bg=left_btn_bg,font=('Times New Roman',12,'bold'))
    right_frame_btn_search.place(relx=0.1,rely=0.94,relwidth=0.1,relheight=0.05)

    # preview button
    right_frame_btn_privew = tk.Button(right_frame,text='Preview',bg=left_btn_bg,font=('Times New Roman',14,'bold'))
    right_frame_btn_privew.place(relx=0.4,rely=0.85,relwidth=0.11,relheight=0.06)

    # back button
    right_frame_btn_back = tk.Button(right_frame,text='Back',bg=left_btn_bg,font=('Times New Roman',14,'bold'),command=lambda:back_home(main_frame))
    right_frame_btn_back.place(relx=0.8,rely=0.85,relwidth=0.11,relheight=0.06)

    # scroll bar
    scrollbar = tk.Scrollbar(right_frame_table_frame)

    # # treeview
    tree = tk.ttk.Treeview(right_frame_table_frame, column=("c1", "c2", "c3"), show='headings', yscrollcommand=scrollbar.set)
    # # tree.column("# 1", anchor=tk.CENTER)
    # # tree.heading("# 1", text="ID")
    # # tree.column("# 2", anchor=tk.CENTER)
    # # tree.heading("# 2", text="Company")
    # # tree.column("# 3", anchor=tk.CENTER)
    # # tree.heading("# 3", text="Company1")

    # # Insert the data in Treeview widget
    # # tree.insert('', 'end', values=('1', 'Honda', "hello"))

    tree.place(relx=0,rely=0,relwidth=0.97,relheight=1)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
    scrollbar.config( command = tree.yview )

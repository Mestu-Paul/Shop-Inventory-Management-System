import tkinter as tk

import color_code as color
from home import init_page

def back_home(main_frame):
    print("back home")
    main_frame.place_forget()
def user_accessibility_manager(accessibility_frame):
    accessibility_frame_lbl = tk.Label(accessibility_frame,text='Product manage',bg=color.color_list[2],anchor='w')
    accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
    
def user_accessibility_admin(accessibility_frame):
    accessibility_frame_lbl = tk.Label(accessibility_frame,text='User manage',bg=color.color_list[2],anchor='w')
    accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
    user_accessibility_manager(accessibility_frame)
    
def user_accessibility_owner(accessibility_frame):
    accessibility_frame_lbl = tk.Label(accessibility_frame,text='Shop basic info',bg=color.color_list[2],anchor='w')
    accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
    user_accessibility_admin(accessibility_frame)
    

def user_panel(root):
    print('i am here user panal')
    init_page(root,'User Panel')
    # item manage main frameprint('i am here user panal')
    
    # =================== main frame ========================= #
    main_frame = tk.Frame(root,bg='white')
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
    
    # =================== top frame ========================= #
    top_frame = tk.Frame(main_frame,bg=color.color_list[7])
    top_frame.place(relx=0,rely=0,relwidth=1, relheight=0.3)
    
    # ----------------------- label --------------------- #
    user_info_list = ['Username :','Password :','Full Name :']
    for i in range(0,len(user_info_list)):
        top_frame_lbl = tk.Label(top_frame,text=user_info_list[i], bg=color.color_list[7], font=('Times New Roman',14), anchor='w')
        top_frame_lbl.place(relx=0.02, rely=0.1+(0.2)*i, relwidth=0.09, relheight=0.15)
    
    # # ---------------------- user info input ------------ #
    top_frame_entry_user_name = tk.Entry(top_frame)
    top_frame_entry_user_name.place(relx=0.12,rely=0.1,relwidth=0.12,relheight=0.15)

    top_frame_entry_password = tk.Entry(top_frame)
    top_frame_entry_password.place(relx=0.12,rely=0.3,relwidth=0.12,relheight=0.15)

    top_frame_entry_user_fullname = tk.Entry(top_frame)
    top_frame_entry_user_fullname.place(relx=0.12,rely=0.5,relwidth=0.12,relheight=0.15)
    
    # =================== access frame ========================= #
    top_frame_user_access_frame = tk.LabelFrame(top_frame,text='User accessibility')
    top_frame_user_access_frame.place(relx=0.35,rely=0.3,relwidth=0.12,relheight=0.7)
    def user_accessibility(event):
        for child in top_frame_user_access_frame.winfo_children():
            child.destroy()
        print(user_type.get())
        if(user_type.get()=='Owner'):
            user_accessibility_owner(top_frame_user_access_frame)
        elif(user_type.get()=='Admin'):
            user_accessibility_admin(top_frame_user_access_frame)
        else:
            user_accessibility_manager(top_frame_user_access_frame)
            
    top_frame_lbl = tk.Label(top_frame,text='User role: ', bg=color.color_list[7], font=('Times New Roman',14), anchor='w')
    top_frame_lbl.place(relx=0.26, rely=0.1, relwidth=0.09, relheight=0.15)
    
    user_type = tk.StringVar()
    user_type_list = ['Owner','Admin','Manager']
    user_type.set('Manager')
    top_frame_entry_user_type = tk.OptionMenu(top_frame,user_type,*user_type_list,command=user_accessibility)
    top_frame_entry_user_type.config(font=('Times New Roma',12))
    top_frame_entry_user_type.place(relx=0.35,rely=0.1,relwidth=0.12,relheight=0.15)

    # user add button
    top_frame_add_user_btn = tk.Button(top_frame,text='Add',bg=color.color_list[2],fg=color.color_list[3],font=('Times New Roma',12))
    top_frame_add_user_btn.place(relx=0.02,rely=0.75,relwidth=0.09,height=30)
    
    # user update button
    top_frame_update_user_btn = tk.Button(top_frame,text='Update',bg=color.color_list[2],fg=color.color_list[3],font=('Times New Roma',12))
    top_frame_update_user_btn.place(relx=0.13,rely=0.75,relwidth=0.09,height=30)
    
    # user delete button 
    top_frame_delete_user_btn = tk.Button(top_frame,text='Delete',bg=color.color_list[6],fg=color.color_list[1],font=('Times New Roma',12))
    top_frame_delete_user_btn.place(relx=0.24,rely=0.75,relwidth=0.09,height=30)
    
    # search type
    top_frame_search_lbl = tk.Label(top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Search by :')
    top_frame_search_lbl.place(relx=0.51, rely=0.1, relwidth=0.09, relheight=0.15)

    user_search_type = tk.StringVar()
    search_type_list = ['User name','User role']
    user_search_type.set(search_type_list[0]) # default value
    search_type = tk.OptionMenu(top_frame, user_search_type, *search_type_list)
    search_type.place(relx=0.61, rely=0.1, relwidth=0.1, relheight=0.15)

    # search box
    top_frame_lbl_1 = tk.Label(top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Query :')
    top_frame_lbl_1.place(relx=0.51, rely=0.3, relwidth=0.09, relheight=0.15)

    query = tk.Entry(top_frame)
    query.place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.15)

    # search button
    top_frame_search_btn = tk.Button(top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Search')
    top_frame_search_btn.place(relx=0.55, rely=0.75, relwidth=0.09, height=30)
    
    # refresh button
    top_frame_refresh_btn = tk.Button(top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Refresh')
    top_frame_refresh_btn.place(relx=0.75, rely=0.75, relwidth=0.09, height=30)
    
    # close button
    top_frame_close_btn = tk.Button(top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Back', command=lambda:back_home(main_frame))
    top_frame_close_btn.place(relx=0.86, rely=0.75, relwidth=0.09, height=30)
    
        
    # =================== bottom frame ========================= #
    bottom_frame = tk.Frame(main_frame,bg=color.color_list[7])
    bottom_frame.place(relx=0,rely=0.31,relwidth=1,relheight=.69)
    
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

    tree.place(relx=0.003,rely=0,relwidth=0.97,relheight=1)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
    scrollbar.config( command = tree.yview )
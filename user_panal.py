import tkinter as tk
import re as regex
from PIL import ImageTk, Image
# from tkinter import ttk

import color_code as color
# from home import init_page
import home as _home
import help_functions as _help_functions
import DAO as dao

class User_Panel():
    def __init__(self,root):
        self.root = root
        # self.user_panel()
    def user_panel(self):
        print('i am here user panal')
        try:
            _home.init_page(self.root,'User Panel')
            # item manage main frameprint('i am here user panal')
            
            # =================== main frame ========================= #
            self.main_frame = tk.Frame(self.root,bg='white')
            self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
            
            # =================== top frame ========================= #
            self.top_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
            self.top_frame.place(relx=0,rely=0,relwidth=1, relheight=0.3)
            
            # ----------------------- label --------------------- #
            user_info_list = ['Username :','Password :','Full Name :']
            for i in range(0,len(user_info_list)):
                top_frame_lbl = tk.Label(self.top_frame,text=user_info_list[i], bg=color.color_list[7], font=('Times New Roman',14), anchor='w')
                top_frame_lbl.place(relx=0.02, rely=0.1+(0.2)*i, relwidth=0.09, relheight=0.15)
            
            # # ---------------------- user info input ------------ #
            self.top_frame_entry_user_name = tk.Entry(self.top_frame)
            self.top_frame_entry_user_name.place(relx=0.12,rely=0.1,relwidth=0.12,relheight=0.15)

            self.top_frame_entry_password = tk.Entry(self.top_frame,show='*')
            self.top_frame_entry_password.place(relx=0.12,rely=0.3,relwidth=0.12,relheight=0.15)

            self.open_eye = ImageTk.PhotoImage(Image.open("img/eye_open.png").resize((20,17)))
            self.closed_eye = ImageTk.PhotoImage(Image.open("img/eye_close.png").resize((20,17)))
            self.toggle_button = tk.Button(self.top_frame, image=self.closed_eye, command=self.toggle_password)
            self.toggle_button.place(relx=0.24,rely=0.3,relwidth=0.02,relheight=0.15)
            
            self.top_frame_entry_user_fullname = tk.Entry(self.top_frame)
            self.top_frame_entry_user_fullname.place(relx=0.12,rely=0.5,relwidth=0.12,relheight=0.15)
            
            
            # =================== access frame ========================= #
            self.top_frame_user_access_frame = tk.LabelFrame(self.top_frame,text='User accessibility')
            self.top_frame_user_access_frame.place(relx=0.35,rely=0.3,relwidth=0.12,relheight=0.7)



            
            self.top_frame_lbl = tk.Label(self.top_frame,text='User role: ', bg=color.color_list[7], font=('Times New Roman',14), anchor='w')
            self.top_frame_lbl.place(relx=0.26, rely=0.1, relwidth=0.09, relheight=0.15)
            
            self.user_type = tk.StringVar()
            user_type_list = ['Owner','Admin','Manager']
            self.user_type.set('Manager')
            self.top_frame_entry_user_type = tk.OptionMenu(self.top_frame,self.user_type,*user_type_list,command=self.user_accessibility)

            self.top_frame_entry_user_type.config(font=('Times New Roma',12))
            self.top_frame_entry_user_type.place(relx=0.35,rely=0.1,relwidth=0.12,relheight=0.15)
            
            # user add button
            self.top_frame_add_user_btn = tk.Button(self.top_frame,text='Add',bg=color.color_list[2],fg=color.color_list[3],font=('Times New Roma',12),command=self.add_new_user)
            self.top_frame_add_user_btn.place(relx=0.02,rely=0.75,relwidth=0.09,height=30)
            
            # user update button
            self.top_frame_update_user_btn = tk.Button(self.top_frame,text='Update',bg=color.color_list[2],fg=color.color_list[3],font=('Times New Roma',12),command=self.update_user)
            self.top_frame_update_user_btn.place(relx=0.13,rely=0.75,relwidth=0.09,height=30)
            
            # user delete button 
            self.top_frame_delete_user_btn = tk.Button(self.top_frame,text='Delete',bg=color.color_list[6],fg=color.color_list[1],font=('Times New Roma',12),command=self.delete_user)
            self.top_frame_delete_user_btn.place(relx=0.24,rely=0.75,relwidth=0.09,height=30)
            
            # search type
            self.top_frame_search_lbl = tk.Label(self.top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Search by :')
            self.top_frame_search_lbl.place(relx=0.51, rely=0.1, relwidth=0.09, relheight=0.15)

            user_search_type = tk.StringVar()
            search_type_list = ['User name','User role']
            user_search_type.set(search_type_list[0]) # default value
            search_type = tk.OptionMenu(self.top_frame, user_search_type, *search_type_list)
            search_type.place(relx=0.61, rely=0.1, relwidth=0.1, relheight=0.15)

            # search box
            self.top_frame_lbl_1 = tk.Label(self.top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Query :')
            self.top_frame_lbl_1.place(relx=0.51, rely=0.3, relwidth=0.09, relheight=0.15)

            self.query = tk.Entry(self.top_frame)
            self.query.place(relx=0.61, rely=0.3, relwidth=0.1, relheight=0.15)

            # search button
            self.top_frame_search_btn = tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Search')
            self.top_frame_search_btn.place(relx=0.55, rely=0.75, relwidth=0.09, height=30)
            
            # refresh button
            self.top_frame_refresh_btn = tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Refresh',command=self.user_panel)
            self.top_frame_refresh_btn.place(relx=0.75, rely=0.75, relwidth=0.09, height=30)
            
            # close button
            self.top_frame_close_btn = tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Back', command=lambda:self.back_home(self.main_frame))
            self.top_frame_close_btn.place(relx=0.86, rely=0.75, relwidth=0.09, height=30)
            
                
            # =================== bottom frame ========================= #
            self.bottom_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
            self.bottom_frame.place(relx=0,rely=0.31,relwidth=1,relheight=.69)
            self.show_table()
        except Exception as e:
            _help_functions.show_message("warning",e)
            return
        
    def show_table(self):
        self.tree = tk.ttk.Treeview(self.bottom_frame, columns=("col2", "col3","col4"))
        # Define the columns for the table
        self.tree.heading("#0", text="Serial No.")
        # self.tree.heading("col1", text="Email")
        self.tree.heading("col2", text="user_name")
        self.tree.heading("col3", text="full name")
        self.tree.heading("col4", text="role")

        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="grey")
        self.tree.tag_configure("red_green", background="white")
        user_panel_user_info = dao.get_user_panel()
        print(user_panel_user_info)
        if user_panel_user_info[0]==0:
            print(user_panel_user_info[1])
            _help_functions.show_message('warning',user_panel_user_info[1])
        else:
            for i in range(0,len(user_panel_user_info[1])):
                values_list = [user_panel_user_info[1][i][0],user_panel_user_info[1][i][3],user_panel_user_info[1][i][4]]
                self.tree.insert("",tk.END,text=(str)(i+1),values=values_list,tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    def add_new_user(self):
        message_type=['error','success']
        user_info = [self.top_frame_entry_user_name.get(),self.top_frame_entry_password.get(),self.top_frame_entry_user_fullname.get(),self.user_type.get()]
        if len(user_info)!=4:
            _help_functions.show_message(message_type[0],"Please fill all the fields")
            return
        for info in user_info:
            print(info)
        for info in user_info:
            if len(info)==0:
                _help_functions.show_message(message_type[0],"Please fill all the fields")
                print(user_info)
                return
            elif regex.match("^[a-zA-Z\s]+$",info)==None:
                _help_functions.show_message(message_type[0],"You can not use any special character")
                return
        message = dao.set_user_panel(user_info)
        print(message)
        _help_functions.show_message(message_type[message[0]],message[1])
        self.user_panel()
            
    
    def update_user(self):
        message_type=['error','success']
        user_info = [self.user_name_to_query,self.top_frame_entry_password.get(),self.top_frame_entry_user_fullname.get(),self.user_type.get()]
        if len(user_info)!=4:
            _help_functions.show_message(message_type[0],"Please fill all the fields")
            return
        for info in user_info:
            print(info)
        for info in user_info:
            if len(info)==0:
                _help_functions.show_message(message_type[0],"Please fill all the fields")
                print(user_info)
                return
            elif regex.match("^[a-zA-Z\s]+$",info)==None:
                _help_functions.show_message(message_type[0],"You can not use any special character")
                return
        message = dao.updater_user_panel(user_info)
        print(message)
        _help_functions.show_message(message_type[message[0]],message[1])
        self.user_panel()
        
    
    def delete_user(self):
        message_type=['error','success']
        message = dao.delete_row_of_a_table("user_panel","user_name",self.user_name_to_query)
        print(message)
        _help_functions.show_message(message_type[message[0]],message[1])
        self.user_panel()
    
    
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
        
        
    def on_select(self,event):
        # Get the selected items
        selected_items = self.tree.selection()
        
        # Iterate through the selected items
        for item in selected_items:
            # Get the values of the selected item
            item_values = self.tree.item(item)["values"]
            print(item_values)
            self.user_name_to_query = item_values[0]
            self.set_entry_value(self.top_frame_entry_user_name,item_values[0])
            self.set_entry_value(self.top_frame_entry_user_fullname,item_values[1])
            self.user_type.set(item_values[2])
            self.user_accessibility(event)
            
    def toggle_password(self):
        if self.top_frame_entry_password["show"] == "*":
            self.top_frame_entry_password["show"] = ""
            self.toggle_button.config(image=self.open_eye)
        else:
            self.top_frame_entry_password["show"] = "*"
            self.toggle_button.config(image=self.closed_eye)
  
    def user_accessibility(self,event):
        for child in self.top_frame_user_access_frame.winfo_children():
            child.destroy()
        print(self.user_type.get())
        if(self.user_type.get()=='Owner'):
            self.user_accessibility_owner(self.top_frame_user_access_frame)
        elif(self.user_type.get()=='Admin'):
            self.user_accessibility_admin(self.top_frame_user_access_frame)
        else:
            self.user_accessibility_manager(self.top_frame_user_access_frame)
            
            
    def user_accessibility_manager(self,accessibility_frame):
        accessibility_frame_lbl = tk.Label(accessibility_frame,text='Product manage',bg=color.color_list[2],anchor='w')
        accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
        
        
    def user_accessibility_admin(self,accessibility_frame):
        accessibility_frame_lbl = tk.Label(accessibility_frame,text='User manage',bg=color.color_list[2],anchor='w')
        accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
        self.user_accessibility_manager(accessibility_frame)
        
        
    def user_accessibility_owner(self,accessibility_frame):
        accessibility_frame_lbl = tk.Label(accessibility_frame,text='Shop basic info',bg=color.color_list[2],anchor='w')
        accessibility_frame_lbl.pack(side=tk.TOP,fill=tk.X,padx=5,pady=2)
        self.user_accessibility_admin(accessibility_frame)
    
        
    def back_home(self):
        print("back home")
        self.main_frame.place_forget()

# root = tk.Tk()
# obj = User_Panel(root)
# obj.user_accessibility()    
# root.geometry('1100x650+10+10')        
# user_panel(root)
# root.mainloop()
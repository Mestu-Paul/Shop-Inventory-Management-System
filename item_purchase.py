import tkinter as tk
import tkcalendar as tkcal

import color_code as color
import item_manage as item_manage
import DAO as dao
import help_functions as _help_functions

class Item_Purchase:
    def __init__(self,root) -> None:
        self.root = root
        self.message_type=['error','success']
        self.item_manage_obj = item_manage.Item_Manage(root)
        
    
    def backHome(self):
        print("back home")
        self.main_frame.place_forget()
    
    def get_values(self):
        values = []
        values.append(self.left_frame_entry_item_name.get())
        values.append(self.left_frame_entry_item_code.get())
        values.append(self.left_frame_entry_item_date.get())
        values.append(self.left_frame_entry_item_group.get())
        values.append(self.left_frame_entry_company.get())
        values.append(self.left_frame_entry_shelf_no.get())
        values.append(self.left_frame_entry_quantity.get())
        values.append(self.left_frame_entry_sale_price.get())
        values.append(self.left_frame_entry_purchase_price.get())
        return values
        
    def add_item_to_db(self):
        values = self.get_values()
        if self.is_valid(values)==False:
            return
        print("values ",values)
        command = "INSERT INTO item_details VALUES(?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print(message)
        self.show_table()
        self.clear_input()
        _help_functions.show_message(self.message_type[message[0]],message[1])
        pass
    
    def update_item(self):
        try:
            values = self.get_values()
            # values = [self.item_code_to_query,self.top_frame_entry_password.get(),self.top_frame_entry_user_fullname.get(),self.user_type.get()]
            # if self.is_valid(values)==False:
            #     return
            command = "UPDATE item_details SET item_name = ?,item_date = ?,item_group = ?,item_company = ?,item_shelf_no = ?,item_quantity = ?,item_sale_price = ?,item_purchase_price = ? WHERE item_code=?;"
            message = dao.update_rows(command,values)
            print(message)
            self.clear_input()
            _help_functions.show_message(self.message_type[message[0]],message[1])
        except AttributeError:
            _help_functions.show_message(self.message_type[0],"Please select one")
        except Exception as e:
            _help_functions.show_message(self.message_type[0],e)
    
    def delete_item(self):
        try:
            command = "DELETE FROM item_details WHERE item_code = ?;"
            values = [self.item_code_to_query]
            message = dao.delete_rows(command,values)
            print(message)
            _help_functions.show_message(self.message_type[message[0]],message[1])
        except AttributeError:
            _help_functions.show_message(self.message_type[0],"Please select one")
        except Exception as e:
            _help_functions.show_message(self.message_type[0],e)
    
    
    def item_purchase(self,root):
        # item manage main frame
        self.main_frame = tk.Frame(root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

        # ============================ left frame 1 ============================
        left_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        left_frame.place(relx=0.01,rely=0, relwidth=0.28, relheight=1)

        # ----------------------------------------------------------------------#
        purchase_date = tkcal.DateEntry(left_frame,selecmode='day', cursor='hand1')
        purchase_date.place(relx=0.55,y=5,relwidth=0.4)

        item_info_list = ['Item Name :', 'Item Code :','Item Group :', 'Company :',
                        'Shelf No. :', 'Quantity :','Sale Price :','Purchase Price :','Date :']


        for itm in range(0,len(item_info_list)):
            left_frame_lbl_0 = tk.Label(left_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text=item_info_list[itm])
            left_frame_lbl_0.place(relx=0.02, rely=0.01+(0.08)*itm, relwidth=0.45, relheight=0.06)


        # delete item
        left_frame_btn_delete = tk.Button(left_frame, fg=color.color_list[3], bg=color.color_list[2],font=('Times New Roman',14), text='Delete')
        left_frame_btn_delete.place(relx=0.02,rely=0.92, height=25)

        self.check_free = tk.IntVar()
        tk.Checkbutton(left_frame, bg=color.color_list[2], font=('Times New Roman',14), text='Free', variable=self.check_free).place(relx=0.37,rely=0.92,height=25)
        # add item to sell
        left_frame_btn_add = tk.Button(left_frame, fg=color.color_list[3], bg=color.color_list[2],font=('Times New Roman',14), text='Add item')
        left_frame_btn_add.place(relx=0.7,rely=0.92, height=25)



        # --------------------------------product input box------------------------------- #

        self.left_frame_entry_item_name = tk.Entry(left_frame)
        self.left_frame_entry_item_name.place(relx=0.48,rely=0.01,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_item_code = tk.Entry(left_frame)
        self.left_frame_entry_item_code.place(relx=0.48,rely=0.09,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_item_group = tk.Entry(left_frame)
        self.left_frame_entry_item_group.place(relx=0.48,rely=0.17,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_company = tk.Entry(left_frame)
        self.left_frame_entry_company.place(relx=0.48,rely=0.25,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_shelf_no = tk.Entry(left_frame)
        self.left_frame_entry_shelf_no.place(relx=0.48,rely=0.33,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_quantity = tk.Entry(left_frame)
        self.left_frame_entry_quantity.place(relx=0.48,rely=0.41,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_sale_price = tk.Entry(left_frame)
        self.left_frame_entry_sale_price.place(relx=0.48,rely=0.49,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_purchase_price = tk.Entry(left_frame)
        self.left_frame_entry_purchase_price.place(relx=0.48,rely=0.57,relwidth=0.5,relheight=0.06)

        self.left_frame_entry_item_date = tkcal.DateEntry(left_frame,selecmode='day', cursor='hand1')
        self.left_frame_entry_item_date.place(relx=0.48,rely=0.65,relwidth=0.5,relheight=0.06)



        # ============================ right frfame ============================ #
        right_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        right_frame.place(relx=0.3,rely=0,relwidth=0.69,relheight=1)

        purchase_font = 12
        # ---------------------------- customer info frame ----------------------------- #
        right_frame_customer_info_frame = tk.Frame(right_frame,bg=color.color_list[7])
        right_frame_customer_info_frame.place(relx=0.01,rely=0.01,relwidth=0.48,relheight=0.6)

        # ---------------------------- label --------------------------#
        # search type
        right_frame_customer_info_frame_lbl_0 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Search by :')
        right_frame_customer_info_frame_lbl_0.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.08)

        # search box
        right_frame_customer_info_frame_lbl_1 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Query :')
        right_frame_customer_info_frame_lbl_1.place(relx=0.01, rely=0.1, relwidth=0.4, relheight=0.08)

        # search button
        right_frame_customer_info_frame_btn_search = tk.Button(right_frame_customer_info_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Search')
        right_frame_customer_info_frame_btn_search.place(relx=0.25, rely=0.2, relwidth=0.4, relheight=0.08)

        # customer name 
        right_frame_customer_info_frame_lbl_2 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Name :')
        right_frame_customer_info_frame_lbl_2.place(relx=0.01, rely=0.3, relwidth=0.4, relheight=0.08)

        # customer pre-balance
        right_frame_customer_info_frame_lbl_3 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Pre-balance :')
        right_frame_customer_info_frame_lbl_3.place(relx=0.01, rely=0.4, relwidth=0.4, relheight=0.08)

        # customer current balance
        right_frame_customer_info_frame_lbl_4 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Current-balance :')
        right_frame_customer_info_frame_lbl_4.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.08)

        # customer contact no
        right_frame_customer_info_frame_lbl_5 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Contact :')
        right_frame_customer_info_frame_lbl_5.place(relx=0.01, rely=0.6, relwidth=0.4, relheight=0.08)

        payment_button = tk.Button(right_frame_customer_info_frame,text='Payment', bg=color.color_list[2])
        payment_button.place(relx=0.8,rely=0.9,height=30)
        tk.Button(right_frame_customer_info_frame,text='Back', bg=color.color_list[2]\
            ,command=self.backHome).place(relx=0.2,rely=0.9,height=30)

        # ---------------------------- Input ------------------------------ #
        self.product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(right_frame_customer_info_frame, self.product_search_type, *search_type_list)
        search_type.place(relx=0.3, rely=0.01, relwidth=0.6, relheight=0.09)

        self.query = tk.Entry(right_frame_customer_info_frame)
        self.query.place(relx=0.3, rely=0.11, relwidth=0.6, relheight=0.08)

        self.customer_name = tk.Entry(right_frame_customer_info_frame)
        self.customer_name.place(relx=0.42, rely=0.3, relwidth=0.48, relheight=0.08)

        self.pre_balance = tk.Entry(right_frame_customer_info_frame)
        self.pre_balance.place(relx=0.42, rely=0.4, relwidth=0.48, relheight=0.08)

        self.current_balance = tk.Entry(right_frame_customer_info_frame)
        self.current_balance.place(relx=0.42, rely=0.5, relwidth=0.48, relheight=0.08)

        self.contact_no = tk.Entry(right_frame_customer_info_frame)
        self.contact_no.place(relx=0.42, rely=0.6, relwidth=0.48, relheight=0.08)


        # ---------------------------- payment info frame ----------------------------- #
        right_frame_frame_payment_info = tk.Frame(right_frame,bg=color.color_list[7])
        right_frame_frame_payment_info.place(relx=0.5,rely=0.01,relwidth=0.49,relheight=0.6)

        purchase_info_list = ['Total Item :', 'Total Price :', 'Discount :',
                            'Payable :', 'Total Paid :', 'Change/Due :']
        for i in range(0,len(purchase_info_list)):
            right_frame_frame_payment_info_lbl = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text=purchase_info_list[i])
            right_frame_frame_payment_info_lbl.place(relx=0.01, rely=0.01+0.1*i, relwidth=0.4, relheight=0.08)     



        # total item 
        self.right_frame_frame_payment_info_lbl_total_item = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
        self.right_frame_frame_payment_info_lbl_total_item.place(relx=0.42, rely=0.01, relwidth=0.4, relheight=0.08)

        # total price
        self.right_frame_frame_payment_info_lbl_total_price = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Total price :')
        self.right_frame_frame_payment_info_lbl_total_price.place(relx=0.42, rely=0.1, relwidth=0.4, relheight=0.08)

        # discount 
        self.right_frame_frame_payment_info_lbl_discount = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
        self.right_frame_frame_payment_info_lbl_discount.place(relx=0.42, rely=0.2, relwidth=0.4, relheight=0.08)

        # Payable
        self.right_frame_frame_payment_info_lbl_payable = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
        self.right_frame_frame_payment_info_lbl_payable.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)

        # total paid
        self.right_frame_frame_payment_info_lbl_total_paid = tk.Entry(right_frame_frame_payment_info)
        self.right_frame_frame_payment_info_lbl_total_paid.place(relx=0.42, rely=0.4, relwidth=0.4, relheight=0.08)

        # change/due
        self.right_frame_frame_payment_info_lbl_change = tk.Label(right_frame_frame_payment_info,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
        self.right_frame_frame_payment_info_lbl_change.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.08)

        # =================== frame ====================== #
        right_frame_frame_payment_info_frame_payment_acount = tk.Frame(right_frame_frame_payment_info,bg=color.color_list[7])

        def payment_method_select(event):
            right_frame_frame_payment_info_frame_payment_acount_lbl_payment_acount = tk.Label(right_frame_frame_payment_info_frame_payment_acount, bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Payment A/C :')
            if(payment_method_type.get()=='Cash'):
                right_frame_frame_payment_info_frame_payment_acount.place_forget()
                return
            
            right_frame_frame_payment_info_frame_payment_acount.place(relx=0,rely=0.6,relwidth=1,relheight=0.4)
            # payment account
            right_frame_frame_payment_info_frame_payment_acount_lbl_payment_acount.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.2)
            payment_acount_number = tk.StringVar()
            payment_acount_number_list = ['Name1', "Name2", "Name3",'Name4']
            payment_acount_number.set(payment_acount_number_list[0]) # default value
            payment_acount = tk.OptionMenu(right_frame_frame_payment_info_frame_payment_acount, payment_acount_number, *payment_acount_number_list,command=payment_method_select)
            payment_acount.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.2)
            default_payment_account = tk.IntVar()
            tk.Checkbutton(right_frame_frame_payment_info_frame_payment_acount, bg=color.color_list[7], font=('Times New Roman',purchase_font), text='Set aa default', variable=default_payment_account).place(relx=0.6,rely=0.7)



        # payment method
        right_frame_customer_info_frame_lbl_6 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',10), text='Payment method :')
        right_frame_customer_info_frame_lbl_6.place(relx=0.01, rely=0.8, relwidth=0.4, relheight=0.08)
        payment_method_type = tk.StringVar()
        payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
        payment_method_type.set(payment_method_type_list[0]) # default value
        payment_method = tk.OptionMenu(right_frame_customer_info_frame, payment_method_type, *payment_method_type_list,command=payment_method_select)
        payment_method.place(relx=0.42, rely=0.8, relwidth=0.4, relheight=0.09)



        # ---------------------------- scroll table frame ----------------------------- #
        right_frame_frame_table = tk.Frame(right_frame)
        right_frame_frame_table.place(relx=0,rely=0.62,relwidth=1,relheight=0.4)

        # scroll bar
        scrollbar = tk.Scrollbar(right_frame_frame_table)
        scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)

        # treeview
        tree = tk.ttk.Treeview(right_frame_frame_table, column=("c1", "c2", "c3"), show='headings', yscrollcommand=scrollbar.set)
        # tree.column("# 1", anchor=tk.CENTER)
        # tree.heading("# 1", text="ID")
        # tree.column("# 2", anchor=tk.CENTER)
        # tree.heading("# 2", text="Company")
        # tree.column("# 3", anchor=tk.CENTER)
        # tree.heading("# 3", text="Company1")

        # Insert the data in Treeview widget
        # tree.insert('', 'end', values=('1', 'Honda', "hello"))

        tree.place(relx=0,rely=0,relwidth=0.97,relheight=1)
        scrollbar.config( command = tree.yview )

import tkinter as tk
import tkcalendar as tkcal

import help_functions as _help_functions
import DAO as dao
import color_code as color

class Item_Manage:
    def __init__(self,root):
        self.root = root
        self.message_type=['error','success']
        # self.item_manage(self.root)
    def back_home(self):
        print("back home")
        self.main_frame.place_forget()
        
        
    def is_valid(self,values):
        for v in values:
            if len(v)==0:
                _help_functions.show_message('error','Please fill all the fields')
                return False
        if _help_functions.is_alpha([values[0],values[3],values[4]])==False:
            _help_functions.show_message('error','Please fill Name, Group and Company carefully.\nYou should use only alphabate')
            return False
        if _help_functions.is_number([values[6],values[7],values[8]])==False:
            _help_functions.show_message('error','Please fill Quantity, Sale price and purchase price carefully.\nYou should use only number')
            return False
        # if (int)(values[7])<=(int)(values[8]):
        #     _help_functions.show_message('warning','Sale price is lower than purchase price SD')
        if _help_functions.is_alphanum([values[1],values[5]])==False:
            _help_functions.show_message('error','Please fill Code and Shelf No. carefully.\nYou should use only alphanumeric')
            return
        return True
    def add_item_to_db(self):
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
        if self.is_valid(values)==False:
            return
        print("values ",values)
        command = "INSERT INTO item_details VALUES(?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print(message)
        _help_functions.show_message(self.message_type[message[0]],message[1])
        self.show_table()
        pass
    
    def update_item(self):
        try:
            values = []
            values.append(self.left_frame_entry_item_name.get())
            values.append(self.left_frame_entry_item_date.get())
            values.append(self.left_frame_entry_item_group.get())
            values.append(self.left_frame_entry_company.get())
            values.append(self.left_frame_entry_shelf_no.get())
            values.append(self.left_frame_entry_quantity.get())
            values.append(self.left_frame_entry_sale_price.get())
            values.append(self.left_frame_entry_purchase_price.get())
            values.append(self.item_code_to_query)
            # values = [self.item_code_to_query,self.top_frame_entry_password.get(),self.top_frame_entry_user_fullname.get(),self.user_type.get()]
            # if self.is_valid(values)==False:
            #     return
            command = "UPDATE item_details SET item_name = ?,item_date = ?,item_group = ?,item_company = ?,item_shelf_no = ?,item_quantity = ?,item_sale_price = ?,item_purchase_price = ? WHERE item_code=?;"
            message = dao.update_rows(command,values)
            print(message)
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
            
    def item_manage(self,root):
        # item manage main frame
        self.main_frame = tk.Frame(root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        item_info_list = ['Item Name :', 'Item Code :','Item Group :', 'Company :',
                        'Shelf No. :', 'Quantity :','Sale Price :','Purchase Price :','Date :']
        
        # =================== frame ========================= #
        left_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        left_frame.place(relx=0.005,rely=0,relwidth=0.25, relheight=1)

        # ----------------------- label --------------------- #
        for i in range(0,len(item_info_list)):
            left_frame_lbl_0 = tk.Label(left_frame,text=item_info_list[i], bg=color.color_list[7], font=('Times New Roman',14), anchor='w')
            left_frame_lbl_0.place(relx=0.02, rely=0.01+(0.08)*i, relwidth=0.45, relheight=0.06)
        
        # ---------------------- item info input ------------ #
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

        # update button
        self.left_frame_btn_update = tk.Button(left_frame,text='Update', font=('Times New Roma',14), bg=color.color_list[2],command=self.update_item)
        self.left_frame_btn_update.place(relx=0.02,rely=0.8,relwidth=0.4)

        # add button
        self.left_frame_btn_update = tk.Button(left_frame,text='Add Item', font=('Times New Roma',14), bg=color.color_list[2],command=self.add_item_to_db)
        self.left_frame_btn_update.place(relx=0.54,rely=0.8,relwidth=0.4)

        # delete button
        self.left_frame_btn_update = tk.Button(left_frame,text='Delete Item', font=('Times New Roma',14,'bold'), bg=color.color_list[6], fg=color.color_list[1],command=self.delete_item)
        self.left_frame_btn_update.place(relx=0.26,rely=0.9,relwidth=0.45)

        # =================== frame ========================= #
        self.right_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.right_frame.place(relx=0.26,rely=0,relwidth=0.738, relheight=1)
        self.show_table()
        
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
            self.item_code_to_query = item_values[1]
            self.set_entry_value(self.left_frame_entry_item_name,item_values[0])
            self.set_entry_value(self.left_frame_entry_item_code,item_values[1])
            self.set_entry_value(self.left_frame_entry_item_group,item_values[2+1])
            self.set_entry_value(self.left_frame_entry_company,item_values[3+1])
            self.set_entry_value(self.left_frame_entry_shelf_no,item_values[4+1])
            self.set_entry_value(self.left_frame_entry_quantity,item_values[5+1])
            self.set_entry_value(self.left_frame_entry_sale_price,item_values[6+1])
            self.set_entry_value(self.left_frame_entry_purchase_price,item_values[7+1])
    
    
    def show_table(self):
        right_frame_table_caption_lbl = tk.Label(self.right_frame,text='Item Table', font=('Times New Roma',16,'bold'),bg=color.color_list[7])
        right_frame_table_caption_lbl.place(relx=0.4,relwidth=0.2,relheight=0.06)

        # ---------------------------- scroll table frame ----------------------------- #
        self.right_frame_table_frame = tk.Frame(self.right_frame,bg=color.color_list[7])
        self.right_frame_table_frame.place(relx=0,rely=0.07,relwidth=1,relheight=0.7)

        right_frame_lbl_1 = tk.Label(self.right_frame,text='Search By: ',bg=color.color_list[7],anchor='w',font=('Times New Roma',12))
        right_frame_lbl_1.place(relx=0.01,rely=0.8,relwidth=0.12)

        self.product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list)
        search_type.config(font=('Times New Roma',12))
        search_type.place(relx=0.14, rely=0.8, relwidth=0.18,relheight=0.06)

        right_frame_lbl_2 = tk.Label(self.right_frame,text='Query: ',bg=color.color_list[7],anchor='w',font=('Times New Roma',12))
        right_frame_lbl_2.place(relx=0.01,rely=0.87,relwidth=0.12)

        self.right_frame_entry_query = tk.Entry(self.right_frame)
        self.right_frame_entry_query.place(relx=0.14,rely=0.87,relwidth=0.18,relheight=0.05)

        # search button
        self.right_frame_btn_search = tk.Button(self.right_frame,text='Search',bg=color.color_list[2],font=('Times New Roman',12,'bold'))
        self.right_frame_btn_search.place(relx=0.1,rely=0.94,relwidth=0.1,relheight=0.05)

        # preview button
        self.right_frame_btn_privew = tk.Button(self.right_frame,text='Preview',bg=color.color_list[2],font=('Times New Roman',14,'bold'))
        self.right_frame_btn_privew.place(relx=0.4,rely=0.85,relwidth=0.11,relheight=0.06)

        # back button
        self.right_frame_btn_back = tk.Button(self.right_frame,text='Back',bg=color.color_list[2],font=('Times New Roman',14,'bold'),command=lambda:self.back_home())
        self.right_frame_btn_back.place(relx=0.8,rely=0.85,relwidth=0.11,relheight=0.06)

        
        
        
        # scroll bar
        scrollbar = tk.Scrollbar(self.right_frame_table_frame)

        # # treeview
        self.tree = tk.ttk.Treeview(self.right_frame_table_frame, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8", "c9"), show='headings', yscrollcommand=scrollbar.set)
        self.tree.heading("#0", text="Serial No.")
        # self.tree.heading("col1", text="Email")
        self.tree.heading("c1", text="Item Name")
        self.tree.heading("c2", text="Item Code")
        self.tree.heading("c3", text="Date")
        self.tree.heading("c4", text="Item Group")
        self.tree.heading("c5", text="Item Company")
        self.tree.heading("c6", text="Shelf No.")
        self.tree.heading("c7", text="QTY")
        self.tree.heading("c8", text="Sale")
        self.tree.heading("c9", text="Purchase")
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        command = "SELECT * FROM item_details"
        data_rows = dao.get_rows(command)
        # # Insert the data in Treeview widget
        # # tree.insert('', 'end', values=('1', 'Honda', "hello"))
        print(data_rows)
        if data_rows[0]==0:
            print(data_rows[1])
            _help_functions.show_message('warning',data_rows[1])
        else:
            for i in range(0,len(data_rows[1])):
                values_list = []
                for data in data_rows[1][i]:
                    values_list.append(data)
                # values_list = [data_rows[1][i][0],data_rows[1][i][3],data_rows[1][i][4]]
                self.tree.insert("",tk.END,text=(str)(i+1),values=values_list,tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=1)
        scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbar.config( command = self.tree.yview )
        
        
# root = tk.Tk()
# root.geometry('1100x650')        
# obj = Item_Manage()

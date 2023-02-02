import tkinter as tk
import tkcalendar as tkcal
import datetime as dt 

import help_functions as _help
import DAO as dao
import color_code as color

class Item_Manage:
    def __init__(self,root):
        self.root = root
        self.message_type=['error','success']
        self.item_entries = None
        # self.item_manage(self.root)
    def backHome(self):
        print("back home")
        self.main_frame.place_forget()
    
    def get_values(self):
        values = []
        for i in range(8):
            values.append(self.item_entries[i].get())
        return values
    
    
    def addInvoiceDB(self):
        message = dao.get_new_invoice()
        print("\n-----------new invoice--------------\n",message)
        if(message[0]==0):
            _help.show_message('error',message[1])
            return
        values = [0 for i in range(10)]
        values[0] = message[1]+1 # invoice id
        values[1] = 'add' # type
        values[2] = self.item_entries[8].get() # date
        values[3] = dt.datetime.now().strftime("%I:%M:%S %p") # time
        
        qty = (int)(self.item_entries[5].get()) # qty
        unit_price = (float)(self.item_entries[6].get()) # unit  price
        
        values[4] = (float)(qty*unit_price) # total
        values[5] = 0 # discount
        values[6] = (float)(values[4]*(float)(self.item_entries[4].get())) # vat
        values[7] = values[4]+values[6] # payable
        values[8] = values[7] # paid
        values[9] = 0 # change
        command = "INSERT INTO invoice VALUES(?,?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print("\n-----------invoice--------------\n",message)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        pass
    
    
    def addPurchaseHistoryDB(self):
        values = [0 for i in range(11)]
        values[0] = self.item_entries[0].get() # code
        values[1] = self.item_entries[1].get() # name 
        values[2] = (int)(self.item_entries[5].get()) # qty
        values[3] = (float)(self.item_entries[6].get()) # unit  price
        values[4] = (float)(values[2]*values[3]) # total
        values[5] = 0 #discount
        values[6] = (float)(values[4]*(float)(self.item_entries[4].get())) # vat
        values[7] = values[4]+values[6] # payable
        values[8] = values[7] # paid
        values[9] = 0 # change
        message = dao.get_new_invoice()
        print("\n-----------new invoice purchase--------------\n",message)
        if(message[0]==0):
            _help.show_message('error',message[1])
            return
        
        values[10] = message[1]+1 # invoice_id
        command = "INSERT INTO sale_purchase VALUES(?,?,?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print("\n-----------insert sale pur--------------\n",message)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        
        
    def addItemDetailsDB(self):
        values = self.get_values()
        for v in values:
            if len(v)==0:
                _help.show_message('error','Please fill all the fields')
                return False
        print("values ",values)
        message = dao.get_new_invoice()
        values.append(message[1]+1)
        print("\n-----------new invoice item details-------------\n",message)
        if(message[0]==0):
            _help.show_message('error',message[1])
            return
        command = "INSERT INTO item_details VALUES(?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print("\n-----------insert item--------------\n",message)
        self.addPurchaseHistoryDB()
        self.addInvoiceDB()
        self.show_table()
        self.clear_input()
        _help.show_message(self.message_type[message[0]],message[1])
        pass
    
    def update_item(self):
        try:
            values = [self.item_entries[i].get() for i in range(1,8)]
            values.append(self.item_code_to_query)
            for v in values:
                if len(v)==0:
                    _help.show_message('error','Please fill all the fields')
                    return False
            command = "UPDATE item_details SET name = ?, group_ = ?, company = ?, vat_rate = ?, quantity = ?, unit_purchase_price = ?, unit_sale_price = ? WHERE code=?;"
            print(values)
            message = dao.update_rows(command,values)
            print(message)
            command = "UPDATE invoice SET date=? WHERE invoice_id IN (SELECT invoice_id FROM item_details WHERE code=?);"
            values = [self.item_entries[8].get(),self.item_code_to_query]
            message = dao.update_rows(command,values)
            print(message)
            self.clear_input()
            self.show_table()
            _help.show_message(self.message_type[message[0]],message[1])
        except AttributeError:
            _help.show_message(self.message_type[0],"Please select one")
        except Exception as e:
            _help.show_message(self.message_type[0],e)
    
    def delete_item(self):
        try:
            command = "DELETE FROM item_details WHERE item_code = ?;"
            values = [self.item_code_to_query]
            message = dao.delete_rows(command,values)
            print(message)
            _help.show_message(self.message_type[message[0]],message[1])
        except AttributeError:
            _help.show_message(self.message_type[0],"Please select one")
        except Exception as e:
            _help.show_message(self.message_type[0],e)
    
    def clear_input(self):
        for i in range(8):
            self.set_entry_value(self.item_entries[i],'')
    
    def leftFrame(self,left_frame):
        item_info_list = ['Item Code :','Item Name :', 'Item Group :', 'Company :',
                        'VAT :', 'Quantity :','Sale Price :','Purchase Price :','Date :']
        # ----------------------- label --------------------- #
        for i in range(0,len(item_info_list)):
            tk.Label(left_frame,text=item_info_list[i], bg=color.color_list[7], font=('Times New Roman',14), anchor='w' \
                     ).place(relx=0.02, rely=0.01+(0.08)*i, relwidth=0.45, relheight=0.06)
        
        # ---------------------- item info input ------------ #
        self.item_entries = [tk.Entry(left_frame) for i in range(8)]
        self.item_entries.append(tkcal.DateEntry(left_frame,date_pattern="dd/MM/yyyy"))
        for i in range(9):
            self.item_entries[i].place(relx=0.48,rely=0.01+i*0.08,relwidth=0.5,relheight=0.06)
    
    def rightFrame(self):
        tk.Label(self.right_frame,text='Search By: ',bg=color.color_list[7],anchor='w',\
            font=('Times New Roma',12)).place(relx=0.01,rely=0.8,relwidth=0.12)

        self.product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list)
        search_type.config(font=('Times New Roma',12))
        search_type.place(relx=0.14, rely=0.8, relwidth=0.18,relheight=0.06)

        tk.Label(self.right_frame,text='Query: ',bg=color.color_list[7],anchor='w',\
            font=('Times New Roma',12)).place(relx=0.01,rely=0.87,relwidth=0.12)

        self.right_frame_entry_query = tk.Entry(self.right_frame)
        self.right_frame_entry_query.place(relx=0.14,rely=0.87,relwidth=0.18,relheight=0.05)

        # search button
        self.right_frame_btn_search = tk.Button(self.right_frame,text='Search',bg=color.color_list[2],font=('Times New Roman',12,'bold'))
        self.right_frame_btn_search.place(relx=0.1,rely=0.94,relwidth=0.1,relheight=0.05)

        # preview button
        self.right_frame_btn_privew = tk.Button(self.right_frame,text='Preview',bg=color.color_list[2],font=('Times New Roman',14,'bold'))
        self.right_frame_btn_privew.place(relx=0.4,rely=0.85,relwidth=0.11,relheight=0.06)

        # back button
        self.right_frame_btn_back = tk.Button(self.right_frame,text='Back',bg=color.color_list[2],font=('Times New Roman',14,'bold'),command=lambda:self.backHome())
        self.right_frame_btn_back.place(relx=0.8,rely=0.85,relwidth=0.11,relheight=0.06)

        
    def item_manage(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        # ======================== left frame ========================= #
        left_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        left_frame.place(relx=0.005,rely=0,relwidth=0.25, relheight=1)
        self.leftFrame(left_frame)
        
        # update button
        self.left_frame_btn_update = tk.Button(left_frame,text='Update', font=('Times New Roma',14), bg=color.color_list[2],command=self.update_item)
        self.left_frame_btn_update.place(relx=0.02,rely=0.8,relwidth=0.4)

        # add button
        self.left_frame_btn_update = tk.Button(left_frame,text='Add Item', font=('Times New Roma',14), bg=color.color_list[2],command=self.addItemDetailsDB)
        self.left_frame_btn_update.place(relx=0.54,rely=0.8,relwidth=0.4)

        # delete button
        self.left_frame_btn_update = tk.Button(left_frame,text='Delete Item', font=('Times New Roma',14,'bold'), bg=color.color_list[6], fg=color.color_list[1],command=self.delete_item)
        self.left_frame_btn_update.place(relx=0.26,rely=0.9,relwidth=0.45)

        # ========================= right frame ========================= #
        self.right_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.right_frame.place(relx=0.26,rely=0,relwidth=0.738, relheight=1)
        self.rightFrame()
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
            for i in range(8):
                self.set_entry_value(self.item_entries[i],item_values[i+1])
            self.item_entries[8].set_date(item_values[10])
    
    def show_table(self):
        tk.Label(self.right_frame,text='Item Table', font=('Times New Roma',16,'bold'),\
                bg=color.color_list[7]).place(relx=0.4,relwidth=0.2,relheight=0.06)

        # ---------------------------- scroll table frame ----------------------------- #
        self.right_frame_table_frame = tk.Frame(self.right_frame,bg=color.color_list[7])
        self.right_frame_table_frame.place(relx=0,rely=0.07,relwidth=1,relheight=0.7)
        
        # scroll bar
        scrollbary = tk.Scrollbar(self.right_frame_table_frame)
        scrollbarx = tk.Scrollbar(self.right_frame_table_frame)
        
        columns = [f'c{i}' for i in range(1,12)]
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','Sale','inv-id','Date']
        column_size = [20,50,50,50,100,30,30,50,50,50,30]
        column_anchor = ['e','center','center','center','center','w','w','w','w','w','center']
        
        # treeview
        self.tree = tk.ttk.Treeview(self.right_frame_table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        
        command = "SELECT item_details.*, invoice.date \
        FROM item_details,invoice \
        WHERE invoice.type='add' and item_details.invoice_id=invoice.invoice_id;"
        
        data_rows = dao.get_rows(command)
        print(data_rows)
        if data_rows[0]==0:
            print(data_rows[1])
            _help.show_message('warning',data_rows[1])
        else:
            for i in range(0,len(data_rows[1])):
                values_list = [i+1]
                for data in data_rows[1][i]:
                    values_list.append(data)
                
                self.tree.insert("",tk.END,values=values_list,tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
        
        
# root = tk.Tk()
# root.geometry('1100x650')        
# obj = Item_Manage()

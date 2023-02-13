import tkinter as tk
import tkcalendar as tkcal
import datetime as dt 

import help_functions as _help
import DAO as dao
import color_code as color

class Item_Manage:
    def __init__(self,root):
        try:
            self.root = root
            self.message_type=['error','success']
            self.item_entries = None
            # self.item_manage(self.root)
        except Exception as e:
            _help.show_message('warning',f'Occur exception while Item manage object creating {e}')
    def backHome(self):
        print("back home")
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()
    
    def get_values(self):
        values = []
        for i in range(8):
            values.append(self.item_entries[i].get())
        return values
    
    
    def addInvoiceDB(self):
        message = dao.getLastInvoiceId()
        print("\n-----------new invoice--------------\n",message)
        if(message[0]==0):
            _help.show_message('error',message[1])
            return
        values = [0 for i in range(10)]
        values[0] = message[1]+1 # invoice id
        values[1] = 'purchase' # type
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
        message = dao.getLastInvoiceId()
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
        message = dao.getLastInvoiceId()
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
        self.retrieveAllItems()
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
            self.retrieveAllItems()
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
        for i in range(7):
            self.set_entry_value(self.item_entries[i],'')
    
    def activeNextEntry(self,event,next_entry):
        next_entry.focus_set()
        
    def leftFrame(self,left_frame):
        item_info_list = ['Item Code :','Item Name :', 'Item Group :', 'Company :',
                        'VAT :', 'Quantity :','Purchase Price :','Sale Price :','Date :']
        
        # ----------------------- label --------------------- #
        for i in range(0,len(item_info_list)):
            tk.Label(left_frame,text=item_info_list[i], bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), font=('Helvic',10), anchor='w' \
                     ).place(relx=0.02, rely=0.01+(0.06)*i, relwidth=0.45, relheight=0.04)
        
        self.item_entries_frame = [tk.Frame(left_frame, bg=color.getColor('bd_input')) for i in range(9)]
        self.item_entries = [tk.Entry(self.item_entries_frame[i], bd=0) for i in range(8)]
        self.item_entries.append(tkcal.DateEntry(self.item_entries_frame[8],date_pattern="dd/MM/yyyy"))
        for i in range(9):
            self.item_entries_frame[i].place(relx=0.48,rely=0.01+i*0.06,relwidth=0.5,relheight=0.04)
            self.item_entries[i].pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
            _help.input_hover(self.item_entries_frame[i],self.item_entries[i])
        
        self.item_entries[0].focus_set()
        for i in range(7):
            self.item_entries[i].bind("<Return>",lambda e,next_entry=self.item_entries[i+1]: self.activeNextEntry(e,next_entry))
    
    
    def searchItem(self):
        if len(self.product_search_type.get())==0 or len(self.search_query.get())==0:
            _help.show_message('warning','Input field can not be empty')
            return
        command = f"SELECT item_details.*, invoice.date \
        FROM item_details,invoice \
        WHERE item_details.{self.product_search_type.get()}=? and item_details.invoice_id=invoice.invoice_id;"
        
        data_rows = dao.get_rows(command,[self.search_query.get()])
        print(data_rows)
        items = []
        if data_rows[0]==0:
            print(data_rows[1])
            _help.show_message('warning',data_rows[1])
            return
        else:
            for i in range(0,len(data_rows[1])):
                values_list = [i+1]
                for data in data_rows[1][i]:
                    values_list.append(data)
                items.append(values_list)
        self.show_table(items)
        pass
    
    def suggestion(self,event):
        command = f'SELECT DISTINCT {self.product_search_type.get()} FROM item_details;'
        result = dao.get_rows(command,[])
        if result[0]==0:
            _help.show_message('error',f'Found an exception while finding distinct words for search {result[1]}')
        self.suggestion_words = []
        for word in result[1]:
            self.suggestion_words.append(word[0])
        
    
    def showSuggestion(self,event,type):
        if type:
            self.suggestion_frame.place(relx=0.14,rely=0.92,relwidth=0.18,relheight=0.08)
            self.search_btn_frame.place_forget()
            self.update_suggestions(event)
        else:
            self.search_btn_frame.place(relx=0.1,rely=0.94, width=90, height=22)
            self.suggestion_frame.place_forget()
        
    def update_suggestions(self,event):
        entered_text = self.search_query.get()
        print(self.suggestion_words)
        suggestions = [word for word in self.suggestion_words if word.startswith(entered_text)]
        if len(entered_text)==0:
            suggestions=self.suggestion_words
        print(suggestions)
        self.suggest_list.delete(0, tk.END)
        for suggestion in suggestions:
            self.suggest_list.insert(tk.END, suggestion)
    
    def rightFrame(self):
        tk.Label(self.right_frame,text='Search By: ',bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'),anchor='w',\
            font=('Times New Roma',12)).place(relx=0.01,rely=0.8,relwidth=0.12)

        self.product_search_type = tk.StringVar()
        search_type_list = ['name', 'name', 'code', 'company','group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.ttk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list, command=self.suggestion)
        search_type.place(relx=0.14, rely=0.8, relwidth=0.18,relheight=0.06)

        tk.Label(self.right_frame,text='Query: ',bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'),anchor='w',\
            font=('Times New Roma',12)).place(relx=0.01,rely=0.87,relwidth=0.12)

        self.search_query = tk.Entry(self.right_frame)
        self.search_query.place(relx=0.14,rely=0.87,relwidth=0.18,relheight=0.05)
        self.search_query.bind("<KeyRelease>", self.update_suggestions)
        self.search_query.bind("<BackSpace>", self.update_suggestions)
        self.search_query.bind("<FocusIn>",lambda e,type=1:self.showSuggestion(e,type))
        self.search_query.bind("<FocusOut>",lambda e,type=0:self.showSuggestion(e,type))

        self.suggestion_frame = tk.Frame(self.right_frame)
        y_scrollbar = tk.Scrollbar(self.suggestion_frame)
        y_scrollbar.place(relx=0.9,rely=0,relwidth=0.1,relheight=1)
        self.suggest_list = tk.Listbox(self.suggestion_frame, yscrollcommand=y_scrollbar.set)
        self.suggest_list.place(relx=0,rely=0,relwidth=0.9,relheight=1)
        
        def fillQuery(event):
            self.set_entry_value(self.search_query,self.suggest_list.get(self.suggest_list.curselection()))
            self.showSuggestion(event,0)
        self.suggest_list.bind("<Double-Button-1>", fillQuery)
        self.suggest_list.bind("<FocusIn>",lambda e,type=1:self.showSuggestion(e,type))
        
        
        btn_frame = [tk.Frame(self.right_frame,bg=color.getColor('bd_button')) for i in range(3)]
        btn_frame[0].place(relx=0.1,rely=0.94, width=90, height=22)
        btn_frame[1].place(relx=0.4,rely=0.85, width=90, height=22)
        btn_frame[2].place(relx=0.8,rely=0.85, width=90, height=22)
        
        self.search_btn_frame = btn_frame[0]
        # search button
        search_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Search', bd=0, command=self.searchItem)
        search_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        preview_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Preview', bd=0)
        preview_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        back_btn = tk.Button(btn_frame[2],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Back', bd=0,command=self.backHome)
        back_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame[0],search_btn)
        _help.button_hover(btn_frame[1],preview_btn)
        _help.button_hover(btn_frame[2],back_btn)
        

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
    
    def show_table(self, items):
        tk.Label(self.right_frame,text='Item Table', font=('Times New Roma',16,'bold'),\
                bg=color.getColor('bg_lbl')).place(relx=0.4,relwidth=0.2,relheight=0.06)

        # ---------------------------- scroll table frame ----------------------------- #
        self.right_frame_table_frame = tk.Frame(self.right_frame,bg='#ffffff')
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
        
        for i,item in enumerate(items):
            self.tree.insert("",tk.END,values=item,tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
    
    
    def retrieveAllItems(self):
        command = "SELECT item_details.*, invoice.date \
        FROM item_details,invoice \
        WHERE invoice.type=? and item_details.invoice_id=invoice.invoice_id;"
        
        data_rows = dao.get_rows(command,['purchase'])
        print(data_rows)
        items = []
        if data_rows[0]==0:
            print(data_rows[1])
            _help.show_message('warning',data_rows[1])
            return
        else:
            for i in range(0,len(data_rows[1])):
                values_list = [i+1]
                for data in data_rows[1][i]:
                    values_list.append(data)
                items.append(values_list)
        self.show_table(items)
        pass
    
    
    def item_manage(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        # ======================== left frame ========================= #
        left_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        left_frame.place(relx=0.005,rely=0,relwidth=0.25, relheight=1)
        self.leftFrame(left_frame)
        
        btn_frame = [tk.Frame(left_frame,bg=color.getColor('bd_button')) for i in range(3)]
        btn_frame[1].place(relx=0.01,rely=0.8, relwidth=.31, height=22) # add button place
        btn_frame[0].place(relx=0.33,rely=0.8, relwidth=.31, height=22) # update 
        btn_frame[2].place(relx=0.66,rely=0.8, relwidth=.31, height=22) # delete
        
        update_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Update', bd=0,command=self.update_item)
        update_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        add_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Add', bd=0,command=self.addItemDetailsDB)
        add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        delete_btn = tk.Button(btn_frame[2],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Delete', bd=0,command=self.delete_item)
        delete_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        _help.button_hover(btn_frame[0],update_btn)
        _help.button_hover(btn_frame[1],add_btn)
        _help.button_hover_del(btn_frame[2],delete_btn)

        # ========================= right frame ========================= #
        self.right_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.right_frame.place(relx=0.26,rely=0,relwidth=0.738, relheight=1)
        self.rightFrame()
        self.retrieveAllItems()
        
# root = tk.Tk()
# root.geometry('1100x650')        
# obj = Item_Manage()

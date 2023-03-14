import tkinter as tk

from home import *
import color_code as color
import pytohtml as _pytohtml
import help_functions as _help


class DemageStcok:
    def __init__(self,root) -> None:
        try:
            self.root = root
            self.item_info_lbl = []
        except Exception as e:
            _help.show_message('warning',f'Occur exception while demage stock object creating {e}')
        pass
    
    def backHome(self):
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()
        
    def preview(self):
        receipt_name = ' Stock Item'
        date = dt.datetime.today().date()
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','inv-id','Date']
        total_info_name = ['Total item Quantity :','Total Purchase Price :']
        total_info = [0 for i in range(len(total_info_name))]
        rows = []
        for i,row in enumerate(self.item_list):
            rows.append([i+1]+list(row))
            total_info[0] += float(row[5]) # qty
            total_info[1] += float(row[6]) # purchase
        
        obj = _pytohtml.PythonToHtml()
        obj.stockReceipt(receipt_name,date,self.lstinv, headings,rows,total_info_name,total_info)
    
    def deleteFromDemage(self):
        pass
    
    def addInvoiceDB(self,row):
        command = "INSERT INTO invoice(invoice_id,type,date,time,total) VALUES(?,?,?,?,?);"
        return dao.set_rows(command,row)
        
        
    def addToDemage(self):
        selected_code = self.item_info_lbl[0].get()
        try:
            int(self.item_info_lbl[5].get())
        except ValueError:
            _help.show_message('error','Quantity have to integer number')
            return
        demaeged_qty = int(self.item_info_lbl[5].get())
        if demaeged_qty > self.avl_qty:
            _help.show_message('error','Demaged quantity is larger than available')
            return
        
        # decrease available quantity
        command = "UPDATE item_details SET quantity = quantity-? WHERE code = ?;"
        values = [demaeged_qty,selected_code]
        message = dao.update_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While removing demaged item {message[1]}')
            return
         
        lastInvoiceId = int(dao.getLastInvoiceId()[1])
        self.lstinv = lastInvoiceId+1
        # insert into invoice table
        row = [lastInvoiceId+1,'demage',dt.datetime.now().strftime("%d/%m/%Y"),dt.datetime.now().strftime("%I:%M:%S %p"),self.avl_qty*self.price]
        message = self.addInvoiceDB(row)
        if message[0]==0:
            _help.show_message('error',f'While inserting into invoice new demage {message[1]}')
            return
        command = "INSERT INTO demage_item VALUES(?,?,?);"
        values = [selected_code,demaeged_qty,lastInvoiceId+1]
        message = dao.set_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While inserting into demage new demage {message[1]}')
            return
        for i,itm in enumerate(self.item_info_lbl):
            if i%5:
                itm.config(text='')
            else:
                self.set_entry_value(itm,'')
        
        _help.show_message('success','Successfull Added')
        pass
    
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
        
    def showItemDetails(self,event):
        code = self.item_info_lbl[0].get()
        command = "SELECT item_details.*, invoice.date \
            FROM item_details, invoice \
            WHERE item_details.invoice_id=invoice.invoice_id\
            AND invoice.type=? AND item_details.code = ?; "
        values = ['demage',code]
        message = dao.get_rows(command,values)
        print(message,values)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        
        if len(message[1])==0:
            _help.show_message('warning','No items')
            return
        item_details = message[1][0]
        self.avl_qty = int(item_details[5]) # available quantity
        self.price = float(item_details[6])
        for i,itm in enumerate(item_details):
            if i%5:
                self.item_info_lbl[i].config(text=itm)
            else:
                self.set_entry_value(self.item_info_lbl[i],itm)
        self.item_info_lbl[5].focus_set()
        
    def restoreItem(self):
        pass
    
    
    def updateDemageStock(self):
        lbl_height=0.13
        lbl_start = 0.08
        lbl_gap = 0.03
        lbl_name = ['Code','Name','Group','Company','VAT(%)','QTY','Purchase','Sale','inv-id','Date']
        
        for i in range(0,10):
            tk.Label(self.top_frame,text=lbl_name[i], bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w'
                ).place(relx=0.22 if i<5 else 0.38,rely=lbl_start+(lbl_height+lbl_gap)*(i%5), relwidth=0.06, relheight=lbl_height)
                    
        self.item_info_lbl = [tk.Label(self.top_frame, bg=color.getColor('bg_input'), fg=color.getColor('fg_input'), anchor='w')
                              if i%5 else tk.Entry(self.top_frame) for i in range(0,10)]
        
        for i in range(0,10):
            self.item_info_lbl[i].place(relx=0.29 if i<5 else 0.45,rely=lbl_start+(lbl_height+lbl_gap)*(i%5), relwidth=0.08, relheight=lbl_height)
        self.item_info_lbl[0].focus_set()
        self.item_info_lbl[0].bind("<Return>",self.showItemDetails)

        btn_frame = [tk.Frame(self.top_frame,bg=color.getColor('bd_button')) for i in range(3)]
        btn_frame[0].place(relx=0.55,rely=0.2,width=90,height=22)
        btn_frame[1].place(relx=0.55,rely=0.4,width=90,height=22)
        btn_frame[2].place(relx=0.55,rely=0.6,width=90,height=22)
        add_btn = tk.Button(btn_frame[0],text='Add', bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), command=self.addToDemage, bd=0)
        add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        restore_btn = tk.Button(btn_frame[1],text='Restore', bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), command=self.restoreItem, bd=0)
        restore_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        delete_btn = tk.Button(btn_frame[2],text='Delete', bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), command=self.deleteFromDemage, bd=0)
        delete_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame[0],add_btn)
        _help.button_hover(btn_frame[1],restore_btn)
        _help.button_hover_del(btn_frame[2],delete_btn)

    def suggestion(self,event):
        command = f'SELECT DISTINCT {self.product_search_type.get()} FROM item_details;'
        result = dao.get_rows(command,[])
        if result[0]==0:
            _help.show_message('error',f'Found an exception while finding distinct words for search {result[1]}')
        self.suggestion_words = []
        for word in result[1]:
            self.suggestion_words.append(word[0])
        self.set_entry_value(self.search_query,'')
          
    
    def showSuggestion(self,event,type):
        if type:
            self.suggestion_frame.place(relx=0.09, rely=0.35, relwidth=0.1,relheight=0.25)
            self.search_btn_frame.place_forget()
            self.update_suggestions(event)
        else:
            self.search_btn_frame.place(relx=0.05, rely=0.42, width=90, height=22)
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
               
    def searchItem(self):
        if len(self.product_search_type.get())==0 or len(self.search_query.get())==0:
            _help.show_message('warning','Input field can not be empty')
            return
        command = f"SELECT item_details.*, invoice.date \
            FROM item_details, invoice,demage_item \
            WHERE demage_item.invoice_id=invoice.invoice_id AND\
            demage_item.code=item_details.code \
            AND item_details.{self.product_search_type.get()}=? AND \
            invoice.type=?;"
        # command = f"SELECT item_details.*, invoice.date \
        # FROM item_details,invoice \
        # WHERE item_details.{self.product_search_type.get()}=? AND\
        # invoice.type=? AND item_details.invoice_id=invoice.invoice_id;"
        
        data_rows = dao.get_rows(command,[self.search_query.get(),'demage'])
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
        self.showTable(items)
        pass
    
    
    def topFrame(self):
        self.updateDemageStock()
        # search type
        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w', font=('Times New Roman',12), text='Search by :'
            ).place(relx=0.01, rely=0.08, relwidth=0.08, relheight=0.1)

        self.product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.ttk.OptionMenu(self.top_frame, self.product_search_type, *search_type_list, command=self.suggestion)
        search_type.place(relx=0.09, rely=0.08, relwidth=0.1, relheight=0.12)

        # search box
        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w', font=('Times New Roman',12), text='Query :'
            ).place(relx=0.01, rely=0.25, relwidth=0.08, relheight=0.1)

        self.search_query = tk.Entry(self.top_frame)
        self.search_query.place(relx=0.09, rely=0.25, relwidth=0.1, relheight=0.1)
        self.search_query.bind("<KeyRelease>", self.update_suggestions)
        self.search_query.bind("<BackSpace>", self.update_suggestions)
        self.search_query.bind("<FocusIn>",lambda e,type=1:self.showSuggestion(e,type))
        self.search_query.bind("<FocusOut>",lambda e,type=0:self.showSuggestion(e,type))
        
        self.suggestion_frame = tk.Frame(self.top_frame)
        self.suggest_list = tk.Listbox(self.suggestion_frame)
        self.suggest_list.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def fillQuery(event):
            self.set_entry_value(self.search_query,self.suggest_list.get(self.suggest_list.curselection()))
            self.showSuggestion(event,0)
        self.suggest_list.bind("<Double-Button-1>", fillQuery)
        self.suggest_list.bind("<FocusIn>",lambda e,type=1:self.showSuggestion(e,type))
        

        btn_frame = [tk.Frame(self.top_frame,bg=color.getColor('bd_button')) for i in range(4)]
        btn_frame[0].place(relx=0.05, rely=0.42, width=90, height=22)
        btn_frame[1].place(relx=0.8, rely=0.15, width=90, height=22)
        btn_frame[2].place(relx=0.8, rely=0.35, width=90, height=22)
        btn_frame[3].place(relx=0.8, rely=0.55, width=90, height=22)
        
        self.search_btn_frame = btn_frame[0]
        # search button
        search_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Search', bd=0, command=self.searchItem)
        search_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        refresh_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Refresh', bd=0)
        refresh_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        preview_btn = tk.Button(btn_frame[2],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Preview', bd=0,command=self.preview)
        preview_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        back_btn = tk.Button(btn_frame[3],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Back', bd=0,command=self.backHome)
        back_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame[0],search_btn)
        _help.button_hover(btn_frame[1],refresh_btn)
        _help.button_hover(btn_frame[2],preview_btn)
        _help.button_hover(btn_frame[3],back_btn)

    def on_select(self,event):
        selected_items = self.tree.selection()
        
        for item in selected_items:
            item_values = self.tree.item(item)["values"]
            for i in range(1,len(item_values)):
                if (i-1)%5:
                    self.item_info_lbl[i].config(text=item_values[i]) if i>=7 \
                    else self.item_info_lbl[i-1].config(text=item_values[i])
                else:
                    self.set_entry_value(self.item_info_lbl[i],item_values[i]) if i>=7 \
                    else self.set_entry_value(self.item_info_lbl[i-1],item_values[i])
        pass
    
    def showTable(self,items=None):
        if items:
            self.item_list=items
        table_frame = tk.Frame(self.bottom_frame,bg='#ffffff')
        table_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','inv-id','Date']
        columns = [f'c{i}' for i in range(1,len(headings)+1)]
        column_size = [80 for i in range(0,len(headings))]
        column_anchor = ['e','center','center','center','center','w','w','w','w','center']
        
        # treeview
        self.tree = tk.ttk.Treeview(table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.98,relheight=.95)
        scrollbary.place(relx=0.98,rely=0,relwidth=0.02,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
        
        for i in range(0,len(self.item_list)):
            self.tree.insert("",tk.END,values=[i+1]+list(self.item_list[i]),tag = row_color[i%2])
        pass
    
    def bottomFrame(self):
        command = "SELECT item_details.code,item_details.name,item_details.group_,item_details.company,\
            item_details.vat_rate,demage_item.quantity,item_details.unit_purchase_price,invoice.invoice_id,invoice.date\
            FROM item_details, invoice,demage_item \
            WHERE demage_item.invoice_id=invoice.invoice_id AND demage_item.code=item_details.code \
            AND demage_item.code = ?;"
        values = ['abc']
        message = dao.get_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While fetching item data {message[1]}')
            return
        
        self.item_list = message[1]
        self.showTable()
        
        
    def demageStock(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

        # ======================== top frame ===================== #
        self.top_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.35)
        self.topFrame()

        # ======================== bottom frame ===================== #
        self.bottom_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.bottom_frame.place(relx=0,rely=0.35,relwidth=1,relheight=0.65)
        self.bottomFrame()
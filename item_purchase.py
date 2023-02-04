import tkinter as tk
from tkinter import ttk
import tkcalendar as tkcal
import datetime as dt 

import color_code as color
import DAO as dao
import help_functions as _help
import pytohtml as pytohtml


class Item_Purchase:
    def __init__(self,root):
        self.root = root
        self.add_item_list = []
        self.check_unique_code = {}
        pass
    
    def back_home(self):
        self.add_item_list.clear()
        self.check_unique_code.clear()
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()
    
    def clearItemEntries(self):
        for i in range(len(self.item_entries)-1):
            self.set_entry_value(self.item_entries[i],'')
            
            
    def addItemList(self):
        values = [entry.get() for entry in self.item_entries]
        if values[0] in self.check_unique_code:
            _help.show_message('warning','Duplicate code\nYou can update previous record')
            return
        for v in values:
            if len(v)==0:
                _help.show_message('error','Please fill all the fields')
                return False
            
        self.check_unique_code[values[0]]=1
        self.add_item_list.append(values)
        self.showTable()
        self.showTotalInfo()
        self.clearItemEntries()
        pass
    
    def updateItem(self):
        values = [entry.get() for entry in self.item_entries]
        for v in values:
            if len(v)==0:
                _help.show_message('error','Please fill all the fields')
                return False
        for i,item in enumerate(self.add_item_list):
            if item[0]==self.selected_code:
                self.add_item_list[i] = values
                self.showTable()
                self.showTotalInfo()
                self.clearItemEntries()
                self.item_entries[0].config(state='normal')
                return
    
    def deleteItem(self):
        for i,item in enumerate(self.add_item_list):
            if item[0]==self.selected_code:
                del self.check_unique_code[item[0]]
                del self.add_item_list[i]
                self.showTable()
                self.showTotalInfo()
                self.clearItemEntries()
                self.item_entries[0].config(state='normal')
                return
    def activeNextEntry(self,event,next_entry):
        next_entry.focus_set()
        
    def leftFrame(self):
        item_info_list = ['Item Code :','Item Name :', 'Item Group :', 'Company :',
                        'VAT :', 'Quantity :','Purchase Price :','Sale Price :','Date :']
        
        for i in range(0,len(item_info_list)):
            tk.Label(self.left_frame,text=item_info_list[i], bg=color.color_list[7], font=('Times New Roman',14), anchor='w' \
                     ).place(relx=0.02, rely=0.01+(0.08)*i, relwidth=0.45, relheight=0.06)
        
        self.item_entries = [tk.Entry(self.left_frame) for i in range(8)]
        self.item_entries.append(tkcal.DateEntry(self.left_frame,date_pattern="dd/MM/yyyy"))
        for i in range(9):
            self.item_entries[i].place(relx=0.48,rely=0.01+i*0.08,relwidth=0.5,relheight=0.06)
        
        self.item_entries[0].focus_set()
        for i in range(7):
            self.item_entries[i].bind("<Return>",lambda e,next_entry=self.item_entries[i+1]: self.activeNextEntry(e,next_entry))
        
        self.add_btn = tk.Button(self.left_frame,text='Add',bg=color.color_list[2], fg=color.color_list[3], command=self.addItemList)
        self.update_btn = tk.Button(self.left_frame,text='Update',bg=color.color_list[2], fg=color.color_list[3], command=self.updateItem)
        self.delete_btn = tk.Button(self.left_frame,text='Delete',bg=color.color_list[6], fg=color.color_list[1], command=self.deleteItem)
        
        self.delete_btn.place(relx=0.10,rely=0.8,relwidth=0.25,relheight=0.05)
        self.update_btn.place(relx=0.37,rely=0.8,relwidth=0.25,relheight=0.05)
        self.add_btn.place(relx=0.64,rely=0.8,relwidth=0.25,relheight=0.05)
        
    def showTotalInfo(self):
        sum = 0
        vat = 0
        qty  = 0
        for values in self.add_item_list:
            tmp = (float)(values[5])*(float)(values[7])
            qty += float(values[5])
            sum += tmp
            print(values[5],values[7])
        vat = 0          
        total_info = [qty,sum,0,vat,vat+sum]+[entries.get() for entries in self.total_info_entries]            
        
        for lbl,text in zip(self.total_info_lbl,total_info):
            lbl.config(text=text)
    
    def searchFrame(self):
        tk.Label(self.right_frame,text='Search by :', bg=color.color_list[7], anchor='w').place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.05)
        tk.Label(self.right_frame,text='Query :', bg=color.color_list[7], anchor='w').place(relx=0.01, rely=0.07, relwidth=0.15, relheight=0.05)
        
        self.product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list)
        search_type.place(relx=0.16, rely=0.01, relwidth=0.2, relheight=0.06)
        
        self.query = tk.Entry(self.right_frame)
        self.query.place(relx=0.16,rely=0.07, relwidth=0.2, relheight=0.05)
        
        self.search_btn = tk.Button(self.right_frame,text='Search',bg=color.color_list[2])
        self.search_btn.place(relx=0.1, rely=0.13, relwidth=0.15, relheight=0.05)

    
    def suplierFrame(self):
        lbl_list = ['Name','Pre-balance','Current Balance', 'Contact']
        for i in range(len(lbl_list)):
            tk.Label(self.right_frame,text=lbl_list[i],bg=color.color_list[7], anchor='w'\
                ).place(relx=0.01, rely=0.19+(i*0.06), relwidth=0.15, relheight=0.05)
        self.supliers_entries = [tk.Entry(self.right_frame) for i in range(4)]
        for i in range(len(self.supliers_entries)):
            self.supliers_entries[i].place(relx=0.16,rely=0.19+(i*0.06),relwidth=0.2,relheight=0.05)
          
    def calcChange(self,event):
        self.set_entry_value(self.total_info_entries[1],(float)(self.total_info_entries[0].get())-(float)(self.total_info_lbl[4].cget('text')))

    def totalFrame(self):
        lbl_list = ['Total Item :', 'Total Price :','Discount :','VAT :','Payable :','Total Paid :', 'Change :']
        for i in range(len(lbl_list)):
            tk.Label(self.right_frame,text=lbl_list[i],bg=color.color_list[7], anchor='w'\
                ).place(relx=0.45, rely=0.01+(i*0.06), relwidth=0.15, relheight=0.05)
            
        self.total_info_lbl = [tk.Label(self.right_frame,bg=color.color_list[7]) for i in range(5)]
        for i in range(len(self.total_info_lbl)):
            self.total_info_lbl[i].place(relx=0.6,rely=0.01+(i*0.06),relwidth=0.15,relheight=0.05)
            
        self.total_info_entries = [tk.Entry(self.right_frame) for i in range(2)]
        for i in range(len(self.total_info_entries)):
            self.total_info_entries[i].place(relx=0.6,rely=0.31+(i*0.06),relwidth=0.15,relheight=0.05)
        self.total_info_entries[0].bind("<Return>",self.calcChange)
            
    def paymentMethodSelect(self,event):
        account_list = []
        if self.payment_method_type.get() in ('Bkash','Nagad'):
            account_list = ['01700909000','01611818111']
        else:
            account_list = ['sonali bank-1','sonali-bank-2']
        select_lbl = tk.Label(self.right_frame,text='Select A/C :',bg=color.color_list[7],  anchor='w')
        select_lbl.place(relx=0.8,rely=0.15,relwidth=0.15,relheight=0.05)
        
        self.payment_acount = tk.StringVar()
        self.payment_acount.set(account_list[0]) # default value
        payment_acount_entry = tk.OptionMenu(self.right_frame, self.payment_acount, *account_list)
        payment_acount_entry.place(relx=0.8, rely=0.22, relwidth=0.15, relheight=0.05)
            
            
        pass            
    def paymentFrame(self):
        tk.Label(self.right_frame,text='Payment Method :',bg=color.color_list[7], anchor='w'\
            ).place(relx=0.8,rely=0.01,relwidth=0.15,relheight=0.05)
        
        self.payment_method_type = tk.StringVar()
        payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
        self.payment_method_type.set(payment_method_type_list[0]) # default value
        payment_method = tk.OptionMenu(self.right_frame, self.payment_method_type, *payment_method_type_list,command=self.paymentMethodSelect)
        payment_method.place(relx=0.8, rely=0.07, relwidth=0.1, relheight=0.05)
        pass
    
    
    def addInvoiceDB(self,row):
        values = [0 for i in range(10)]
        values[0] = row[9]# invoice id
        values[1] = 'purchase' # type
        values[2] = row[8] # date
        values[3] = dt.datetime.now().strftime("%I:%M:%S %p") # time
        
        qty = (int)(row[5]) # qty
        unit_price = (float)(row[7]) # unit  price
        
        values[4] = (float)(qty*unit_price) # total
        values[5] = 0 # discount
        values[6] = (float)(values[4]*(float)(row[4])) # vat
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
    
    
    def addPurchaseHistoryDB(self,row):
        values = [0 for i in range(11)]
        values[0] = row[0] # code
        values[1] = row[1] # name 
        values[2] = (int)(row[5]) # qty
        values[3] = (float)(row[6]) # unit  price
        values[4] = (float)(values[2]*values[3]) # total
        values[5] = 0 #discount
        values[6] = (float)(values[4]*(float)(row[4])) # vat
        values[7] = values[4]+values[6] # payable
        values[8] = values[7] # paid
        values[9] = 0 # change
        values[10] = row[9] # invoice_id
        
        command = "INSERT INTO sale_purchase VALUES(?,?,?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,values)
        print("\n-----------insert sale pur--------------\n",message)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        
    def addItemDetailsDB(self,values):
        message = dao.getLastInvoiceId()
        self.lstinv = message[1]+1
        values.append(message[1]+1)
        print("\n-----------new invoice item details-------------\n",message)
        if(message[0]==0):
            _help.show_message('error',message[1])
            return
        print(values)
        command = "INSERT INTO item_details VALUES(?,?,?,?,?,?,?,?,?);"
        row = values[0:8]+values[9:10]
        print(row)
        message = dao.set_rows(command,row)
        print(message)
        if message[0]==0:
            _help.show_message('error',f"while insert into item details table {message[1]}for item code = {values[0]}")
            return 
        print("\n-----------insert item--------------\n",message)
        
        self.addPurchaseHistoryDB(values)
        self.addInvoiceDB(values)
        
        self.showTable()
        self.clearItemEntries()
        return message
        
    def completePayment(self):
        item_name = []
        item_qty = []
        item_price = []
        sum = 0
        vat = 0
        discount = 0
        for values in self.add_item_list:
            item_name.append(values[1])
            item_qty.append(float(values[5]))
            item_price.append(float(values[7]))
            sum += (float)(values[5])*(float)(values[7])
            print(values[5],values[7])
        
        total_info = [sum,discount,vat,vat+sum]+[float(entries.get()) for entries in self.total_info_entries]
        print("complete ",total_info)
        print("sum ",sum)
        if total_info[4]=='' or total_info[5]=='' or total_info[4]<sum:
            _help.show_message('warning','Please pay carefully')
            return
        
        for values in self.add_item_list:
            self.addItemDetailsDB(values)
        
        # update total amount of main acount
        message = dao.set_rows("UPDATE basic SET total_amount = total_amount+?;",[total_info[3]])
        if message[0]==0:
            _help.show_message('error',f'While updating total amount for sale item {message[1]}')
            return
        
        
        self.back_home()
        obj = pytohtml.PythonToHtml()
        date = dt.datetime.now().strftime("%d/%m/%Y")
        obj.saleReceipt('Purchase Item',date,self.lstinv, item_name=item_name,item_qty=item_qty,item_price=item_price,total_info=total_info)
        _help.show_message('success','Successfully added a new transaction')
        pass
        
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
        
    def on_select(self,event):
        selected_items = self.tree.selection()
        
        for item in selected_items:
            item_values = self.tree.item(item)["values"]
            print(item_values)
            for i in range(9):
                self.set_entry_value(self.item_entries[i],item_values[i+1])

        self.selected_code = self.item_entries[0].get()
        self.item_entries[0].config(state='disabled')
    
    def showTable(self):
        table_frame = tk.Frame(self.right_frame,bg=color.color_list[1])
        table_frame.place(relx=0,rely=0.51,relwidth=1,relheight=0.49)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        columns = [f'c{i}' for i in range(1,11)]
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','Sale','Date']
        column_size = [20,50,50,50,100,30,30,50,50,30]
        column_anchor = ['e','center','center','center','center','w','w','w','w','center']
        
        # treeview
        self.tree = tk.ttk.Treeview(table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        
        for i in range(0,len(self.add_item_list)):
            self.tree.insert("",tk.END,values=[i+1]+self.add_item_list[i],tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
        
    def rightFrame(self):
        self.searchFrame()
        self.suplierFrame()
        self.totalFrame()
        self.paymentFrame()
        tk.Button(self.right_frame,text='Back',bg=color.color_list[2],command=self.back_home).place(relx=0.2,rely=0.45,relwidth=0.1,relheight=0.05)
        tk.Button(self.right_frame,text='Payment',bg=color.color_list[2],command=self.completePayment).place(relx=0.7,rely=0.45,relwidth=0.1,relheight=0.05)
        self.showTable()
    
        
        
    def itemPurchase(self):
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        self.left_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.left_frame.place(relx=0.01,rely=0, relwidth=0.28, relheight=1)
        self.leftFrame()
        
        self.right_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.right_frame.place(relx=0.3,rely=0, relwidth=0.69, relheight=1)
        self.rightFrame()
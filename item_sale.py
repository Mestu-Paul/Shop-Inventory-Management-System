import tkinter as tk
from PIL import ImageTk, Image
import datetime as dt 
import tkcalendar as tkcal
import datetime

import DAO as dao
import help_functions as _help
import color_code as color
import pytohtml as pytohtml


class ItemSale:
    # total_items_info >>>
    # total_item 0
    # total_price 1
    # total_discount 2
    # total vat 3
    # payable 4 
    # paid 5
    # change 6
    
    # items to sale >>
    # item code 0
    # item name 1
    # unit price 2
    # quantity 3
    # discount 4
    # total 5
    # vat 6
    # payable 7
    # date 8
    def __init__(self,root):
        try:
            self.root = root
            self.items_to_sale = []
            self.total_items_info = [0,0,0,0,0,0,0]
            self.count_by_item_code = dict()
        except Exception as e:
            _help.show_message('warning',f'Occur exception while home object creating {e}')
        pass
    def back_home(self):
        self.main_frame.place_forget()
        
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
    
    
    def updateChange(self,event):
        try:
            total_paid = (int)(self.right_frame_payment_info_frame_total_paid.get())
            total_payable = (int)(self.right_frame_payment_info_frame_payable.cget('text'))
            total_change = total_paid-total_payable
            if total_change<0:
                _help.show_message('warning','Customer have to pay fully')
                return
            print(total_paid,total_payable,total_change)
            self.set_entry_value(self.right_frame_payment_info_frame_change,total_change)
        except ValueError:
            _help.show_message('warning','total paid contain non digit')
        except Exception as e:
            _help.show_message('warning',e)
        
        

    def deleteItem(self):
        del self.items_to_sale[self.selected_si-1]
        self.showTable()
        self.showTotalInfo()
        pass
        
    def clearItemEntries(self):
        for i in range(len(self.item_entries)-1):
            self.set_entry_value(self.item_entries[i],'')
        self.item_entries[0].focus_set()
    
    def showTotalInfo(self):
        for lbl,text in zip(self.total_info_lbl,self.total_items_info):
            lbl.config(text=format(text,'0.2f'))
            
            
    def addItemToSale(self):
        for i,entries in enumerate(self.item_entries):
            if entries.get()=='':
                _help.show_message('warning','Fill all fields carefully')
        item = [self.item_entries[0].get()] # code 0
        item += [self.item_entries[1].get()] # name 1
        item += [float(self.item_entries[6].get())] # unit price 2
        item += [float(self.item_entries[7].get())] # qty 3
        if item[0] in self.count_by_item_code.keys():
            for i in range(len(self.items_to_sale)):
                if self.items_to_sale[i][0]==item[0]:
                    if float(self.item_entries[9].get())!=self.items_to_sale[i][4]:
                        self.set_entry_value(self.item_entries[9],self.items_to_sale[i][4])
                        _help.show_message('warning','Discount can not be different of same products')
                    break
        
        item += [float(self.item_entries[9].get())] # discount 4
        item += [float(self.item_entries[10].get())] # total 5
        item += [float(self.item_entries[4].get())] # vat 6
        print(f"total {item[5]}  vat(%) {item[6]} payable =  {item[5]+item[5]*(item[6]/100)}")
        item += [item[5]+item[5]*(item[6]/100)] # payable 7
        item += [self.item_entries[11].get()] # date 8
        
        self.total_items_info[0] += item[3] # total item
        total_price = item[3]*item[2]
        self.total_items_info[1] += total_price # total price
        self.total_items_info[2] += (total_price-item[5]) # total discount
        self.total_items_info[3] += (item[7]-item[5]) # total vat
        self.total_items_info[4] += item[7] # payable
        
        if item[0] not in self.count_by_item_code.keys():
            if float(self.avl_qty)<item[3]:
                _help.show_message('warning','Not enough items')
                return
            self.count_by_item_code[item[0]] = item[3]
            self.items_to_sale.append(item)
        else:
            for i in range(len(self.items_to_sale)):
                if self.items_to_sale[i][0]==item[0]:
                    if float(self.avl_qty)<item[3]+self.items_to_sale[i][3]:
                        _help.show_message('warning','Not enough items')
                        return
                    self.count_by_item_code[item[0]] += item[3]
                    
                    self.items_to_sale[i][3] += item[3] # qty
                    self.items_to_sale[i][5] += item[5] # total
                    self.items_to_sale[i][7] += item[7] # discount
                
        self.showTable()
        self.clearItemEntries()
        self.showTotalInfo()
        self.item_entries[0].focus_set()
        pass
    
    def activeNextEntry(self,event,next_entry):
        next_entry.focus_set()
        
    def showItemDetails(self,event):
        code = self.item_entries[0].get()
        command = "SELECT code,name,group_,company,vat_rate,quantity,unit_sale_price\
                    FROM item_details, invoice\
                    WHERE code = ? AND item_details.invoice_id = invoice.invoice_id AND invoice.type='purchase';"
        values = [code]
        message = dao.get_rows(command,values)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        
        if len(message[1])==0:
            _help.show_message('warning','No items')
            return
        item_details = message[1][0]
        self.avl_qty = item_details[5] # available quantity
        for i,itm in enumerate(item_details):
            self.set_entry_value(self.item_entries[i],itm)
        
        
        print(item_details)
        self.item_entries[7].focus_set()
        pass
    
    def showItemDetails1(self,event):
        try:
            qty = (int)(self.item_entries[7].get())
            price = float(self.item_entries[6].get())
            self.set_entry_value(self.item_entries[8],qty*price)
            self.set_entry_value(self.item_entries[9],0)
            self.item_entries[9].focus_set()
        except ValueError:
            _help.show_message('warning','quantity or/and price contain non digit')
        except Exception as e:
            _help.show_message('warning',e)
    
    def showItemDetails2(self,event):
        try:
            discount = float(self.item_entries[9].get())
            price = float(self.item_entries[8].get())
            discount = (discount/100.0)*price
            self.set_entry_value(self.item_entries[10],price-discount)
        except ValueError:
            _help.show_message('warning','discount or/and price contain non digit')
        except Exception as e:
            _help.show_message('warning',e)          
        pass
        
    def middleFrame(self):
        item_info_list = ['Item Code :', 'Item Name :','Item Group :', 'Company :',
                          'VAT :', 'Available Quantity :','Sale Price Rate :','Sale Quantity :',
                          'Price :', 'Discount(%) :','Item Total Price :','Date :']
        for itm in range(0,len(item_info_list)):
            tk.Label(self.middle_frame, bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w', text=item_info_list[itm]
                ).place(relx=0.01,rely=itm*0.06+0.01,relwidth=0.46)                 
            
        self.item_entries_frame = [tk.Frame(self.middle_frame, bg=color.getColor('bd_input')) for i in range(len(item_info_list))]
        self.item_entries = [tk.Entry(self.item_entries_frame[i], bd=0) for i in range(len(item_info_list)-1)]
        self.item_entries.append(tkcal.DateEntry(self.item_entries_frame[11],date_pattern="dd/MM/yyyy"))
        for i in range(len(item_info_list)):
            self.item_entries_frame[i].place(relx=0.48,rely=0.01+i*0.06,relwidth=0.5,relheight=0.04)
            self.item_entries[i].pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
            _help.input_hover(self.item_entries_frame[i],self.item_entries[i])
        
        self.item_entries[0].focus_set()
        self.item_entries[0].bind("<Return>",self.showItemDetails)
        self.item_entries[7].bind("<Return>",self.showItemDetails1)
        self.item_entries[9].bind("<Return>",self.showItemDetails2)
        
        button_frame = [tk.Frame(self.middle_frame,bg=color.getColor('bd_button')) for i in range(2)]
        button_frame[0].place(relx=0.10,rely=0.8,relwidth=0.25,relheight=0.05)
        button_frame[1].place(relx=0.64,rely=0.8,relwidth=0.25,relheight=0.05)
        
        self.add_btn = tk.Button(button_frame[0],text='Add',bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), bd=0, font=('helvic',10), command=self.addItemToSale)
        self.delete_btn = tk.Button(button_frame[1],text='Delete',bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), font=('helvic',10), bd=0, command=self.deleteItem)
        self.add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        self.delete_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(button_frame[0],self.add_btn)
        _help.button_hover_del(button_frame[1],self.delete_btn)
    
    def searchFrame(self):
        tk.Label(self.right_frame,text='Search by :',  bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w').place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.05)
        tk.Label(self.right_frame,text='Query :', bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl') , anchor='w').place(relx=0.01, rely=0.07, relwidth=0.15, relheight=0.05)
        
        self.product_search_type = tk.StringVar()
        search_type_list = ['A/C name', "Phone"]
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.ttk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list)
        search_type.place(relx=0.16, rely=0.01, relwidth=0.2, relheight=0.06)
        
        self.query = tk.Entry(self.right_frame)
        self.query.place(relx=0.16,rely=0.07, relwidth=0.2, relheight=0.05)
        
        btn_frame = tk.Frame(self.right_frame,bg=color.getColor('bd_button'))
        btn_frame.place(relx=0.1, rely=0.13, width=90, height=22)
        self.search_btn = tk.Button(btn_frame,text='Search',fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), bd=0)
        self.search_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame,self.search_btn)
    
    def customerFrame(self):
        lbl_list = ['Name','Pre-balance','Current Balance', 'Contact']
        for i in range(len(lbl_list)):
            tk.Label(self.right_frame,text=lbl_list[i],bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w'\
                ).place(relx=0.01, rely=0.19+(i*0.06), relwidth=0.15, relheight=0.05)
        self.customer_entries = [tk.Entry(self.right_frame) for i in range(4)]
        for i in range(len(self.customer_entries)):
            self.customer_entries[i].place(relx=0.16,rely=0.19+(i*0.06),relwidth=0.2,relheight=0.05)
    
    def calcChange(self,event):
        try:
            self.set_entry_value(self.total_info_entries[1],format((float)(self.total_info_entries[0].get())-(float)(self.total_info_lbl[4].cget('text')),'0.2f'))
        except ValueError:
            _help.show_message('warning','total paid contain non digit')
        except Exception as e:
            _help.show_message('warning',e)  
    
    def totalFrame(self):
        lbl_list = ['Total Item :', 'Total Price :','Discount :','VAT :','Payable :','Total Paid :', 'Change :']
        for i in range(len(lbl_list)):
            tk.Label(self.right_frame,text=lbl_list[i],bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w'\
                ).place(relx=0.45, rely=0.01+(i*0.06), relwidth=0.15, relheight=0.05)
            
        self.total_info_lbl = [tk.Label(self.right_frame, bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl')) for i in range(5)]
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
        select_lbl = tk.Label(self.right_frame,text='Select A/C :',bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'),  anchor='w')
        select_lbl.place(relx=0.8,rely=0.15,relwidth=0.2,relheight=0.05)
        
        self.payment_acount = tk.StringVar()
        self.payment_acount.set(account_list[0]) # default value
        payment_acount_entry = tk.ttk.OptionMenu(self.right_frame, self.payment_acount, *account_list)
        payment_acount_entry.place(relx=0.8, rely=0.22, relwidth=0.2, relheight=0.05)
             
    def paymentFrame(self):
        tk.Label(self.right_frame,text='Payment Method :',bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w'\
            ).place(relx=0.8,rely=0.01,relwidth=0.2,relheight=0.05)
        
        self.payment_method_type = tk.StringVar()
        payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
        self.payment_method_type.set(payment_method_type_list[0]) # default value
        payment_method = tk.ttk.OptionMenu(self.right_frame, self.payment_method_type, *payment_method_type_list,command=self.paymentMethodSelect)
        payment_method.place(relx=0.8, rely=0.07, relwidth=0.2, relheight=0.05)
    
    
    def addInvoiceDB(self,row):
        command = "INSERT INTO invoice VALUES(?,?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,row)
        print("\n-----------invoice--------------\n",message)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        pass
    
    def addSaleHistoryDB(self,row):
        command = "INSERT INTO sale_purchase VALUES(?,?,?,?,?,?,?,?,?,?,?);"
        message = dao.set_rows(command,row)
        print("\n-----------insert sale pur--------------\n",message)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
    
    def completePayment(self):
        item_name = []
        item_qty = []
        item_price = []
        sum = 0
        vat = 0
        discount = 0
        for values in self.items_to_sale:
            item_name.append(values[1])
            item_qty.append(float(values[3]))
            item_price.append(float(values[2]))
            sum += (float)(values[2])*(float)(values[3])
            discount += (float)(values[2])*(float)(values[3])*(values[4]/100)
            tmp = ((float)(values[2])*(float)(values[3])) - (float)(values[2])*(float)(values[3])*(values[4]/100)
            vat += tmp*(values[6]/100)
            print(values[2],values[3])
            
        print(f"sum {sum},discount {discount},vat {vat}")
        try:
            total_info = [sum,discount,vat,sum-discount+vat]+[float(entries.get()) for entries in self.total_info_entries]
            print("tota ",total_info)
            print("sum ",sum-discount+vat)
            if total_info[5]=='' or total_info[4]=='' or (float)(total_info[4])<sum-discount+vat:
                _help.show_message('warning','Please pay carefully')
                return
        except ValueError:
            _help.show_message('warning','total paid contain non digit')
        except Exception as e:
            _help.show_message('warning',e)  
        
        for values in self.items_to_sale:
            command = "UPDATE item_details SET quantity = quantity - ? WHERE code = ?;"
            message = dao.update_rows(command,[values[3],values[0]])
            if message[0]==0:
                _help.show_message('warning',f"{message[1]} for code = {values[0]}")
                
        lastInvoiceId = dao.getLastInvoiceId()
        if lastInvoiceId[0]==0:
            _help.show_message('error',f'While creating new invoice id {lastInvoiceId[1]}')
            return
        print(self.total_items_info,"\n",len(self.total_items_info))
        row = [lastInvoiceId[1]+1,'sale',self.items_to_sale[0][8],dt.datetime.now().strftime("%I:%M:%S %p"),] +[self.total_items_info[i] for i in range(1,len(self.total_items_info))]
        print(row)
            
        self.addInvoiceDB(row)
        for values in self.items_to_sale:
            qty = values[3]
            price = values[2]
            total = qty*price
            discount = total*(values[4]/100)
            vat = (total-discount)*(values[4]/100)
            row = [values[0],values[1],qty,price,total,discount,vat,total+vat-discount,'','',lastInvoiceId[1]+1]
            self.addSaleHistoryDB(row)
        
        # update total amount of main acount
        message = dao.set_rows("UPDATE basic SET total_amount = total_amount+?;",[total_info[3]])
        if message[0]==0:
            _help.show_message('error',f'While updating total amount for sale item {message[1]}')
            return
        
        
        # self.back_home()
        obj = pytohtml.PythonToHtml()
        obj.saleReceipt('Sale item',self.items_to_sale[0][8],lastInvoiceId[1]+1,item_name=item_name,item_qty=item_qty,item_price=item_price,total_info=total_info)
        self.total_items_info = [0 for i in range(7)]
        self.showTotalInfo()
        self.set_entry_value(self.total_info_entries[0],0)
        self.set_entry_value(self.total_info_entries[1],0)
        self.items_to_sale.clear()
        self.showTable()
        _help.show_message('success','Successfully added a new transaction')
        pass    
    
    def on_select(self,event):
        selected_items = self.tree.selection()
        
        for item in selected_items:
            item_values = self.tree.item(item)["values"]
            self.selected_si = item_values[0]
                
    def showTable(self):
        table_frame = tk.Frame(self.right_frame,bg='#ffffff')
        table_frame.place(relx=0,rely=0.51,relwidth=1,relheight=0.49)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        columns = [f'c{i}' for i in range(1,11)]
        headings = ['SI','Code','Name','Price','QTY','Discount(%)','Total','VAT(%)','Payable','Date']
        column_size = [40] + [80 for i in range(2,11)]
        column_anchor = ['e','center','center','w','w','w','w','w','w','center']
        
        print(self.items_to_sale)
        # treeview
        self.tree = tk.ttk.Treeview(table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        
        for i in range(0,len(self.items_to_sale)):
            self.tree.insert("",tk.END,values=[i+1]+self.items_to_sale[i],tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
        
    def rightFrame(self):
        self.searchFrame()
        self.customerFrame()
        self.totalFrame()
        self.paymentFrame()
        
        btn_frame = [tk.Frame(self.right_frame,bg=color.getColor('bd_button')) for i in range(3)]
        btn_frame[0].place(relx=0.2,rely=0.45,width=90,height=22)
        btn_frame[1].place(relx=0.7,rely=0.45,width=90,height=22)

        back_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), text='Back', bd=0, command=self.back_home)
        back_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        payment_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), text='Payment', bd=0, command=self.completePayment)
        payment_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        _help.button_hover(btn_frame[0],back_btn)
        _help.button_hover(btn_frame[1],payment_btn)
        self.showTable()

        
    def itemSale(self):
        _help.init_page(self.root,'Item Sale')
        
        self.main_frame = tk.Frame(self.root,bg='#ffffff')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
    
        

        # ================================= middle frame ================================
        self.middle_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.middle_frame.place(relx=0.01,rely=0, relwidth=0.28, relheight=1)
        self.middleFrame()
        


        # ============================ right frame ============================ #
        self.right_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.right_frame.place(relx=0.3,rely=0,relwidth=0.69,relheight=1)
        self.rightFrame()


    def refresh(self):
        print('refresh home')
        _help.init_page(self.root,'Item Sale')
        self.addHome()

    
# root = tk.Tk()
# root.title('Shopping Inventory Management System')
# root.geometry('1100x650+10+10')
# root.minsize(1100,650)
# obj = ItemSale(root)
# obj.itemSale()
# root.mainloop()
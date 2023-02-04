import tkinter as tk
from PIL import ImageTk, Image
import datetime as dt 
import tkcalendar as tkcal
import datetime

import DAO as dao

import item_purchase as _item_purchase
import check_stock as _check_stock
import check_demage_stock as _check_demage_stock
import sales_report as _sales_report
import purchase_report as _purchase_report
import expenditure_manage as _expenditure_manage
import expenditure_report as _expenditure_report
import staff_manager as _staff_manager
import item_manage as _item_manage
import help_functions as _help
import color_code as color
import pytohtml as pytohtml

shop_name = None
phone = None
email = None
owner = None

# object of classes

# root window




# def update_date_time(time_lbl,date_lbl):
#     cur_time = dt.datetime.now().strftime("%I:%M:%S %p")
#     cur_date = dt.date.today().strftime("%B %d, %Y")
#     time_lbl.config(text=cur_time)
#     date_lbl.config(text=cur_date)
    
def init_page(root,page_name):
    # ============================ top frame 0 ============================
    top_frame_0 = tk.Frame(root,bg=color.color_list[0])
    top_frame_0.place(relx=0,rely=0,relwidth=1,relheight=0.12)
    # ---------------------------------------------------------------------
    # logo  (at frame 0)
    
    global shop_name,phone,email,owner
    if shop_name==None:
        print('retrieve')
        message = dao.get_rows("SELECT * FROM basic;",[])
        if message[0]==0:
            _help.show_message('error',f'While retreiving basic info {message[1]}')
            return
        message= message[1][0]
        print(message)
        shop_name = message[0]
        owner = message[1]
        phone = message[2]
        email = message[3]

    
    root.shop_logo = ImageTk.PhotoImage(Image.open("img/logo.png").resize((50,50)))
    top0_frame_0_lbl_0 = tk.Label(top_frame_0, image = root.shop_logo)
    top0_frame_0_lbl_0.place(relx=0.01, rely=0.1, relwidth=0.05, relheight=0.7)

    # shop name (at frame 0)
    top0_frame_0_lbl_1 = tk.Label(top_frame_0,text=shop_name , fg=color.color_list[1], bg=color.color_list[0], font=("Comic Sans MS", 20, "bold"))
    top0_frame_0_lbl_1.place(relx=0.07, rely=0.2)

    # shop owner's info (at frame 0)
    top0_frame_0_lbl_2 = tk.Label(top_frame_0,text=f"Mobile: {phone}\nEmail: {email}\nOwner: {owner}" , fg=color.color_list[1], bg=color.color_list[0], font=("Times New Roman", 12))
    top0_frame_0_lbl_2.place(relx=0.8, rely=0.1)
    
    # page name 
    top0_frame_0_lbl_3 = tk.Label(top_frame_0,text=page_name , fg=color.color_list[1], bg=color.color_list[0], font=("Times New Roman", 17,"bold"))
    top0_frame_0_lbl_3.place(relx=0.43, rely=0.3)




    # ============================ top frame 1 ============================
    top_frame_1 = tk.Frame(root,bg=color.color_list[2])
    top_frame_1.place(relx=0,rely=0.12,relwidth=1,relheight=0.05)
    # ---------------------------------------------------------------------
    # welcome  (at frame 1)
    top_frame_1_lbl_0 = tk.Label(top_frame_1,text="Welcome to abc Fasion House" , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_0.pack(side=tk.LEFT,padx=50)

    # date (at frame 1)
    cur_date = dt.date.today().strftime("%B %d, %Y")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_date , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # time (at frame 1)
    cur_time = dt.datetime.now().strftime("%I:%M:%S %p")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_time , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # tittle (at frame 1)
    # top_frame_1_lbl_1 = tk.Label(top_frame_1,text="Home" , fg=color.color_list[3], bg=color.color_list[2], font=("Comic Sans MS",12))
    # top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

def manage_item(root):
    print("go to manage item")
    init_page(root,'Manage Item')
    item_manage_obj.item_manage()

def purchase_item(root):
    print('go to purchase item')
    init_page(root,'Purchase Item')
    item_purchase_obj.itemPurchase()
    

def check_stock(root):
    print('go to check stock')
    init_page(root,'Check Stock Item')
    check_stock_obj.checkStock()    

def check_demage_stock(root):
    print('go to demage check')
    init_page(root,'Deamge Stock Item')
    demage_stock_obj.demageStock()

def purchase_report(root):
    print('go to purchase report')
    init_page(root,'Purchase report')
    purchase_report_obj.purchaseReport()

def sales_report(root):
    print('go to sales report')
    init_page(root,'Sales Report')
    sales_report_obj.salesReport()



def expenditure(root):
    print('go to expenditure')
    expenditure_manage_obj.expenditureManage()

def expenditure_report(root):
    print('go to expenditure report')
    init_page(root,'Expenditure Report')
    expenditure_report_obj.expenditureReport()

def staff_manager(root):
    print('go to staff manager')
    _staff_manager.staff_manager(root)

def contact_book(root):
	print('go to contact_book')



# class Item:
#     def __init__(self):
#         self.item_name=None
#         self.item_code=None
#         self.item_quantity=None
#         self.item_price=None
#         self.available=None
#         self.discount=None
#         self.total_item_price=None
#         pass
#     def __init__(self,values):
#         self.item_name=values[0]
#         self.item_code=values[1]
#         self.item_quantity=values[2]
#         self.item_price=values[3]
#         self.available=values[4]
#         self.discount=values[5]
#         self.total_item_price=values[6]
#         pass  
#     def set_values(self,values):
#         self.item_name=values[0]
#         self.item_code=values[1]
#         self.item_quantity=values[2]
#         self.item_price=values[3]
#         self.available=values[4]
#         self.discount=values[5]
#         self.total_item_price=values[6]
        

class Home:
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
        self.root = root
        global item_manage_obj,item_purchase_obj,check_stock_obj
        global demage_stock_obj,purchase_report_obj,sales_report_obj
        global expenditure_manage_obj,expenditure_report_obj
        item_manage_obj = _item_manage.Item_Manage(root)
        item_purchase_obj = _item_purchase.Item_Purchase(root)
        check_stock_obj = _check_stock.CheckStock(root)
        demage_stock_obj = _check_demage_stock.DemageStcok(root)
        purchase_report_obj = _purchase_report.PurchaseReport(root)
        sales_report_obj = _sales_report.SalesReport(root)
        expenditure_manage_obj = _expenditure_manage.ExpenditureManage(root)
        expenditure_report_obj = _expenditure_report.ExpenditureReport(root)
        
        self.items_to_sale = []
        self.total_items_info = [0,0,0,0,0,0,0]
        self.count_by_item_code = dict()
        pass
    def back_home(self):
        self.main_frame.place_forget()
        
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
    
    
    def updateChange(self,event):
        total_paid = (int)(self.right_frame_payment_info_frame_total_paid.get())
        total_payable = (int)(self.right_frame_payment_info_frame_payable.cget('text'))
        total_change = total_paid-total_payable
        if total_change<0:
            _help.show_message('warning','Customer have to pay fully')
            return
        print(total_paid,total_payable,total_change)
        self.set_entry_value(self.right_frame_payment_info_frame_change,total_change)
        
    def leftFrame(self):
        # ---------------------------operation button--------------------------- #
        operation_name = ['Manage Item','Purchase Item','Check Stock','Demage Stock','Purchase Report',
                          'Sales Report','Expenditure','Expenditure Report','Staff Manager','Contact Book']
        self.operation_btn = [tk.Button(self.left_frame,text=operation_name[i], fg=color.color_list[3], bg=color.color_list[5]) for i in range(len(operation_name))]
        
        for btn in self.operation_btn:
            btn.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)
        self.operation_btn[0].config(command=lambda:manage_item(self.root))
        self.operation_btn[1].config(command=lambda:purchase_item(self.root))
        self.operation_btn[2].config(command=lambda:check_stock(self.root))
        self.operation_btn[3].config(command=lambda:check_demage_stock(self.root))
        self.operation_btn[4].config(command=lambda:purchase_report(self.root))
        self.operation_btn[5].config(command=lambda:sales_report(self.root))
        self.operation_btn[6].config(command=lambda:expenditure(self.root))
        self.operation_btn[7].config(command=lambda:expenditure_report(self.root))
        self.operation_btn[8].config(command=lambda:staff_manager(self.root))
        self.operation_btn[9].config(command=lambda:contact_book(self.root))

        # Refresh (at left_frame0) 
        self.left_frame_btn_11 = tk.Button(self.left_frame,text="Refresh", fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=self.refresh)
        self.left_frame_btn_11.pack(side=tk.TOP,fill=tk.X,padx=5, pady=15)

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
        qty = (int)(self.item_entries[7].get())
        price = float(self.item_entries[6].get())
        self.set_entry_value(self.item_entries[8],qty*price)
        self.set_entry_value(self.item_entries[9],0)
        self.item_entries[9].focus_set()

    
    def showItemDetails2(self,event):
        discount = float(self.item_entries[9].get())
        price = float(self.item_entries[8].get())
        discount = (discount/100.0)*price
        self.set_entry_value(self.item_entries[10],price-discount)
        pass
        
    def middleFrame(self):
        item_info_list = ['Item Code :', 'Item Name :','Item Group :', 'Company :',
                          'VAT :', 'Available Quantity :','Sale Price Rate :','Sale Quantity :',
                          'Price :', 'Discount(%) :','Item Total Price :','Date :']
        for itm in range(0,len(item_info_list)):
            tk.Label(self.middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text=item_info_list[itm]
                ).place(relx=0.01,rely=itm*0.06+0.01,relwidth=0.46)                 
        self.item_entries = [tk.Entry(self.middle_frame) for itm in range(0,len(item_info_list)-1)]
        self.item_entries.append(tkcal.DateEntry(self.middle_frame))
        for i,entries in enumerate(self.item_entries):
            entries.place(relx=0.46,rely=i*0.06+0.02,relwidth=0.5)
        
        self.item_entries[0].bind("<Return>",self.showItemDetails)
        self.item_entries[7].bind("<Return>",self.showItemDetails1)
        self.item_entries[9].bind("<Return>",self.showItemDetails2)
        
        # self.item_entries[7].bind("<Return>",lambda e,next_entry=self.item_entries[9]: self.activeNextEntry(e,next_entry))
        self.item_entries[0].focus_set()
        
            
        # delete item
        tk.Button(self.middle_frame, fg=color.color_list[1], bg=color.color_list[6],font=('Times New Roman',14), text='Delete',command=self.deleteItem
            ).place(relx=0.02,rely=0.92, height=25)
        # add item to sell
        tk.Button(self.middle_frame, fg=color.color_list[3], bg=color.color_list[2],font=('Times New Roman',14), text='Add item',command=self.addItemToSale
            ).place(relx=0.7,rely=0.92, height=25)
        
    
    def searchFrame(self):
        tk.Label(self.right_frame,text='Search by :', bg=color.color_list[7], anchor='w').place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.05)
        tk.Label(self.right_frame,text='Query :', bg=color.color_list[7], anchor='w').place(relx=0.01, rely=0.07, relwidth=0.15, relheight=0.05)
        
        self.product_search_type = tk.StringVar()
        search_type_list = ['A/C name', "Phone"]
        self.product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(self.right_frame, self.product_search_type, *search_type_list)
        search_type.place(relx=0.16, rely=0.01, relwidth=0.2, relheight=0.06)
        
        self.query = tk.Entry(self.right_frame)
        self.query.place(relx=0.16,rely=0.07, relwidth=0.2, relheight=0.05)
        
        self.search_btn = tk.Button(self.right_frame,text='Search',bg=color.color_list[2])
        self.search_btn.place(relx=0.1, rely=0.13, relwidth=0.15, relheight=0.05)
    
    def customerFrame(self):
        lbl_list = ['Name','Pre-balance','Current Balance', 'Contact']
        for i in range(len(lbl_list)):
            tk.Label(self.right_frame,text=lbl_list[i],bg=color.color_list[7], anchor='w'\
                ).place(relx=0.01, rely=0.19+(i*0.06), relwidth=0.15, relheight=0.05)
        self.customer_entries = [tk.Entry(self.right_frame) for i in range(4)]
        for i in range(len(self.customer_entries)):
            self.customer_entries[i].place(relx=0.16,rely=0.19+(i*0.06),relwidth=0.2,relheight=0.05)
    
    def calcChange(self,event):
        self.set_entry_value(self.total_info_entries[1],format((float)(self.total_info_entries[0].get())-(float)(self.total_info_lbl[4].cget('text')),'0.2f'))
    
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
        select_lbl.place(relx=0.8,rely=0.15,relwidth=0.2,relheight=0.05)
        
        self.payment_acount = tk.StringVar()
        self.payment_acount.set(account_list[0]) # default value
        payment_acount_entry = tk.OptionMenu(self.right_frame, self.payment_acount, *account_list)
        payment_acount_entry.place(relx=0.8, rely=0.22, relwidth=0.2, relheight=0.05)
             
    def paymentFrame(self):
        tk.Label(self.right_frame,text='Payment Method :',bg=color.color_list[7], anchor='w'\
            ).place(relx=0.8,rely=0.01,relwidth=0.2,relheight=0.05)
        
        self.payment_method_type = tk.StringVar()
        payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
        self.payment_method_type.set(payment_method_type_list[0]) # default value
        payment_method = tk.OptionMenu(self.right_frame, self.payment_method_type, *payment_method_type_list,command=self.paymentMethodSelect)
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
        total_info = [sum,discount,vat,sum-discount+vat]+[float(entries.get()) for entries in self.total_info_entries]
        print("tota ",total_info)
        print("sum ",sum-discount+vat)
        if total_info[5]=='' or total_info[4]=='' or (float)(total_info[4])<sum-discount+vat:
            _help.show_message('warning','Please pay carefully')
            return
        
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
        row = [lastInvoiceId[1]+1,'sale',self.items_to_sale[0][8],dt.datetime.now().strftime("%I:%M:%S %p"),] +[self.total_items_info[i] for i in range(1,7)]
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
        table_frame = tk.Frame(self.right_frame,bg=color.color_list[1])
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
        tk.Button(self.right_frame,text='Payment',bg=color.color_list[2],command=self.completePayment).place(relx=0.45,rely=0.45,relwidth=0.1,relheight=0.05)
        self.showTable()

        
    def addHome(self):
        init_page(self.root,'Item Sale')
        # global item_manage_obj
        # item_manage_obj = _item_manage.Item_Manage(self.root)
        # global item_purchase_obj
        # item_purchase_obj = _item_purchase.Item_Purchase(self.root)
        
        self.main_frame = tk.Frame(self.root,bg=color.color_list[1])
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        # ============================ left frame 0 ============================
        self.left_frame = tk.Frame(self.main_frame,bg=color.color_list[4])
        self.left_frame.place(relx=0.005,rely=0, relwidth=0.15, relheight=1)
        self.leftFrame()
        

        # ================================= middle frame ================================
        self.middle_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.middle_frame.place(relx=0.16,rely=0, relwidth=0.28, relheight=1)
        self.middleFrame()
        


        # ============================ right frame ============================ #
        self.right_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.right_frame.place(relx=0.45,rely=0,relwidth=0.545,relheight=1)
        self.rightFrame()


    def refresh(self):
        print('refresh home')
        init_page(self.root,'Item Sale')
        self.addHome()

    
# root = tk.Tk()
# root.title('Shopping Inventory Management System')
# root.geometry('1100x650+10+10')
# root.minsize(1100,650)
# addHome(root)
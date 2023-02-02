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
import item_sales_report as _item_sales_report
import purchase_report as _purchase_report
import expenditure_report as _expenditure_report
import staff_manager as _staff_manager
import item_manage as _item_manage
import help_functions as _help_functions
import color_code as color
import pytohtml as pytohtml


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
    root.shop_logo = ImageTk.PhotoImage(Image.open("img/logo.png").resize((50,50)))
    top0_frame_0_lbl_0 = tk.Label(top_frame_0, image = root.shop_logo)
    top0_frame_0_lbl_0.place(relx=0.01, rely=0.1, relwidth=0.05, relheight=0.7)

    # shop name (at frame 0)
    top0_frame_0_lbl_1 = tk.Label(top_frame_0,text="abc Fashion House" , fg=color.color_list[1], bg=color.color_list[0], font=("Comic Sans MS", 20, "bold"))
    top0_frame_0_lbl_1.place(relx=0.07, rely=0.2)

    # shop owner's info (at frame 0)
    top0_frame_0_lbl_2 = tk.Label(top_frame_0,text="Mobile: +8801xxxxxxxxx\nEmail: abc@xxxxx.com\nOwner: abc" , fg=color.color_list[1], bg=color.color_list[0], font=("Times New Roman", 12))
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
    item_manage_obj.item_manage(root)

def purchase_item(root):
    print('go to purchase item')
    init_page(root,'Purchase Item')
    item_purchase_obj.item_purchase(root)
    

def check_stock(root):
    print('go to check stock')
    init_page(root,'Check Stock Item')
    _check_stock.check_stock(root)    

def check_demage_stock(root):
    print('go to demage check')
    init_page(root,'Deamge Stock Item')
    _check_demage_stock.check_demage_stock(root)

def purchase_report(root):
    print('go to purchase report')
    init_page(root,'Purchase report')
    _purchase_report.purchase_report(root)

def sales_report(root):
    print('go to sales report')
    init_page(root,'Sales Report')
    _sales_report.sales_report(root)

def item_sales_report(root):
    print('go to demage check')
    init_page(root,'Item-Sales Report')
    _item_sales_report.item_sales_report(root)


def expenditure(root):
	print('go to expenditure')

def expenditure_report(root):
    print('go to expenditure report')
    init_page(root,'Expenditure Report')
    _expenditure_report.expenditure_report(root)

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
    # total_item
    # total_price
    # total_discount
    # payable 
    # paid
    # change
    
    # items to sale >>
    # item name
    # item code
    # quantity 
    # unit price 
    # avlabl qty 
    # discount 
    # payable
    
    def __init__(self,root):
        self.root = root
        self.items_to_sale = []
        self.total_items_info = [0,0,0,0,0,0]
        self.count_by_item_code = dict()
        pass
    
    def set_entry_value(self,entry_name,entry_value):
        entry_name.delete(0,"end")
        entry_name.insert(0,entry_value)
    def query_show(self,event):
        command = f"SELECT * FROM item_details WHERE item_code = '{self.item_code.get()}'"
        self.item_details = dao.get_rows(command)
        if self.item_details[0]==0:
            _help_functions.show_message('error',self.item_details[1])
            return
        elif len(self.item_details[1])==0:
            _help_functions.show_message('warning','No item according to the item code')
            return
        self.item_details=list(self.item_details[1][0])
        
        if self.item_details[1] in self.count_by_item_code:
            self.item_details[6] = (int)(self.item_details[6])- self.count_by_item_code[self.item_details[1]]
        self.set_entry_value(self.item_name,self.item_details[0])
        self.set_entry_value(self.sale_price_rate,self.item_details[8])
        self.set_entry_value(self.discount,"0")
        self.set_entry_value(self.sale_quantity,1)
        self.middle_frame_lbl_item_name.config(text=self.item_details[0])
        self.middle_frame_lbl_item_code.config(text=self.item_details[1])
        self.middle_frame_lbl_item_group.config(text=self.item_details[3])
        self.middle_frame_lbl_company.config(text=self.item_details[4])
        self.middle_frame_lbl_shelf_no.config(text=self.item_details[5])
        self.middle_frame_lbl_avl_quantity.config(text=self.item_details[6])
        self.middle_frame_lbl_price.config(text=self.item_details[8])
        self.middle_frame_lbl_total_price.config(text=self.item_details[8])
        pass
    
    def update_total_price_label(self,event):
        cur_discount = (int)(self.discount.get())
        cur_quantity = (int)(self.sale_quantity.get())
        cur_price = (int)(self.middle_frame_lbl_price.cget('text'))
        self.middle_frame_lbl_total_price.config(text=cur_price*cur_quantity*((100-cur_discount)/100))
        
        
    def add_item_to_sale(self):
        try:
            item = [self.item_details[0],self.item_details[1],(int)(self.sale_quantity.get()),(int)(self.item_details[8]),(int)(self.item_details[6]),(int)(self.discount.get())]        
        except ValueError:
            _help_functions.show_message('error','Please write item code')
        except AttributeError:
            _help_functions.show_message('error','Please write item code')
        except Exception as e:
            _help_functions.show_message('error',e)
        
        if self.item_details[1] not in self.count_by_item_code:
            self.count_by_item_code[self.item_details[1]] = item[2]
        else:
            self.count_by_item_code[self.item_details[1]] += item[2]
        print(self.count_by_item_code[self.item_details[1]],self.item_details[6])
        if self.count_by_item_code[self.item_details[1]] > (int)(self.item_details[6]):
            self.count_by_item_code[self.item_details[1]] -= item[2]
            print("updated ",self.count_by_item_code[self.item_details[1]])
            _help_functions.show_message('warning',"Not enough in stock")
            return
        item.append(item[2]*item[3]*((100-item[5])/100))
        # item = [self.item_name.get(),self.item_code.get(),(int)(self.sale_quantity.get()),"150","10","0","150"]
        self.total_items_info[0] += item[2]
        self.total_items_info[1] += item[3]*item[2]
        self.total_items_info[2] += item[2]*item[3]*(item[5]/100)
        self.total_items_info[3] = (self.total_items_info[1]-self.total_items_info[2])
        self.total_items_info[4] = 0
        self.total_items_info[5] = 0
        
        self.items_to_sale.append(item)
        
        self.middle_frame_lbl_avl_quantity.config(text=(int)(self.item_details[6])-self.count_by_item_code[self.item_details[1]])
        
        # clear all
        self.set_entry_value(self.item_name,'')
        self.set_entry_value(self.item_code,'')
        self.set_entry_value(self.sale_price_rate,'')
        self.set_entry_value(self.discount,'')
        self.set_entry_value(self.sale_quantity,'')
        self.middle_frame_lbl_item_name.config(text='')
        self.middle_frame_lbl_item_code.config(text='')
        self.middle_frame_lbl_item_group.config(text='')
        self.middle_frame_lbl_company.config(text='')
        self.middle_frame_lbl_shelf_no.config(text='')
        self.middle_frame_lbl_avl_quantity.config(text='')
        self.middle_frame_lbl_price.config(text='')
        self.middle_frame_lbl_total_price.config(text='')
        
        self.show_table(self.items_to_sale)
        self.show_total_items_info()
        
        pass
    
    def show_total_items_info(self):
        # total item 
        self.right_frame_payment_info_frame_total_item.config(text=self.total_items_info[0])

        # total price
        self.right_frame_payment_info_frame_total_price.config(text=self.total_items_info[1])

        # discount 
        self.right_frame_payment_info_frame_discount.config(text=self.total_items_info[2])

        # Payable
        self.right_frame_payment_info_frame_payable.config(text=self.total_items_info[3])
        pass
        
        
    def delete_item(self):
        try:
            if self.selected_intex_to_delete==None:
                _help_functions.show_message('warning','select one')
                return
        except AttributeError:
            _help_functions.show_message('warning','select one')
        
        item = self.items_to_sale[self.selected_intex_to_delete]
        self.total_items_info[0] -= item[2]
        self.total_items_info[1] -= item[3]
        self.total_items_info[2] -= (item[2]*item[3]*(item[5]/100))
        self.total_items_info[3] = (self.total_items_info[1]-self.total_items_info[2])
        
        self.count_by_item_code[self.items_to_sale[self.selected_intex_to_delete][1]] -= (int)(self.items_to_sale[self.selected_intex_to_delete][4])
        del self.items_to_sale[self.selected_intex_to_delete]
        self.selected_intex_to_delete=None
        self.show_table(self.items_to_sale)
        self.show_total_items_info()
        _help_functions.show_message('success','Deleted')
        pass
    
    def print_receipt(self,item_name,item_qty,item_price,total_info):
        preview = pytohtml.PythonToHtml()
        preview.saleReceipt(item_name,item_qty,item_price,total_info)
        pass
    
    def payment_process(self):
        if self.payment_method_type.get()=='Cash':
            item_name = []
            item_qty = []
            item_price = []
            total_info = [self.total_items_info[1],self.total_items_info[2],self.total_items_info[3]
                          ,self.right_frame_payment_info_frame_total_paid.get(),self.right_frame_payment_info_frame_change.get()]
            
            if self.right_frame_payment_info_frame_total_paid.get()=='' or self.right_frame_payment_info_frame_change.get()=='':
                _help_functions.show_message('warning','Type paid amount and press enter') 
                return
            self.new_invoice_number = dao.get_new_invoice()
            if(self.new_invoice_number[0]==0):
                _help_functions.show_message('error',self.new_invoice_number[1])
                return
            print("inv num",self.new_invoice_number)
            self.new_invoice_number[1]+=1
            cur_date = datetime.date.today()
            cur_time = datetime.datetime.now().time()
            command = "INSERT INTO invoice VALUES(?,?,?,?,?,?,?,?,?);"
            values = [self.new_invoice_number[1],'sale',cur_date.strftime("%d:%m:%Y") ,cur_time.strftime("%H:%M:%S"),self.total_items_info[1],
                      self.total_items_info[2],self.total_items_info[3],self.right_frame_payment_info_frame_total_paid.get(),
                      self.right_frame_payment_info_frame_change.get()]
            print(values)
            message = dao.set_rows(command,values)
            print(message)
            if(message[0]==0):
                _help_functions.show_message('error',message[1])
                return
            command = "INSERT INTO invoice_product_details VALUES(?,?,?,?,?,?);"
            for item in self.items_to_sale:
                item_name.append(item[0])
                item_qty.append(item[2])
                item_price.append(item[3])
                values = [item[1],(int)(item[2]),(float)(item[2]*item[3]),float(item[5]),float(item[6]),self.new_invoice_number[1]]
                # print(values)
                # print(self.new_invoice_number)
                message = dao.set_rows(command,values)
                if message[0]==0:
                    _help_functions.show_message('error',message[1])
                    return
            for code, avl in self.count_by_item_code.items():
                print(code, avl)
                command = "UPDATE item_details SET item_quantity=item_quantity-? WHERE item_code = ?;"
                message = dao.update_rows(command,values=[avl,code])
                if message[0]==0:
                    _help_functions.show_message('error',message[1])
                    return
                message = dao.get_rows("SELECT * FROM item_details;")
                for row in message[1]:
                    print(row)
            self.print_receipt(item_name,item_qty,item_price,total_info)
            self.clear_payment()
            _help_functions.show_message('success','successfully completed a transaction')
        # self.right_frame_payment_info_frame_change
        pass
    
    def  clear_payment(self):
        self.items_to_sale.clear()
        self.show_table(self.items_to_sale)
        self.count_by_item_code.clear()
        self.right_frame_payment_info_frame_total_item.config(text='')
        self.right_frame_payment_info_frame_total_price.config(text='')
        self.right_frame_payment_info_frame_discount.config(text='')
        self.right_frame_payment_info_frame_payable.config(text='')
        self.set_entry_value(self.right_frame_payment_info_frame_total_paid,'')
        self.set_entry_value(self.right_frame_payment_info_frame_change,'')
        pass
        
    
    
    def update_change(self,event):
        total_paid = (int)(self.right_frame_payment_info_frame_total_paid.get())
        total_payable = (int)(self.right_frame_payment_info_frame_payable.cget('text'))
        total_change = total_paid-total_payable
        if total_change<0:
            _help_functions.show_message('warning','Customer have to pay fully')
            return
        print(total_paid,total_payable,total_change)
        self.set_entry_value(self.right_frame_payment_info_frame_change,total_change)
        
                
    def addHome(self):
        init_page(self.root,'Item Sale')
        global item_manage_obj
        item_manage_obj = _item_manage.Item_Manage(self.root)
        global item_purchase_obj
        item_purchase_obj = _item_purchase.Item_Purchase(self.root)
        
        # item manage main frame
        main_frame = tk.Frame(self.root,bg='white')
        main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        # ============================ left frame 0 ============================
        left_frame = tk.Frame(main_frame,bg=color.color_list[4])
        left_frame.place(relx=0.005,rely=0, relwidth=0.15, relheight=1)

        # ---------------------------operation button--------------------------- #
        self.left_frame_btn_manage_item = tk.Button(left_frame,text='Manage Item', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:manage_item(self.root))
        self.left_frame_btn_manage_item.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_purchase_item = tk.Button(left_frame,text='Purchase Item', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:purchase_item(self.root))
        self.left_frame_btn_purchase_item.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_check_stock = tk.Button(left_frame,text='Check Stock', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:check_stock(self.root))
        self.left_frame_btn_check_stock.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_demage_stock = tk.Button(left_frame,text='Demage Stock', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:check_demage_stock(self.root))
        self.left_frame_btn_demage_stock.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_purchase_report = tk.Button(left_frame,text='Purchase Report', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:purchase_report(self.root))
        self.left_frame_btn_purchase_report.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_sales_report = tk.Button(left_frame,text='Sales Report', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:sales_report(self.root))
        self.left_frame_btn_sales_report.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_item_sales_report = tk.Button(left_frame,text='Item Sales Report', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:item_sales_report(self.root))
        self.left_frame_btn_item_sales_report.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_expenditure = tk.Button(left_frame,text='Expenditure', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:expenditure(self.root))
        self.left_frame_btn_expenditure.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_expenditure_report = tk.Button(left_frame,text='Expenditure Report', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:expenditure_report(self.root))
        self.left_frame_btn_expenditure_report.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_staff_manager = tk.Button(left_frame,text='Staff Manager', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:staff_manager(self.root))
        self.left_frame_btn_staff_manager.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

        self.left_frame_btn_contact_book = tk.Button(left_frame,text='Contact Book', fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=lambda:contact_book(self.root))
        self.left_frame_btn_contact_book.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)


        # for op in range(0,len(operation_list)-1):
        #     left_frame_btn[op] = tk.Button(left_frame,text=operation_list[op], fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10))
        #     left_frame_btn[op].pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)
        
        #Manage button commanf
        # left_frame_btn[0].config(command=lambda:manage_item(self.root))
        
        # Refresh (at left_frame0) 
        self.left_frame_btn_11 = tk.Button(left_frame,text="Refresh", fg=color.color_list[3], bg=color.color_list[5], font=('Times New Roman1',10),command=self.refresh)
        self.left_frame_btn_11.pack(side=tk.TOP,fill=tk.X,padx=5, pady=15)


        # ================================= middle frame ================================
        middle_frame = tk.Frame(main_frame,bg=color.color_list[7])
        middle_frame.place(relx=0.16,rely=0, relwidth=0.28, relheight=1)

        # ---------------------------------------------------------------------- #
        self.purchase_date = tkcal.DateEntry(middle_frame,selecmode='day', cursor='hand1')
        self.purchase_date.place(relx=0.55,y=5,relwidth=0.4)

        item_info_list = ['Item Name :', 'Item Code :', 'Item Name :', 'Item Code :',
                        'Item Group :', 'Company :', 'Shelf No. :', 'Available Quantity :',
                        'Sale Price Rate :', 'Sale Quantity :', 'Price :', 'Discount :',
                        'Item Total Price :']


        for itm in range(0,len(item_info_list)):
            middle_frame_lbl_0 = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text=item_info_list[itm])
            middle_frame_lbl_0.place(x=5,y=(itm+1)*30,relwidth=0.5)    


        # delete item
        self.left_frame_btn_delete = tk.Button(middle_frame, fg=color.color_list[3], bg=color.color_list[2],font=('Times New Roman',14), text='Delete',command=self.delete_item)
        self.left_frame_btn_delete.place(relx=0.02,rely=0.92, height=25)

        self.check_free = tk.IntVar()
        tk.Checkbutton(middle_frame, bg=color.color_list[2], font=('Times New Roman',14), text='Free', variable=self.check_free).place(relx=0.37,rely=0.92,height=25)
        # add item to sell
        self.left_frame_btn_add = tk.Button(middle_frame, fg=color.color_list[3], bg=color.color_list[2],font=('Times New Roman',14), text='Add item',command=self.add_item_to_sale)
        self.left_frame_btn_add.place(relx=0.7,rely=0.92, height=25)


        # --------------------------------product input box------------------------------- #

        self.item_name = tk.Entry(middle_frame)
        self.item_name.place(relx=0.5, y=33, relwidth=0.48, relheight=0.04)

        self.item_code = tk.Entry(middle_frame)
        self.item_code.place(relx=0.5, y=63, relwidth=0.48, relheight=0.04)
        self.item_code.bind("<Return>", self.query_show)
        # tk.Button(middle_frame,text='f',command=self.query_show).place(relx=0.98,y=63,width=10,height=10)

        self.sale_price_rate = tk.Entry(middle_frame)
        self.sale_price_rate.place(relx=0.5, y=273, relwidth=0.48, relheight=0.04)

        self.sale_quantity = tk.Entry(middle_frame)
        self.sale_quantity.place(relx=0.5, y=303, relwidth=0.48, relheight=0.04)
        self.sale_quantity.bind("<Return>",self.update_total_price_label)

        self.discount = tk.Entry(middle_frame)
        self.discount.place(relx=0.5, y=363, relwidth=0.48, relheight=0.04)
        self.discount.bind("<Return>",self.update_total_price_label)

        # --------------------------------product info box------------------------------- #

        # Item Name (at left_frame1)
        self.middle_frame_lbl_item_name = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_item_name.place(relx=0.5, y=90, relwidth=0.48, relheight=0.04)

        # Item Code (at left_frame1)
        self.middle_frame_lbl_item_code = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_item_code.place(relx=0.5, y=120, relwidth=0.48, relheight=0.04)

        # Item Group (at left_frame1)
        self.middle_frame_lbl_item_group = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_item_group.place(relx=0.5, y=150, relwidth=0.48, relheight=0.04)

        # Company (at left_frame1)
        self.middle_frame_lbl_company = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_company.place(relx=0.5, y=180, relwidth=0.48, relheight=0.04)

        # Shelf No. (at left_frame1)
        self.middle_frame_lbl_shelf_no = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_shelf_no.place(relx=0.5, y=210, relwidth=0.48, relheight=0.04)

        # Available Quantity (at left_frame1)
        self.middle_frame_lbl_avl_quantity = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_avl_quantity.place(relx=0.5, y=240, relwidth=0.48, relheight=0.04)

        # Price
        self.middle_frame_lbl_price = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_price.place(relx=0.5, y=330, relwidth=0.48, relheight=0.04)

        # Item Total Price (at left_frame1)
        self.middle_frame_lbl_total_price = tk.Label(middle_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',14), text='')
        self.middle_frame_lbl_total_price.place(relx=0.5, y=390, relwidth=0.48, relheight=0.04)



        # ============================ left frame 2 ============================ #
        right_frame = tk.Frame(main_frame,bg=color.color_list[7])
        right_frame.place(relx=0.45,rely=0,relwidth=0.545,relheight=1)

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
        
        payment_button = tk.Button(right_frame_customer_info_frame,text='Payment', bg=color.color_list[2],command=self.payment_process)
        payment_button.place(relx=0.8,rely=0.9,height=30)

        # ---------------------------- Input ------------------------------ #
        product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(right_frame_customer_info_frame, product_search_type, *search_type_list)
        search_type.place(relx=0.3, rely=0.01, relwidth=0.6, relheight=0.09)

        query = tk.Entry(right_frame_customer_info_frame)
        query.place(relx=0.3, rely=0.11, relwidth=0.6, relheight=0.08)

        customer_name = tk.Entry(right_frame_customer_info_frame)
        customer_name.place(relx=0.42, rely=0.3, relwidth=0.48, relheight=0.08)

        pre_balance = tk.Entry(right_frame_customer_info_frame)
        pre_balance.place(relx=0.42, rely=0.4, relwidth=0.48, relheight=0.08)

        current_balance = tk.Entry(right_frame_customer_info_frame)
        current_balance.place(relx=0.42, rely=0.5, relwidth=0.48, relheight=0.08)

        contact_no = tk.Entry(right_frame_customer_info_frame)
        contact_no.place(relx=0.42, rely=0.6, relwidth=0.48, relheight=0.08)


        # ---------------------------- payment info frame ----------------------------- #
        right_frame_payment_info_frame = tk.Frame(right_frame,bg=color.color_list[7])
        right_frame_payment_info_frame.place(relx=0.5,rely=0.01,relwidth=0.49,relheight=0.6)

        purchase_info_list = ['Total Item :', 'Total Price :', 'Discount :',
                            'Payable :', 'Total Paid :', 'Change/Due :']
        for i in range(0,len(purchase_info_list)):
            right_frame_payment_info_frame_lbl = tk.Label(right_frame_payment_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text=purchase_info_list[i])
            right_frame_payment_info_frame_lbl.place(relx=0.01, rely=0.01+0.1*i, relwidth=0.4, relheight=0.08)     



        # total item 
        self.right_frame_payment_info_frame_total_item = tk.Label(right_frame_payment_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font))
        self.right_frame_payment_info_frame_total_item.place(relx=0.42, rely=0.01, relwidth=0.4, relheight=0.08)

        # total price
        self.right_frame_payment_info_frame_total_price = tk.Label(right_frame_payment_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font))
        self.right_frame_payment_info_frame_total_price.place(relx=0.42, rely=0.1, relwidth=0.4, relheight=0.08)

        # discount 
        self.right_frame_payment_info_frame_discount = tk.Label(right_frame_payment_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font))
        self.right_frame_payment_info_frame_discount.place(relx=0.42, rely=0.2, relwidth=0.4, relheight=0.08)

        # Payable
        self.right_frame_payment_info_frame_payable = tk.Label(right_frame_payment_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font))
        self.right_frame_payment_info_frame_payable.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)

        # total paid
        self.right_frame_payment_info_frame_total_paid = tk.Entry(right_frame_payment_info_frame)
        self.right_frame_payment_info_frame_total_paid.place(relx=0.42, rely=0.4, relwidth=0.4, relheight=0.08)
        self.right_frame_payment_info_frame_total_paid.bind('<Return>',self.update_change)

        # change/due
        self.right_frame_payment_info_frame_change = tk.Entry(right_frame_payment_info_frame)
        self.right_frame_payment_info_frame_change.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.08)

        
        # ================================ frame ======================================== #
        right_frame_payment_info_frame_frame_payment_acount = tk.Frame(right_frame_payment_info_frame,bg=color.color_list[7])

        def payment_method_select(event):
            right_frame_payment_info_frame_frame_payment_acount_lbl_11 = tk.Label(right_frame_payment_info_frame_frame_payment_acount, bg=color.color_list[7], anchor='w', font=('Times New Roman',purchase_font), text='Payment A/C :')
            if(self.payment_method_type.get()=='Cash'):
                right_frame_payment_info_frame_frame_payment_acount.place_forget()
                return
            
            right_frame_payment_info_frame_frame_payment_acount.place(relx=0,rely=0.6,relwidth=1,relheight=0.4)
            # payment account
            right_frame_payment_info_frame_frame_payment_acount_lbl_11.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.2)
            payment_acount_number = tk.StringVar()
            payment_acount_number_list = ['Name1', "Name2", "Name3",'Name4']
            payment_acount_number.set(payment_acount_number_list[0]) # default value
            payment_acount = tk.OptionMenu(right_frame_payment_info_frame_frame_payment_acount, payment_acount_number, *payment_acount_number_list,command=payment_method_select)
            payment_acount.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.2)
            default_payment_account = tk.IntVar()
            tk.Checkbutton(right_frame_payment_info_frame_frame_payment_acount, bg=color.color_list[7], font=('Times New Roman',purchase_font), text='Set aa default', variable=default_payment_account).place(relx=0.6,rely=0.7)


        
        # payment method
        right_frame_customer_info_frame_lbl_6 = tk.Label(right_frame_customer_info_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',10), text='Payment method :')
        right_frame_customer_info_frame_lbl_6.place(relx=0.01, rely=0.8, relwidth=0.4, relheight=0.08)
        self.payment_method_type = tk.StringVar()
        payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
        self.payment_method_type.set(payment_method_type_list[0]) # default value
        payment_method = tk.OptionMenu(right_frame_customer_info_frame, self.payment_method_type, *payment_method_type_list,command=payment_method_select)
        payment_method.place(relx=0.42, rely=0.8, relwidth=0.4, relheight=0.09)



        # ---------------------------- scroll table frame ----------------------------- #
        self.right_frame_frame_table = tk.Frame(right_frame)
        self.right_frame_frame_table.place(relx=0,rely=0.62,relwidth=1,relheight=0.4)

        
        # ================= bottom frame ======================= #
        bottom_frame = tk.Frame(self.root,bg='#e5c6b7')
        bottom_frame.place(relx=0,rely=0.922,relwidth=1,relheight=0.08)
        tk.Label(bottom_frame,text='Information').pack()
        # self.root.mainloop()
    
    
    def on_select(self,event):
        # Get the selected items
        selected_items = self.tree.selection()
        
        # Iterate through the selected items
        for item in selected_items:
            # Get the values of the selected item
            self.selected_intex_to_delete = self.tree.index(item)
        pass
    
    def show_table(self,items_to_sale):
        # scroll bar
        scrollbar = tk.Scrollbar(self.right_frame_frame_table)
        scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)

        # treeview
        self.tree = tk.ttk.Treeview(self.right_frame_frame_table, column=("c1", "c2", "c3","c4","c5"), show='headings', yscrollcommand=scrollbar.set)
        self.tree.heading("#0", text="SI")
        self.tree.heading("c1", text="Item Name")
        self.tree.heading("c2", text="Qty")
        self.tree.heading("c3", text="Unit Price")
        self.tree.heading("c4", text="Discount(%)")
        self.tree.heading("c5", text="Total Price")
        
        self.tree.column("#0",width=10,minwidth=10)
        self.tree.column("c1",width=50,minwidth=50)
        self.tree.column("c2",width=10,minwidth=10)
        self.tree.column("c3",width=20,minwidth=20)
        self.tree.column("c4",width=20,minwidth=20)
        self.tree.column("c5",width=20,minwidth=20)
        
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        for i in range(0,len(items_to_sale)):
            values_list = []
            print(items_to_sale[i])
            for j in range(0,len(items_to_sale[i])):
                if j==1 or j==4:
                    continue
                values_list.append(items_to_sale[i][j])
            # values_list = [items_to_sale[1][i][0],items_to_sale[1][i][3],items_to_sale[1][i][4]]
            self.tree.insert("",tk.END,text=(str)(i+1),values=values_list,tag = row_color[i%2])
        
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=1)
        scrollbar.config( command = self.tree.yview )
    def refresh(self):
        print('refresh home')
        init_page(self.root,'Item Sale')
        self.addHome()
    
# root = tk.Tk()
# root.title('Shopping Inventory Management System')
# root.geometry('1100x650+10+10')
# root.minsize(1100,650)
# addHome(root)
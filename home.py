import tkinter as tk
from PIL import ImageTk, Image
import datetime as dt 
import tkcalendar as tkcal
import datetime
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import DAO as dao

import item_sale as _item_sale
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


# object of classes

# root window




# def update_date_time(time_lbl,date_lbl):
#     cur_time = dt.datetime.now().strftime("%I:%M:%S %p")
#     cur_date = dt.date.today().strftime("%B %d, %Y")
#     time_lbl.config(text=cur_time)
#     date_lbl.config(text=cur_date)

def sale_item(root):
    print("go to sale item")
    _help.init_page(root,'Manage Item')
    item_sale_obj.itemSale()
def manage_item(root):
    # if root.session['role']>2:
    #     _help.init_page(root,'Manage Item')    
    print("go to manage item")
    _help.init_page(root,'Manage Item')
    item_manage_obj.item_manage()

def purchase_item(root):
    print('go to purchase item')
    _help.init_page(root,'Purchase Item')
    item_purchase_obj.itemPurchase()
    

def check_stock(root):
    print('go to check stock')
    _help.init_page(root,'Check Stock Item')
    check_stock_obj.checkStock()    

def check_demage_stock(root):
    print('go to demage check')
    _help.init_page(root,'Deamge Stock Item')
    demage_stock_obj.demageStock()

def purchase_report(root):
    print('go to purchase report')
    _help.init_page(root,'Purchase report')
    purchase_report_obj.purchaseReport()

def sales_report(root):
    print('go to sales report')
    _help.init_page(root,'Sales Report')
    sales_report_obj.salesReport()



def expenditure(root):
    print('go to expenditure')
    expenditure_manage_obj.expenditureManage()

def expenditure_report(root):
    print('go to expenditure report')
    _help.init_page(root,'Expenditure Report')
    expenditure_report_obj.expenditureReport()

def staff_manager(root):
    print('go to staff manager')
    staff_manager_obj.staffManager()

def contact_book(root):
	print('go to contact_book')



class Home:
 
    
    def __init__(self,root):
        try:
            self.root = root
            global item_manage_obj,item_purchase_obj,check_stock_obj,item_sale_obj
            global demage_stock_obj,purchase_report_obj,sales_report_obj
            global expenditure_manage_obj,expenditure_report_obj,staff_manager_obj
            item_manage_obj = _item_manage.Item_Manage(root)
            item_purchase_obj = _item_purchase.Item_Purchase(root)
            check_stock_obj = _check_stock.CheckStock(root)
            demage_stock_obj = _check_demage_stock.DemageStcok(root)
            purchase_report_obj = _purchase_report.PurchaseReport(root)
            sales_report_obj = _sales_report.SalesReport(root)
            expenditure_manage_obj = _expenditure_manage.ExpenditureManage(root)
            expenditure_report_obj = _expenditure_report.ExpenditureReport(root)
            staff_manager_obj = _staff_manager.StaffManager(root)
            item_sale_obj = _item_sale.ItemSale(root)
        except Exception as e:
            _help.show_message('warning',f'Occur exception while home object creating {e}')
        pass
    
    def barGraph(self):
        days = range(15)
        values1 = [random.randint(0, 100) for day in days]
        values2 = [random.randint(0, 100) for day in days]

        bar_width = 0.35
        opacity = 0.8

        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.3)
        ax.bar(days, values1, bar_width, alpha=opacity, color='#ff6347', label='Sale')
        ax.bar([day + bar_width for day in days], values2, bar_width, alpha=opacity, color='#1090a5', label='Purchase')

        ax.set_xlabel("Day")
        ax.set_ylabel("Taka(in thousand)")
        ax.set_title("Bar Graph for last 15days of sale and purchase")
        ax.legend()

        ax.set_xticks(days)
        ax.set_xticklabels([f"{ dt.datetime.now().strftime('%d/%m/%y')}" for day in days], rotation=45, fontsize=9, fontname='Arial')

        canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0,rely=0.4,relwidth=1,relheight=0.6)
        
    def box(self):
        top_frame = tk.Frame(self.right_frame,bg='#ffffff')
        top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.4)
        
        self.root.sale_icon = ImageTk.PhotoImage(Image.open("img/sale_icon.png").resize((50,50)))
        self.root.purchase_icon = ImageTk.PhotoImage(Image.open("img/purchase_icon.png").resize((30,30)))
        self.root.user_icon = ImageTk.PhotoImage(Image.open("img/user_icon.png").resize((30,30)))
        sale_frame = tk.Frame(top_frame,bg='#1090a5')
        sale_frame.place(relx=0.1,rely=0.3,relwidth=0.2,relheight=0.5)
        tk.Label(sale_frame,text='Total Sale\n$1000',bg='#1090a5', fg='#ffffff', font=('Helvic',14)
            ).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        tk.Label(sale_frame,bg='#1090a5',image=self.root.sale_icon).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        
        purchase_frame = tk.Frame(top_frame,bg='#ff6347')
        purchase_frame.place(relx=0.4,rely=0.3,relwidth=0.2,relheight=0.5)
        tk.Label(purchase_frame,text='Total Purchase\n$1000',bg='#ff6347', fg='#ffffff', font=('Helvic',14)
            ).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        tk.Label(purchase_frame,bg='#ff6347',image=self.root.purchase_icon).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        
        customer_frame = tk.Frame(top_frame,bg='#0d9355')
        customer_frame.place(relx=0.7,rely=0.3,relwidth=0.2,relheight=0.5)
        tk.Label(customer_frame,text='Number of Customer\n1200',bg='#0d9355', fg='#ffffff', font=('Helvic',14)
            ).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        tk.Label(customer_frame,bg='#0d9355',image=self.root.user_icon).pack(side=tk.TOP,fill='both',padx=5,pady=5)
        
    def rightFrame(self):
        self.barGraph()
        self.box()
        
    def leftFrame(self):
        # ---------------------------operation button--------------------------- #
        operation_name = ['Sale Item','Manage Item','Purchase Item','Check Stock','Demage Stock','Purchase Report',
                          'Sales Report','Expenditure','Expenditure Report','Staff Manager','Contact Book','Refresh']
        self.operation_btn_frm = [tk.Frame(self.left_frame, bg=color.getColor('bd_button'), bd=0) for i in range(len(operation_name))]
        self.operation_btn = [tk.Button() for i in range(len(operation_name))]
        
        for i,frm in enumerate(self.operation_btn_frm):
            frm.pack(side=tk.TOP,fill=tk.X,padx=10, pady=5)
            self.operation_btn[i] = tk.Button(frm,text=operation_name[i], fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), bd=0)
            self.operation_btn[i].pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
            _help.button_hover(frm,self.operation_btn[i])
            
        self.operation_btn[0].config(command=lambda:sale_item(self.root))
        self.operation_btn[1].config(command=lambda:manage_item(self.root))
        self.operation_btn[2].config(command=lambda:purchase_item(self.root))
        self.operation_btn[3].config(command=lambda:check_stock(self.root))
        self.operation_btn[4].config(command=lambda:check_demage_stock(self.root))
        self.operation_btn[5].config(command=lambda:purchase_report(self.root))
        self.operation_btn[6].config(command=lambda:sales_report(self.root))
        self.operation_btn[7].config(command=lambda:expenditure(self.root))
        self.operation_btn[8].config(command=lambda:expenditure_report(self.root))
        self.operation_btn[9].config(command=lambda:staff_manager(self.root))
        self.operation_btn[10].config(command=lambda:contact_book(self.root))
        self.operation_btn[11].config(command=self.refresh)

    
        
    def addHome(self):
        _help.init_page(self.root,'Item Sale')
        
        self.main_frame = tk.Frame(self.root,bg='#ffffff')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        
        # ============================ left frame 0 ============================
        self.left_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.left_frame.place(relx=0.005,rely=0, relwidth=0.15, relheight=1)
        self.leftFrame()
        
        self.right_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.right_frame.place(relx=0.16,rely=0,relwidth=0.835, relheight=1)
        self.rightFrame()
        


    def refresh(self):
        print('refresh home')
        _help.init_page(self.root,'Item Sale')
        self.addHome()

    
# root = tk.Tk()
# root.title('Shopping Inventory Management System')
# root.geometry('1100x650+10+10')
# root.minsize(1100,650)
# addHome(root)
import tkinter as tk
from PIL import ImageTk, Image
import datetime as dt 
import tkcalendar as tkcal
# root window
# root = tk.Tk()
# root.title('Shopping Inventory Management System')
# root.geometry('1100x650+10+10')

def addHome(root):
    # color code 
    top0_bg = '#297592'
    top0_fg = '#ffffff'
    top1_bg = '#3bbd75'
    top1_fg = '#000000'
    left0_bg = '#13dbcc'
    left_0_bg_1 = '#b1b13d'
    left0_fg = '#000000'
    left1_bg = '#e1e1e1'
    left1_fg = '#000000'
    left2_bg = '#e1e1e1'
    left2_fg = '#000000'



    # ============================ top frame 0 ============================
    top_frame_0 = tk.Frame(root,bg=top0_bg)
    top_frame_0.place(x=0,y=0,relwidth=1,height=80)
    # ---------------------------------------------------------------------
    # logo  (at frame 0)
    root.shop_logo = ImageTk.PhotoImage(Image.open("img/logo.png").resize((50,50)))
    top0_frame_0_lbl_0 = tk.Label(top_frame_0, image = root.shop_logo)
    top0_frame_0_lbl_0.pack(side=tk.LEFT,padx=15)

    # shop name (at frame 0)
    top0_frame_0_lbl_1 = tk.Label(top_frame_0,text="abc Fashion House" , fg=top0_fg, bg=top0_bg, font=("Comic Sans MS", 20, "bold"))
    top0_frame_0_lbl_1.pack(side=tk.LEFT,padx=15)

    # shop owner's info (at frame 0)
    top0_frame_0_lbl_2 = tk.Label(top_frame_0,text="Mobile: +8801xxxxxxxxx\nEmail: abc@xxxxx.com" , fg=top0_fg, bg=top0_bg, font=("Times New Roman", 12))
    top0_frame_0_lbl_2.pack(side=tk.LEFT,padx=250)




    # ============================ top frame 1 ============================
    top_frame_1 = tk.Frame(root,bg=top1_bg)
    top_frame_1.place(x=0,y=80,relwidth=1,height=30)
    # ---------------------------------------------------------------------
    # welcome  (at frame 1)
    top_frame_1_lbl_0 = tk.Label(top_frame_1,text="Welcome to abc Fasion House" , fg=top1_fg, bg=top1_bg, font=("Comic Sans MS",12))
    top_frame_1_lbl_0.pack(side=tk.LEFT,padx=50)

    # date (at frame 1)
    cur_date = dt.date.today().strftime("%B %d, %Y")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_date , fg=top1_fg, bg=top1_bg, font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # time (at frame 1)
    cur_time = dt.datetime.now().strftime("%I:%M %p")
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text=cur_time , fg=top1_fg, bg=top1_bg, font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)

    # tittle (at frame 1)
    top_frame_1_lbl_1 = tk.Label(top_frame_1,text="Home" , fg=top1_fg, bg=top1_bg, font=("Comic Sans MS",12))
    top_frame_1_lbl_1.pack(side=tk.LEFT,padx=50)




    # ============================ left frame 0 ============================
    left_frame_0 = tk.Frame(root,bg=left0_bg)
    left_frame_0.place(relx=0.005,rely=0.172, relwidth=0.15, relheight=0.75)

    # ---------------------------------------------------------------------- #
    operation_list = ['Add\Manage Item', 'Purchase Item', 'Check Stock', 'Demage Stock',
                    'Purchase Report', 'Sales Report', 'Item Sales Report', 'Expenditure',
                    'Expenditure Report', 'Staff Manager', 'Contact Book', 'Refresh']
    for op in range(0,len(operation_list)-1):
        left_frame_0_btn_0 = tk.Button(left_frame_0,text=operation_list[op], fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
        left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Refresh (at left_frame0) 
    left_frame_0_btn_11 = tk.Button(left_frame_0,text="Refresh", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_11.pack(side=tk.TOP,fill=tk.X,padx=5, pady=15)


    # ============================ left frame 1 ============================
    left_frame_1 = tk.Frame(root,bg=left1_bg)
    left_frame_1.place(relx=0.16,rely=0.172, relwidth=0.28, relheight=0.75)

    # ----------------------------------------------------------------------#
    purchase_date = tkcal.DateEntry(left_frame_1,selecmode='day', cursor='hand1')
    purchase_date.place(relx=0.55,y=5,relwidth=0.4)

    item_info_list = ['Item Name :', 'Item Name :', 'Item Code :', 'Item Code :',
                    'Item Group :', 'Company :', 'Shelf No. :', 'Available Quantity :',
                    'Sale Price Rate :', 'Sale Quantity :', 'Price :', 'Discount :',
                    'Item Total Price :']


    for itm in range(0,len(item_info_list)):
        left_frame_1_lbl_0 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text=item_info_list[itm])
        left_frame_1_lbl_0.place(x=5,y=(itm+1)*30,relwidth=0.5)    


    # delete item
    left_frame_btn_delete = tk.Button(left_frame_1, fg=top1_fg, bg=top1_bg,font=('Times New Roman',14), text='Delete')
    left_frame_btn_delete.place(relx=0.02,rely=0.92, height=25)

    check_free = tk.IntVar()
    tk.Checkbutton(left_frame_1, bg=top1_bg, font=('Times New Roman',14), text='Free', variable=check_free).place(relx=0.37,rely=0.92,height=25)
    # add item to sell
    left_frame_btn_add = tk.Button(left_frame_1, fg=top1_fg, bg=top1_bg,font=('Times New Roman',14), text='Add item')
    left_frame_btn_add.place(relx=0.7,rely=0.92, height=25)



    # --------------------------------product input box------------------------------- #

    item_name = tk.Entry(left_frame_1)
    item_name.place(relx=0.5, y=33, relwidth=0.48, relheight=0.04)

    item_code = tk.Entry(left_frame_1)
    item_code.place(relx=0.5, y=63, relwidth=0.48, relheight=0.04)

    sale_price_rate = tk.Entry(left_frame_1)
    sale_price_rate.place(relx=0.5, y=273, relwidth=0.48, relheight=0.04)

    sale_quantity = tk.Entry(left_frame_1)
    sale_quantity.place(relx=0.5, y=303, relwidth=0.48, relheight=0.04)

    discount = tk.Entry(left_frame_1)
    discount.place(relx=0.5, y=363, relwidth=0.48, relheight=0.04)

    # --------------------------------product info box------------------------------- #

    # Item Name (at left_frame1)
    left_frame_1_lbl_item_name = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Name :')
    left_frame_1_lbl_item_name.place(relx=0.5, y=90, relwidth=0.48, relheight=0.04)

    # Item Code (at left_frame1)
    left_frame_1_lbl_item_code = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Code :')
    left_frame_1_lbl_item_code.place(relx=0.5, y=120, relwidth=0.48, relheight=0.04)

    # Item Group (at left_frame1)
    left_frame_1_lbl_item_group = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Group :')
    left_frame_1_lbl_item_group.place(relx=0.5, y=150, relwidth=0.48, relheight=0.04)

    # Company (at left_frame1)
    left_frame_1_lbl_company = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Company :')
    left_frame_1_lbl_company.place(relx=0.5, y=180, relwidth=0.48, relheight=0.04)

    # Shelf No. (at left_frame1)
    left_frame_1_lbl_shelf_no = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Shelf No. :')
    left_frame_1_lbl_shelf_no.place(relx=0.5, y=210, relwidth=0.48, relheight=0.04)

    # Available Quantity (at left_frame1)
    left_frame_1_lbl_avl_quantity = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Available Quantity :')
    left_frame_1_lbl_avl_quantity.place(relx=0.5, y=240, relwidth=0.48, relheight=0.04)

    # Price
    left_frame_1_lbl_price = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Price :')
    left_frame_1_lbl_price.place(relx=0.5, y=330, relwidth=0.48, relheight=0.04)

    # Item Total Price (at left_frame1)
    left_frame_1_lbl_total_price = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Total Price :')
    left_frame_1_lbl_total_price.place(relx=0.5, y=390, relwidth=0.48, relheight=0.04)



    # ============================ left frame 2 ============================ #
    left_frame_2 = tk.Frame(root,bg=left2_bg)
    left_frame_2.place(relx=0.45,rely=0.172,relwidth=0.545,relheight=0.75)

    purchase_font = 12
    # ---------------------------- customer info frame ----------------------------- #
    left_frame_2_frame_customer_info = tk.Frame(left_frame_2,bg=left2_bg)
    left_frame_2_frame_customer_info.place(relx=0.01,rely=0.01,relwidth=0.48,relheight=0.6)

    # ---------------------------- label --------------------------#
    # search type
    left_frame_2_frame_customer_info_lbl_0 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Search by :')
    left_frame_2_frame_customer_info_lbl_0.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.08)

    # search box
    left_frame_2_frame_customer_info_lbl_1 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Query :')
    left_frame_2_frame_customer_info_lbl_1.place(relx=0.01, rely=0.1, relwidth=0.4, relheight=0.08)

    # search button
    left_frame_2_frame_customer_info_btn_search = tk.Button(left_frame_2_frame_customer_info,fg=top1_fg, bg=top1_bg, font=('Times New Roman',12), text='Search')
    left_frame_2_frame_customer_info_btn_search.place(relx=0.25, rely=0.2, relwidth=0.4, relheight=0.08)

    # customer name 
    left_frame_2_frame_customer_info_lbl_2 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Name :')
    left_frame_2_frame_customer_info_lbl_2.place(relx=0.01, rely=0.3, relwidth=0.4, relheight=0.08)

    # customer pre-balance
    left_frame_2_frame_customer_info_lbl_3 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Pre-balance :')
    left_frame_2_frame_customer_info_lbl_3.place(relx=0.01, rely=0.4, relwidth=0.4, relheight=0.08)

    # customer current balance
    left_frame_2_frame_customer_info_lbl_4 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Current-balance :')
    left_frame_2_frame_customer_info_lbl_4.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.08)

    # customer contact no
    left_frame_2_frame_customer_info_lbl_5 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Contact :')
    left_frame_2_frame_customer_info_lbl_5.place(relx=0.01, rely=0.6, relwidth=0.4, relheight=0.08)

    # ---------------------------- Input ------------------------------ #
    product_search_type = tk.StringVar()
    search_type_list = ['name', "code", "company",'group']
    product_search_type.set(search_type_list[0]) # default value
    search_type = tk.OptionMenu(left_frame_2_frame_customer_info, product_search_type, *search_type_list)
    search_type.place(relx=0.3, rely=0.01, relwidth=0.6, relheight=0.09)

    query = tk.Entry(left_frame_2_frame_customer_info)
    query.place(relx=0.3, rely=0.11, relwidth=0.6, relheight=0.08)

    customer_name = tk.Entry(left_frame_2_frame_customer_info)
    customer_name.place(relx=0.42, rely=0.3, relwidth=0.48, relheight=0.08)

    pre_balance = tk.Entry(left_frame_2_frame_customer_info)
    pre_balance.place(relx=0.42, rely=0.4, relwidth=0.48, relheight=0.08)

    current_balance = tk.Entry(left_frame_2_frame_customer_info)
    current_balance.place(relx=0.42, rely=0.5, relwidth=0.48, relheight=0.08)

    contact_no = tk.Entry(left_frame_2_frame_customer_info)
    contact_no.place(relx=0.42, rely=0.6, relwidth=0.48, relheight=0.08)


    # ---------------------------- payment info frame ----------------------------- #
    left_frame_2_frame_payment_info = tk.Frame(left_frame_2,bg=left2_bg)
    left_frame_2_frame_payment_info.place(relx=0.5,rely=0.01,relwidth=0.49,relheight=0.6)

    purchase_info_list = ['Total Item :', 'Total Price :', 'Discount :',
                        'Payable :', 'Total Paid :', 'Change/Due :']
    for i in range(0,len(purchase_info_list)):
        left_frame_2_frame_payment_info_lbl = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text=purchase_info_list[i])
        left_frame_2_frame_payment_info_lbl.place(relx=0.01, rely=0.01+0.1*i, relwidth=0.4, relheight=0.08)     



    # total item 
    left_frame_2_frame_payment_info_lbl_1 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    left_frame_2_frame_payment_info_lbl_1.place(relx=0.42, rely=0.01, relwidth=0.4, relheight=0.08)

    # total price
    left_frame_2_frame_payment_info_lbl_2 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Total price :')
    left_frame_2_frame_payment_info_lbl_2.place(relx=0.42, rely=0.1, relwidth=0.4, relheight=0.08)

    # discount 
    left_frame_2_frame_payment_info_lbl_5 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    left_frame_2_frame_payment_info_lbl_5.place(relx=0.42, rely=0.2, relwidth=0.4, relheight=0.08)

    # Payable
    left_frame_2_frame_payment_info_lbl_7 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    left_frame_2_frame_payment_info_lbl_7.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)

    # total paid
    left_frame_2_frame_payment_info_total_paid = tk.Entry(left_frame_2_frame_payment_info)
    left_frame_2_frame_payment_info_total_paid.place(relx=0.42, rely=0.4, relwidth=0.4, relheight=0.08)

    # change/due
    left_frame_2_frame_payment_info_lbl_10 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    left_frame_2_frame_payment_info_lbl_10.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.08)

    # =================== frame ====================== #
    left_frame_2_frame_payment_info_frame_payment_acount = tk.Frame(left_frame_2_frame_payment_info,bg=left2_bg)

    def payment_method_select(event):
        left_frame_2_frame_payment_info_frame_payment_acount_lbl_11 = tk.Label(left_frame_2_frame_payment_info_frame_payment_acount, bg=left2_bg, anchor='w', font=('Times New Roman',purchase_font), text='Payment A/C :')
        if(payment_method_type.get()=='Cash'):
            left_frame_2_frame_payment_info_frame_payment_acount.place_forget()
            return
        
        left_frame_2_frame_payment_info_frame_payment_acount.place(relx=0,rely=0.6,relwidth=1,relheight=0.4)
        # payment account
        left_frame_2_frame_payment_info_frame_payment_acount_lbl_11.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.2)
        payment_acount_number = tk.StringVar()
        payment_acount_number_list = ['Name1', "Name2", "Name3",'Name4']
        payment_acount_number.set(payment_acount_number_list[0]) # default value
        payment_acount = tk.OptionMenu(left_frame_2_frame_payment_info_frame_payment_acount, payment_acount_number, *payment_acount_number_list,command=payment_method_select)
        payment_acount.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.2)
        default_payment_account = tk.IntVar()
        tk.Checkbutton(left_frame_2_frame_payment_info_frame_payment_acount, bg=left2_bg, font=('Times New Roman',purchase_font), text='Set aa default', variable=default_payment_account).place(relx=0.6,rely=0.7)


    
    # payment method
    left_frame_2_frame_customer_info_lbl_6 = tk.Label(left_frame_2_frame_customer_info,bg=left2_bg, anchor='w', font=('Times New Roman',10), text='Payment method :')
    left_frame_2_frame_customer_info_lbl_6.place(relx=0.01, rely=0.8, relwidth=0.4, relheight=0.08)
    payment_method_type = tk.StringVar()
    payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
    payment_method_type.set(payment_method_type_list[0]) # default value
    payment_method = tk.OptionMenu(left_frame_2_frame_customer_info, payment_method_type, *payment_method_type_list,command=payment_method_select)
    payment_method.place(relx=0.42, rely=0.8, relwidth=0.4, relheight=0.09)





    # ---------------------------- scroll table frame ----------------------------- #
    left_frame_2_frame_table = tk.Frame(left_frame_2)
    left_frame_2_frame_table.place(relx=0,rely=0.62,relwidth=1,relheight=0.4)

    # scroll bar
    scrollbar = tk.Scrollbar(left_frame_2_frame_table)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)

    # treeview
    tree = tk.ttk.Treeview(left_frame_2_frame_table, column=("c1", "c2", "c3"), show='headings', yscrollcommand=scrollbar.set)
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


    
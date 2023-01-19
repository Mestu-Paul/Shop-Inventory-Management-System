import tkinter as tk
import tkcalendar as tkcal

from color_code import *

def back_home(main_frame):
    print("back home")
    main_frame.place_forget()
    

def item_purchase(root):
    # item manage main frame
    main_frame = tk.Frame(root,bg='white')
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

    # ============================ left frame 1 ============================
    left_frame = tk.Frame(main_frame,bg=color7)
    left_frame.place(relx=0.01,rely=0, relwidth=0.28, relheight=1)

    # ----------------------------------------------------------------------#
    purchase_date = tkcal.DateEntry(left_frame,selecmode='day', cursor='hand1')
    purchase_date.place(relx=0.55,y=5,relwidth=0.4)

    item_info_list = ['Item Name :', 'Item Code :', 'Item Name :', 'Item Code :',
                    'Item Group :', 'Company :', 'Shelf No. :', 'Available Quantity :',
                    'Sale Price Rate :', 'Sale Quantity :', 'Price :', 'Discount :',
                    'Item Total Price :']


    for itm in range(0,len(item_info_list)):
        left_frame_lbl_0 = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text=item_info_list[itm])
        left_frame_lbl_0.place(x=5,y=(itm+1)*30,relwidth=0.5)    


    # delete item
    left_frame_btn_delete = tk.Button(left_frame, fg=color4, bg=color3,font=('Times New Roman',14), text='Delete')
    left_frame_btn_delete.place(relx=0.02,rely=0.92, height=25)

    check_free = tk.IntVar()
    tk.Checkbutton(left_frame, bg=color3, font=('Times New Roman',14), text='Free', variable=check_free).place(relx=0.37,rely=0.92,height=25)
    # add item to sell
    left_frame_btn_add = tk.Button(left_frame, fg=color4, bg=color3,font=('Times New Roman',14), text='Add item')
    left_frame_btn_add.place(relx=0.7,rely=0.92, height=25)



    # --------------------------------product input box------------------------------- #

    item_name = tk.Entry(left_frame)
    item_name.place(relx=0.5, y=33, relwidth=0.48, relheight=0.04)

    item_code = tk.Entry(left_frame)
    item_code.place(relx=0.5, y=63, relwidth=0.48, relheight=0.04)

    sale_price_rate = tk.Entry(left_frame)
    sale_price_rate.place(relx=0.5, y=273, relwidth=0.48, relheight=0.04)

    sale_quantity = tk.Entry(left_frame)
    sale_quantity.place(relx=0.5, y=303, relwidth=0.48, relheight=0.04)

    discount = tk.Entry(left_frame)
    discount.place(relx=0.5, y=363, relwidth=0.48, relheight=0.04)

    # --------------------------------product info box------------------------------- #

    # Item Name (at left_frame1)
    left_frame_lbl_item_name = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Item Name :')
    left_frame_lbl_item_name.place(relx=0.5, y=90, relwidth=0.48, relheight=0.04)

    # Item Code (at left_frame1)
    left_frame_lbl_item_code = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Item Code :')
    left_frame_lbl_item_code.place(relx=0.5, y=120, relwidth=0.48, relheight=0.04)

    # Item Group (at left_frame1)
    left_frame_lbl_item_group = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Item Group :')
    left_frame_lbl_item_group.place(relx=0.5, y=150, relwidth=0.48, relheight=0.04)

    # Company (at left_frame1)
    left_frame_lbl_company = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Company :')
    left_frame_lbl_company.place(relx=0.5, y=180, relwidth=0.48, relheight=0.04)

    # Shelf No. (at left_frame1)
    left_frame_lbl_shelf_no = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Shelf No. :')
    left_frame_lbl_shelf_no.place(relx=0.5, y=210, relwidth=0.48, relheight=0.04)

    # Available Quantity (at left_frame1)
    left_frame_lbl_avl_quantity = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Available Quantity :')
    left_frame_lbl_avl_quantity.place(relx=0.5, y=240, relwidth=0.48, relheight=0.04)

    # Price
    left_frame_lbl_price = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Price :')
    left_frame_lbl_price.place(relx=0.5, y=330, relwidth=0.48, relheight=0.04)

    # Item Total Price (at left_frame1)
    left_frame_lbl_total_price = tk.Label(left_frame,bg=color7, anchor='w', font=('Times New Roman',14), text='Item Total Price :')
    left_frame_lbl_total_price.place(relx=0.5, y=390, relwidth=0.48, relheight=0.04)



    # ============================ left frame 2 ============================ #
    right_frame = tk.Frame(main_frame,bg=color7)
    right_frame.place(relx=0.3,rely=0,relwidth=0.69,relheight=1)

    purchase_font = 12
    # ---------------------------- customer info frame ----------------------------- #
    right_frame_customer_info_frame = tk.Frame(right_frame,bg=color7)
    right_frame_customer_info_frame.place(relx=0.01,rely=0.01,relwidth=0.48,relheight=0.6)

    # ---------------------------- label --------------------------#
    # search type
    right_frame_customer_info_frame_lbl_0 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Search by :')
    right_frame_customer_info_frame_lbl_0.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.08)

    # search box
    right_frame_customer_info_frame_lbl_1 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Query :')
    right_frame_customer_info_frame_lbl_1.place(relx=0.01, rely=0.1, relwidth=0.4, relheight=0.08)

    # search button
    right_frame_customer_info_frame_btn_search = tk.Button(right_frame_customer_info_frame,fg=color4, bg=color3, font=('Times New Roman',12), text='Search')
    right_frame_customer_info_frame_btn_search.place(relx=0.25, rely=0.2, relwidth=0.4, relheight=0.08)

    # customer name 
    right_frame_customer_info_frame_lbl_2 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Name :')
    right_frame_customer_info_frame_lbl_2.place(relx=0.01, rely=0.3, relwidth=0.4, relheight=0.08)

    # customer pre-balance
    right_frame_customer_info_frame_lbl_3 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Pre-balance :')
    right_frame_customer_info_frame_lbl_3.place(relx=0.01, rely=0.4, relwidth=0.4, relheight=0.08)

    # customer current balance
    right_frame_customer_info_frame_lbl_4 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Current-balance :')
    right_frame_customer_info_frame_lbl_4.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.08)

    # customer contact no
    right_frame_customer_info_frame_lbl_5 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Contact :')
    right_frame_customer_info_frame_lbl_5.place(relx=0.01, rely=0.6, relwidth=0.4, relheight=0.08)

    payment_button = tk.Button(right_frame_customer_info_frame,text='Payment', bg=color3)
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
    right_frame_frame_payment_info = tk.Frame(right_frame,bg=color7)
    right_frame_frame_payment_info.place(relx=0.5,rely=0.01,relwidth=0.49,relheight=0.6)

    purchase_info_list = ['Total Item :', 'Total Price :', 'Discount :',
                        'Payable :', 'Total Paid :', 'Change/Due :']
    for i in range(0,len(purchase_info_list)):
        right_frame_frame_payment_info_lbl = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text=purchase_info_list[i])
        right_frame_frame_payment_info_lbl.place(relx=0.01, rely=0.01+0.1*i, relwidth=0.4, relheight=0.08)     



    # total item 
    right_frame_frame_payment_info_lbl_1 = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    right_frame_frame_payment_info_lbl_1.place(relx=0.42, rely=0.01, relwidth=0.4, relheight=0.08)

    # total price
    right_frame_frame_payment_info_lbl_2 = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Total price :')
    right_frame_frame_payment_info_lbl_2.place(relx=0.42, rely=0.1, relwidth=0.4, relheight=0.08)

    # discount 
    right_frame_frame_payment_info_lbl_5 = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    right_frame_frame_payment_info_lbl_5.place(relx=0.42, rely=0.2, relwidth=0.4, relheight=0.08)

    # Payable
    right_frame_frame_payment_info_lbl_7 = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    right_frame_frame_payment_info_lbl_7.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)

    # total paid
    right_frame_frame_payment_info_total_paid = tk.Entry(right_frame_frame_payment_info)
    right_frame_frame_payment_info_total_paid.place(relx=0.42, rely=0.4, relwidth=0.4, relheight=0.08)

    # change/due
    right_frame_frame_payment_info_lbl_10 = tk.Label(right_frame_frame_payment_info,bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Total item :')
    right_frame_frame_payment_info_lbl_10.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.08)

    # =================== frame ====================== #
    right_frame_frame_payment_info_frame_payment_acount = tk.Frame(right_frame_frame_payment_info,bg=color7)

    def payment_method_select(event):
        right_frame_frame_payment_info_frame_payment_acount_lbl_11 = tk.Label(right_frame_frame_payment_info_frame_payment_acount, bg=color7, anchor='w', font=('Times New Roman',purchase_font), text='Payment A/C :')
        if(payment_method_type.get()=='Cash'):
            right_frame_frame_payment_info_frame_payment_acount.place_forget()
            return
        
        right_frame_frame_payment_info_frame_payment_acount.place(relx=0,rely=0.6,relwidth=1,relheight=0.4)
        # payment account
        right_frame_frame_payment_info_frame_payment_acount_lbl_11.place(relx=0.01, rely=0.5, relwidth=0.4, relheight=0.2)
        payment_acount_number = tk.StringVar()
        payment_acount_number_list = ['Name1', "Name2", "Name3",'Name4']
        payment_acount_number.set(payment_acount_number_list[0]) # default value
        payment_acount = tk.OptionMenu(right_frame_frame_payment_info_frame_payment_acount, payment_acount_number, *payment_acount_number_list,command=payment_method_select)
        payment_acount.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.2)
        default_payment_account = tk.IntVar()
        tk.Checkbutton(right_frame_frame_payment_info_frame_payment_acount, bg=color7, font=('Times New Roman',purchase_font), text='Set aa default', variable=default_payment_account).place(relx=0.6,rely=0.7)



    # payment method
    right_frame_customer_info_frame_lbl_6 = tk.Label(right_frame_customer_info_frame,bg=color7, anchor='w', font=('Times New Roman',10), text='Payment method :')
    right_frame_customer_info_frame_lbl_6.place(relx=0.01, rely=0.8, relwidth=0.4, relheight=0.08)
    payment_method_type = tk.StringVar()
    payment_method_type_list = ['Cash', "Bkash", "Nagad",'Card']
    payment_method_type.set(payment_method_type_list[0]) # default value
    payment_method = tk.OptionMenu(right_frame_customer_info_frame, payment_method_type, *payment_method_type_list,command=payment_method_select)
    payment_method.place(relx=0.42, rely=0.8, relwidth=0.4, relheight=0.09)



    # ---------------------------- scroll table frame ----------------------------- #
    right_frame_frame_table = tk.Frame(right_frame)
    right_frame_frame_table.place(relx=0,rely=0.62,relwidth=1,relheight=0.4)

    # scroll bar
    scrollbar = tk.Scrollbar(right_frame_frame_table)
    scrollbar.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)

    # treeview
    tree = tk.ttk.Treeview(right_frame_frame_table, column=("c1", "c2", "c3"), show='headings', yscrollcommand=scrollbar.set)
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

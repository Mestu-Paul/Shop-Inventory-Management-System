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


    # ============================ top frame 0 ============================
    top_frame_0 = tk.Frame(root,bg=top0_bg)
    top_frame_0.place(x=0,y=0,relwidth=1,height=80)
    # ---------------------------------------------------------------------
    # logo  (at frame 0)
    shop_logo = ImageTk.PhotoImage(Image.open("img/logo.png").resize((50,50)))
    top0_frame_0_lbl_0 = tk.Label(top_frame_0, image = shop_logo)
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
    left_frame_0.place(x=3,y=112, relwidth=0.15, relheight=0.75)

    # ----------------------------------------------------------------------
    # Add\Manage Item (at left_frame0) 
    left_frame_0_btn_0 = tk.Button(left_frame_0,text="Add\Manage Item", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Purchase Item (at left_frame0) 
    left_frame_0_btn_1 = tk.Button(left_frame_0,text="Purchase Item", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_1.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Check Stock (at left_frame0) 
    left_frame_0_btn_2 = tk.Button(left_frame_0,text="Check Stock", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_2.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Demage Stock (at left_frame0) 
    left_frame_0_btn_3 = tk.Button(left_frame_0,text="Demage Stock", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_3.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Purchase Report (at left_frame0) 
    left_frame_0_btn_4 = tk.Button(left_frame_0,text="Purchase Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_4.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Sales Report (at left_frame0) 
    left_frame_0_btn_5 = tk.Button(left_frame_0,text="Sales Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_5.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Item Sales Report (at left_frame0) 
    left_frame_0_btn_6 = tk.Button(left_frame_0,text="Item Sales Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_6.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Expenditure (at left_frame0) 
    left_frame_0_btn_7 = tk.Button(left_frame_0,text="Expenditure", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_7.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Expenditure Report (at left_frame0) 
    left_frame_0_btn_8 = tk.Button(left_frame_0,text="Expenditure Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_8.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Staff Manager (at left_frame0) 
    left_frame_0_btn_9 = tk.Button(left_frame_0,text="Staff Manager", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_9.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Contact Book (at left_frame0) 
    left_frame_0_btn_10 = tk.Button(left_frame_0,text="Contact Book", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_10.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

    # Refresh (at left_frame0) 
    left_frame_0_btn_11 = tk.Button(left_frame_0,text="Refresh", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
    left_frame_0_btn_11.pack(side=tk.TOP,fill=tk.X,padx=5, pady=15)
    
    # ============================ left frame 1 ============================
    left_frame_1 = tk.Frame(root,bg=left1_bg)
    left_frame_1.place(relx=0.16,y=112, relwidth=0.28, relheight=0.75)

    # ----------------------------------------------------------------------#
    purchase_date = tkcal.DateEntry(left_frame_1,selecmode='day', cursor='hand1')
    purchase_date.place(relx=0.55,y=5,relwidth=0.4)

    # Item Name (at left_frame1)
    left_frame_1_lbl_0 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Name :')
    left_frame_1_lbl_0.place(x=5,y=30,relwidth=0.5)

    # Item Code (at left_frame1)
    left_frame_1_lbl_1 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Code :')
    left_frame_1_lbl_1.place(x=5,y=60,relwidth=0.5)

    # Item Name (at left_frame1)
    left_frame_1_lbl_2 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Name :')
    left_frame_1_lbl_2.place(x=5,y=90,relwidth=0.5)

    # Item Code (at left_frame1)
    left_frame_1_lbl_3 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Code :')
    left_frame_1_lbl_3.place(x=5,y=120,relwidth=0.5)

    # Item Group (at left_frame1)
    left_frame_1_lbl_4 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Group :')
    left_frame_1_lbl_4.place(x=5,y=150,relwidth=0.5)

    # Company (at left_frame1)
    left_frame_1_lbl_5 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Company :')
    left_frame_1_lbl_5.place(x=5,y=180,relwidth=0.5)

    # Shelf No. (at left_frame1)
    left_frame_1_lbl_6 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Shelf No. :')
    left_frame_1_lbl_6.place(x=5,y=210,relwidth=0.5)

    # Available Quantity (at left_frame1)
    left_frame_1_lbl_7 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Available Quantity :')
    left_frame_1_lbl_7.place(x=5,y=240,relwidth=0.5)

    # Sale Price Rate (at left_frame1)
    left_frame_1_lbl_8 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Sale Price Rate :')
    left_frame_1_lbl_8.place(x=5,y=270,relwidth=0.5)

    # Sale Quantity (at left_frame1)
    left_frame_1_lbl_9 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Sale Quantity :')
    left_frame_1_lbl_9.place(x=5,y=300,relwidth=0.5)

    # Price
    left_frame_1_lbl_10 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Price :')
    left_frame_1_lbl_10.place(x=5,y=330,relwidth=0.5)

    # Discount (at left_frame1)
    left_frame_1_lbl_11 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Discount :')
    left_frame_1_lbl_11.place(x=5,y=360,relwidth=0.5)

    # Item Total Price (at left_frame1)
    left_frame_1_lbl_12 = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='Item Total Price :')
    left_frame_1_lbl_12.place(x=5,y=390,relwidth=0.5)

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

    
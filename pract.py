import tkinter as tk
from PIL import ImageTk, Image
# from datetime import date
import datetime as dt 

# root window
root = tk.Tk()
root.title('Shopping Inventory Management System')
root.geometry('1100x650+10+10')

# color code 
top0_bg = '#297592'
top0_fg = '#ffffff'
top1_bg = '#3bbd75'
top1_fg = '#000000'
left0_bg = '#13dbcc'
left_0_bg_1 = '#b1b13d'
left0_fg = '#000000'
left1_bg = '#ffffff'


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
left_frame_0.place(x=3,y=112, relwidth=0.15, relheight=0.8)

# ----------------------------------------------------------------------
# Add\Manage Item (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Add\Manage Item", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Purchase Item (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Purchase Item", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Check Stock (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Check Stock", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Demage Stock (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Demage Stock", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Purchase Report (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Purchase Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Sales Report (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Sales Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Item Sales Report (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Item Sales Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Expenditure (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Expenditure", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Expenditure Report (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Expenditure Report", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Staff Manager (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Staff Manager", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Contact Book (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Contact Book", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)

# Refresh (at left_frame0) 
left_frame_0_btn_0 = tk.Button(left_frame_0,text="Refresh", fg=left0_fg, bg=left_0_bg_1, font=('Times New Roman1',10))
left_frame_0_btn_0.pack(side=tk.TOP,fill=tk.X,padx=5, pady=15)


# ============================ left frame 1 ============================
left_frame_1 = tk.Frame(root,)
root.mainloop()
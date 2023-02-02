import tkinter as tk

import color_code as color


def backHome(main_frame):
    print("back home")
    main_frame.place_forget()
def add_new_staff(main_frame):
    print('add new')
def manage_staff(main_frame):
    print('manage')
def staff_payment(main_frame):
    print('payment')
def payment_report(main_frame):
    print('report')
def staff_manager(root):
    main_frame = tk.Frame(root,bg=color.color_list[1])
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
    menu_bar_frame = tk.Frame(main_frame)
    menu_bar_frame.place(relx=0,rely=0,relwidth=1,height=25)
    tk.Button(menu_bar_frame,text='Add new staff',font=('Times New Roman',12,'bold'),command=lambda:add_new_staff(main_frame)).place(relx=0,rely=0,relwidth=0.12,height=25)
    tk.Button(menu_bar_frame,text='Manage staff',font=('Times New Roman',12,'bold'),command=lambda:manage_staff(main_frame)).place(relx=.12,rely=0,relwidth=0.12,height=25)
    tk.Button(menu_bar_frame,text='Staff payment',font=('Times New Roman',12,'bold'),command=lambda:staff_payment(main_frame)).place(relx=.24,rely=0,relwidth=0.12,height=25)
    tk.Button(menu_bar_frame,text='Payment report',font=('Times New Roman',12,'bold'),command=lambda:payment_report(main_frame)).place(relx=.36,rely=0,relwidth=0.12,height=25)
    tk.Button(menu_bar_frame,text='Back',font=('Times New Roman',12,'bold'),command=lambda:backHome(main_frame)).place(relx=.95,rely=0,relwidth=0.05,height=25)

# root = tk.Tk()
# root.geometry('1100x650+10+10')
# staff_manager(root)
# root.mainloop()   
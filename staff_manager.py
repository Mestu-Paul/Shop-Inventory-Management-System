import tkinter as tk

import color_code as color
import help_functions as _help


class StaffManager:
    def __init__(self,root) -> None:
        try:
            self.root = root
        except Exception as e:
            _help.show_message('warning',f'Occur exception while staff manager object creating {e}')
    
    def backHome(self):
        print("back home")
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()
        
    def add_new_staff(self):
        print('add new')
    def manage_staff(self):
        print('manage')
    def staff_payment(self):
        print('payment')
    def payment_report(self):
        print('report')
        
    def staffManager(self):
        self.main_frame = tk.Frame(self.root,bg=color.color_list[1])
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        menu_bar_frame = tk.Frame(self.main_frame)
        menu_bar_frame.place(relx=0,rely=0,relwidth=1,height=25)
            
        tk.Button(menu_bar_frame,text='Add new staff',font=('Times New Roman',12,'bold'),command=self.add_new_staff
            ).place(relx=0,rely=0,relwidth=0.12,height=25)
        tk.Button(menu_bar_frame,text='Manage staff',font=('Times New Roman',12,'bold'),command=self.manage_staff
            ).place(relx=.12,rely=0,relwidth=0.12,height=25)
        tk.Button(menu_bar_frame,text='Staff payment',font=('Times New Roman',12,'bold'),command=self.staff_payment
            ).place(relx=.24,rely=0,relwidth=0.12,height=25)
        tk.Button(menu_bar_frame,text='Payment report',font=('Times New Roman',12,'bold'),command=self.payment_report
            ).place(relx=.36,rely=0,relwidth=0.12,height=25)
        tk.Button(menu_bar_frame,text='Back',font=('Times New Roman',12,'bold'),command=self.backHome
            ).place(relx=.95,rely=0,relwidth=0.05,height=25)

# root = tk.Tk()
# root.geometry('1100x650+10+10')
# staff_manager(root)
# root.mainloop()   
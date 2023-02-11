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
        self.main_frame = tk.Frame(self.root,bg='#ffffff')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        menu_bar_frame = tk.Frame(self.main_frame,bg='#ffffff')
        menu_bar_frame.place(relx=0,rely=0,relwidth=1,height=25)
        
        btn_frame = [tk.Frame(menu_bar_frame,bg=color.getColor('bd_menu-button')) for i in range(5)]
        btn_frame[0].place(x=0,y=0,width=60,height=22)
        btn_frame[1].place(x=60,y=0,width=60,height=22)
        btn_frame[2].place(x=120,y=0,width=60,height=22)
        btn_frame[3].place(x=180,y=0,width=60,height=22)
        btn_frame[4].place(x=240,y=0,width=60,height=22)
        
        # search button
        add_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_menu-button'), bg=color.getColor('bg_menu-button'), font=('helvic',9), text='Add', bd=0)
        add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        manage_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_menu-button'), bg=color.getColor('bg_menu-button'), font=('helvic',9), text='Manage', bd=0)
        manage_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        staff_btn = tk.Button(btn_frame[2],fg=color.getColor('fg_menu-button'), bg=color.getColor('bg_menu-button'), font=('helvic',9), text='Payment', bd=0)
        staff_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        report_btn = tk.Button(btn_frame[3],fg=color.getColor('fg_menu-button'), bg=color.getColor('bg_menu-button'), font=('helvic',9), text='Report', bd=0)
        report_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        back_btn = tk.Button(btn_frame[4],fg=color.getColor('fg_menu-button'), bg=color.getColor('bg_menu-button'), font=('helvic',9), text='Back', bd=0,command=self.backHome)
        back_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover_menu(btn_frame[0],add_btn)
        _help.button_hover_menu(btn_frame[1],manage_btn)
        _help.button_hover_menu(btn_frame[2],staff_btn)
        _help.button_hover_menu(btn_frame[3],report_btn)
        _help.button_hover_menu(btn_frame[4],back_btn)


# root = tk.Tk()
# root.geometry('1100x650+10+10')
# obj = StaffManager(root)
# obj.staffManager()
# root.mainloop()   
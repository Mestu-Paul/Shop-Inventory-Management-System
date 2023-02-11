import tkinter as tk
import tkcalendar as tkcal

import color_code as color
import pytohtml as _pytohtml
import help_functions as _help
import DAO as dao 
import datetime as dt

class ExpenditureManage:
    def __init__(self,root) -> None:
        try:
            self.root = root
            self.item_list = []
        except Exception as e:
            _help.show_message('warning',f'Occur exception while expenditure manager object creating {e}')
        pass

    def backHome(self):
        print("back home")
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()
        
        
    def addInvoiceDB(self,row):
        command = "INSERT INTO invoice(invoice_id,type,date,time,total) VALUES(?,?,?,?,?);"
        return dao.set_rows(command,row)
        
        
    def addExpenditure(self):
        lastInvoiceId = int(dao.getLastInvoiceId()[1])
        date = self.info_entries[0].get()
        time = dt.datetime.now().strftime("%I:%M:%S %p")
        row = [lastInvoiceId+1,'expenditure',date,time,self.info_entries[2].get()]
        
        command = "INSERT INTO expenditure VALUES(?,?,?,?);"
        values = [self.info_entries[1].get(),self.info_entries[2].get(),self.remarks.get('1.0','end'),lastInvoiceId+1]
        if len(values[0])==0 or len(values[1])==0:
            _help.show_message('warning','Fill fields carefully')
            return
        try:
            (float)(values[1])
        except ValueError:
            _help.show_message('warning','Amount must be number')
        
        message = dao.set_rows(command,values)
        if message[0]==0:
            _help.show_message('error',message[1])
            return
        
        command = "UPDATE basic SET total_amount = total_amount+?;"
        values = [float(values[1])]
        message = dao.set_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While updating total amount for expenditure {message[1]}')
            return
        
        message = self.addInvoiceDB(row)
        if message[0]==0:
            _help.show_message('error',f'While creating a new inv-id for expenditure {message[1]}')
            return
        _help.show_message('success','Successfully Added')
        pass
    
    def createWidget(self):
        name_list = ['Date :','Purpose :','Amount :']
        lbl_list = [tk.Label(self.main_frame,text=name_list[i], bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w') for i in range(len(name_list))]
        self.info_entries = [tkcal.DateEntry(self.main_frame)]+[tk.Entry(self.main_frame) for i in range(len(name_list)-1)]
        
        for i in range(len(name_list)):
            lbl_list[i].place(relx=0.15,rely=0.1+i*0.1, relwidth=0.1, relheight=0.07)
            self.info_entries[i].place(relx=0.25,rely=0.1+i*0.1, relwidth=0.15, relheight=0.07)
            
        tk.Label(self.main_frame,text='Amount :\n\t- for debit\n\t + for credit',anchor='w',  bg=color.getColor('bg_lbl'), fg = color.getColor('fg_lbl')
            ).place(relx=0.25,rely = 0.4)
            
        tk.Label(self.main_frame,text='Remarks :', bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w'
            ).place(relx=0.5, rely=0.1)
        self.remarks =  tk.Text(self.main_frame,height=10, width=30)
        self.remarks.place(relx=0.5, rely=0.15)
        
        btn_frame = [tk.Frame(self.main_frame,bg=color.getColor('bd_button')) for i in range(2)]
        btn_frame[0].place(relx=0.25, rely=0.8, width=90, height=22)
        btn_frame[1].place(relx=0.7, rely=0.8, width=90, height=22)
        
        # search button
        add_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Add', bd=0,command=self.addExpenditure)
        add_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        delete_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Delete', bd=0, command=self.backHome)
        delete_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame[0],add_btn)
        _help.button_hover_del(btn_frame[1],delete_btn)
        
    def expenditureManage(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg=color.getColor('bg_frame'))
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        self.createWidget()
        
# root = tk.Tk()
# root.geometry('1100x650+10+10')
# obj = ExpenditureManage(root)
# obj.expenditureManage()
# root.mainloop()
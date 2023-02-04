import tkinter as tk
import tkcalendar as tkcal

import color_code as color
import pytohtml as _pytohtml
import help_functions as _help
import DAO as dao 
import datetime as dt


class ExpenditureManage:
    def __init__(self,root) -> None:
        self.root = root
        self.item_list = []
        pass

    def backHome(self):
        print("back home")
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
        
        
        message = self.addInvoiceDB(row)
        if message[0]==0:
            _help.show_message('error',f'While creating a new inv-id for expenditure {message[1]}')
            return
        _help.show_message('success','Successfully Added')
        pass
    
    def createWidget(self):
        name_list = ['Date :','Purpose :','Amount :']
        lbl_list = [tk.Label(self.main_frame,text=name_list[i], bg=color.color_list[7], anchor='w') for i in range(len(name_list))]
        self.info_entries = [tkcal.DateEntry(self.main_frame)]+[tk.Entry(self.main_frame) for i in range(len(name_list)-1)]
        
        for i in range(len(name_list)):
            lbl_list[i].place(relx=0.15,rely=0.1+i*0.1, relwidth=0.1, relheight=0.07)
            self.info_entries[i].place(relx=0.25,rely=0.1+i*0.1, relwidth=0.15, relheight=0.07)
            
        tk.Label(self.main_frame,text='Remarks :', bg=color.color_list[7], anchor='w'
            ).place(relx=0.5, rely=0.1)
        self.remarks =  tk.Text(self.main_frame,height=10, width=30)
        self.remarks.place(relx=0.5, rely=0.15)
        
        
        tk.Button(self.main_frame,text='Add',bg=color.color_list[2], fg = color.color_list[3], command=self.addExpenditure
            ).place(relx=0.25, rely=0.8, width=80, height=30)
        tk.Button(self.main_frame,text='Cancel',bg=color.color_list[2], fg = color.color_list[3], command=self.backHome
            ).place(relx=0.7, rely=0.8, width=80, height=30)
        
    def expenditureManage(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg=color.color_list[7])
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
        self.createWidget()
        
# root = tk.Tk()
# root.geometry('1100x650+10+10')
# obj = ExpenditureManage(root)
# obj.expenditureManage()
# root.mainloop()
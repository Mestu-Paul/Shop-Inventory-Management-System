import tkinter as tk
from tkinter import ttk
import DAO as dao
import help_functions as _help
import color_code as color

class Last15Invoice:
    def __init__(self):
        pass
    
    def getTotal(self):
        command = 'SELECT total_amount FROM basic;'
        message = dao.get_rows(command,[])
        if message[0]==0:
            _help.show_message('error',f'Fount an exception while retrieving main balance {message[0]}')
            return "error"
        return message[1][0][0]
    
    def mainFrame(self):
        tk.Label(self.main_frame,text='Account and last 15 invoice', bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), font=('Helvic', 15)
                ).pack(side=tk.TOP,pady=5)
        self.showTable()
        
        tk.Label(self.main_frame,text=f'Total Amount ${self.getTotal()}', bg='#ffffff', fg='#000000',font=('Helvic', 15)
            ).place(relx=0,rely=0.755,relwidth=1,relheight=0.1)
        btn_frame = tk.Frame(self.main_frame,bg=color.getColor('bd_button'))
        btn_frame.place(relx=0.7,rely=0.87,width=90,height=22)
        close_btn =  tk.Button(btn_frame,text='Close',bd=0,bg=color.getColor('bg_button'), fg=color.getColor('fg_button'), command=self.root.destroy)
        close_btn.pack(fill='both',expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame,close_btn)
        
        
    def last15Invoice(self):
        try:
            self.root = tk.Tk()
            self.root.geometry('500x700+450+10')
            self.root.title('Account')
            self.root.grab_set()
            
            self.main_frame = tk.Frame(self.root,bg=color.getColor('bg_frame'))
            self.main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
            self.mainFrame()
            
            self.root.mainloop()
        except Exception as e:
            _help.show_message('warning',f'Found an exception while showing last 15 invoice {e}')
        
        
    def showTable(self):
        table_frame = tk.Frame(self.main_frame,bg='#ffffff')
        table_frame.place(relx=0,rely=0.15,relwidth=1,relheight=0.6)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        columns = [f'c{i}' for i in range(1,4)]
        headings = ['SI','Type','Amount','INV-id']
        column_size = [20,50,50,50]
        column_anchor = ['e','center','w','center']
        
        # treeview
        self.tree = tk.ttk.Treeview(table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        self.add_item_list = [['a','b','c']]
        for i in range(0,len(self.add_item_list)):
            self.tree.insert("",tk.END,values=[i+1]+self.add_item_list[i],tag = row_color[i%2])

        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
        
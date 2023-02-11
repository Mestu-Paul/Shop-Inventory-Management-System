import tkinter as tk

from home import *
import color_code as color
import pytohtml as _pytohtml
import help_functions as _help


class ExpenditureReport:
    def __init__(self,root) -> None:
        try:
            self.root = root
            self.item_list = []
        except Exception as e:
            _help.show_message('warning',f'Occur exception while  object creating {e}')
        pass

    def backHome(self):
        print("back home")
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()

    def preview(self):
        receipt_name = ' Expenditure'
        date = dt.datetime.today().date()
        headings = ['SI','Purpose','Amount','Remarks','INV-id','Date','Time']
        total_info_name = ['Total Expenditure :','Expenditure Credit :', 'Expenditure Debit :', 'Total Expenditure Amount :']
        total_info = [0 for i in range(len(total_info_name))]
        rows = []
        for i,row in enumerate(self.item_list):
            rows.append([i+1]+list(row))
            total_info[0] += 1 # qty
            if float(row[1])>=0:
                total_info[1] += float(row[1])
            else:
                total_info[2] += float(row[1])
            total_info[3] += float(row[1])
            
        total_info[2] = abs(total_info[2]) # make debit positive
        obj = _pytohtml.PythonToHtml()
        obj.stockReceipt(receipt_name,date,'N/A',headings,rows,total_info_name,total_info)
    
    def topFrame(self):
        # search type
        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w', font=('Times New Roman',12), text='Search by :'
            ).place(relx=0.01, rely=0.08, relwidth=0.08, relheight=0.1)

        product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        product_search_type.set(search_type_list[0]) # default value
        search_type = tk.ttk.OptionMenu(self.top_frame, product_search_type, *search_type_list)
        search_type.place(relx=0.09, rely=0.08, relwidth=0.1, relheight=0.12)

        # search box
        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'), anchor='w', font=('Times New Roman',12), text='Query :'
            ).place(relx=0.01, rely=0.25, relwidth=0.08, relheight=0.1)

        self.query = tk.Entry(self.top_frame)
        self.query.place(relx=0.09, rely=0.25, relwidth=0.1, relheight=0.1)

        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'),anchor='w', font=('Times New Roman',12), text='From :'
            ).place(relx=0.01,rely=.4,relwidth=0.1)
        
        tk.Label(self.top_frame,bg=color.getColor('bg_lbl'), fg=color.getColor('fg_lbl'),anchor='w', font=('Times New Roman',12), text='To :'
            ).place(relx=0.13,rely=0.4,relwidth=0.1)
        
        self.search_from_date = tkcal.DateEntry(self.top_frame,selecmode='day', cursor='hand1')
        self.search_from_date.place(relx=0.01,rely=.52,relwidth=0.1)
        
        self.search_to_date = tkcal.DateEntry(self.top_frame,selecmode='day', cursor='hand1')
        self.search_to_date.place(relx=0.13,rely=.52,relwidth=0.1)
        
        btn_frame = [tk.Frame(self.top_frame,bg=color.getColor('bd_button')) for i in range(4)]
        btn_frame[0].place(relx=0.05, rely=0.72, width=90, height=22)
        btn_frame[1].place(relx=0.8, rely=0.15, width=90, height=22)
        btn_frame[2].place(relx=0.8, rely=0.35, width=90, height=22)
        btn_frame[3].place(relx=0.8, rely=0.55, width=90, height=22)

        # search button
        search_btn = tk.Button(btn_frame[0],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Search', bd=0)
        search_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        refresh_btn = tk.Button(btn_frame[1],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Refresh', bd=0)
        refresh_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        preview_btn = tk.Button(btn_frame[2],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Preview', bd=0,command=self.preview)
        preview_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)

        back_btn = tk.Button(btn_frame[3],fg=color.getColor('fg_button'), bg=color.getColor('bg_button'), font=('Times New Roman',12), text='Back', bd=0,command=self.backHome)
        back_btn.pack(fill=tk.BOTH, expand=True,padx=1,pady=1)
        _help.button_hover(btn_frame[0],search_btn)
        _help.button_hover(btn_frame[1],refresh_btn)
        _help.button_hover(btn_frame[2],preview_btn)
        _help.button_hover(btn_frame[3],back_btn)
    
    def on_select(self,event):
        selected_items = self.tree.selection()
        
        for item in selected_items:
            item_values = self.tree.item(item)["values"]
            self.selected_si = item_values[0]
                
    def showTable(self):
        table_frame = tk.Frame(self.bottom_frame,bg='#ffffff')
        table_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        headings = ['SI','Purpose','Amount','Remarks','INV-id','Date','Time']
        columns = [f'c{i}' for i in range(1,len(headings)+1)]
        column_size = [40] + [80 for i in range(1,len(headings))]
        column_anchor = ['e','center','w','center','center','w','w']
        
        print(self.item_list)
        # treeview
        self.tree = tk.ttk.Treeview(table_frame, column=columns, show='headings', yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        for i in range(0,len(columns)):
            self.tree.heading(columns[i], text=headings[i])
            self.tree.column(columns[i],width=column_size[i],anchor=column_anchor[i])
            
        row_color = ["red_row","red_green"]
        self.tree.tag_configure("red_row", background="#e1e1e1")
        self.tree.tag_configure("red_green", background="#a9a9a9")
        
        for i in range(0,len(self.item_list)):
            self.tree.insert("",tk.END,values=[i+1]+list(self.item_list[i]),tag = row_color[i%2])

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.place(relx=0,rely=0,relwidth=0.97,relheight=.95)
        scrollbary.place(relx=0.97,rely=0,relwidth=0.03,relheight=1)
        scrollbary.config( command = self.tree.yview )
        scrollbarx.config(orient='horizontal', command=self.tree.xview)
        scrollbarx.place(relx=0,rely=0.95,relwidth=1,relheight=0.05)
    
    def bottomFrame(self):
        command = "SELECT ep.purpose,ep.amount,ep.remarks,\
            inv.invoice_id,inv.date,inv.time\
            FROM expenditure as ep\
            JOIN invoice as inv ON ep.invoice_id = inv.invoice_id \
            WHERE inv.type=?;"
        values = ['expenditure']
        message = dao.get_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While fetching item data {message[1]}')
            return
        
        self.item_list = message[1]
        print(message[1])
        self.showTable()
      
    def expenditureReport(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

        # ======================== top frame ===================== #
        self.top_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.35)
        self.topFrame()
        
        # ======================== bottom frame ===================== #
        self.bottom_frame = tk.Frame(self.main_frame,bg=color.getColor('bg_frame'))
        self.bottom_frame.place(relx=0,rely=0.35,relwidth=1,relheight=0.65)
        self.bottomFrame()
        
# root = tk.Tk()
# root.geometry('1100x650+10+10')
# obj = PurchaseReport(root)
# obj.purchaseReport()
# root.mainloop()
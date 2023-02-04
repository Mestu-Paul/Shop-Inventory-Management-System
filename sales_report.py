import tkinter as tk

from home import *
import color_code as color
import pytohtml as _pytohtml
import help_functions as _help


class SalesReport:
    def __init__(self,root) -> None:
        self.root = root
        self.item_list = []
        pass

    def backHome(self):
        print("back home")
        _help.init_page(self.root,'Sale Item')
        self.main_frame.place_forget()

    def preview(self):
        receipt_name = ' Purchase Item'
        date = dt.datetime.today().date()
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','Total','Discount','VAT(tk)','Payable','inv-id','Date','Time']
        total_info_name = ['Total item Quantity :','Total Purchase Price :']
        total_info = [0 for i in range(len(total_info_name))]
        rows = []
        for i,row in enumerate(self.item_list):
            rows.append([i+1]+list(row))
            total_info[0] += float(row[5]) # qty
            total_info[1] += float(row[6]) # purchase
        
        obj = _pytohtml.PythonToHtml()
        obj.stockReceipt(receipt_name,date,'N\A',headings,rows,total_info_name,total_info)
    
    def topFrame(self):
        # search type
        tk.Label(self.top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Search by :'
            ).place(relx=0.01, rely=0.08, relwidth=0.08, relheight=0.1)

        product_search_type = tk.StringVar()
        search_type_list = ['name', "code", "company",'group']
        product_search_type.set(search_type_list[0]) # default value
        search_type = tk.OptionMenu(self.top_frame, product_search_type, *search_type_list)
        search_type.place(relx=0.09, rely=0.08, relwidth=0.1, relheight=0.12)

        # search box
        tk.Label(self.top_frame,bg=color.color_list[7], anchor='w', font=('Times New Roman',12), text='Query :'
            ).place(relx=0.01, rely=0.25, relwidth=0.08, relheight=0.1)

        self.query = tk.Entry(self.top_frame)
        self.query.place(relx=0.09, rely=0.25, relwidth=0.1, relheight=0.1)

        tk.Label(self.top_frame,bg=color.color_list[7],anchor='w', font=('Times New Roman',12), text='From :'
            ).place(relx=0.01,rely=.4,relwidth=0.1)
        
        tk.Label(self.top_frame,bg=color.color_list[7],anchor='w', font=('Times New Roman',12), text='To :'
            ).place(relx=0.13,rely=0.4,relwidth=0.1)
        
        self.search_from_date = tkcal.DateEntry(self.top_frame,selecmode='day', cursor='hand1')
        self.search_from_date.place(relx=0.01,rely=.52,relwidth=0.1)
        
        self.search_to_date = tkcal.DateEntry(self.top_frame,selecmode='day', cursor='hand1')
        self.search_to_date.place(relx=0.13,rely=.52,relwidth=0.1)
        
        # search button
        tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Search'
            ).place(relx=0.05, rely=0.72, relwidth=0.1, relheight=0.12)
        
        # refresh button
        tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Refresh'
            ).place(relx=0.8, rely=0.15, relwidth=0.1, relheight=0.14)

        # preview buttom
        tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Preview',command=self.preview
            ).place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.14)

        # back home
        tk.Button(self.top_frame,fg=color.color_list[3], bg=color.color_list[2], font=('Times New Roman',12), text='Back',command=self.backHome
            ).place(relx=0.8, rely=0.55, relwidth=0.1, relheight=0.14)
        
    
    def on_select(self,event):
        selected_items = self.tree.selection()
        
        for item in selected_items:
            item_values = self.tree.item(item)["values"]
            self.selected_si = item_values[0]
                
    def showTable(self):
        table_frame = tk.Frame(self.bottom_frame,bg=color.color_list[1])
        table_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        scrollbary = tk.Scrollbar(table_frame)
        scrollbarx = tk.Scrollbar(table_frame)
        
        headings = ['SI','Code','Name','Group','Company','VAT(%)','QTY','Purchase','Total','Discount','VAT(tk)','Payable','inv-id','Date','Time']
        columns = [f'c{i}' for i in range(1,len(headings)+1)]
        column_size = [40] + [80 for i in range(2,len(headings)+1)]
        column_anchor = ['e','center','center','center','center','w','w','w','w','w','w','w','w','w','w']
        
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
        
        command = "SELECT sp.code,sp.name,it.group_,it.company,it.vat_rate,sp.quantity,sp.unit_price,\
            sp.total_price,sp.discount,sp.vat,sp.payable,inv.invoice_id,inv.date,inv.time\
            FROM sale_purchase as sp, item_details as it\
            JOIN invoice as inv ON sp.invoice_id = inv.invoice_id \
            WHERE inv.type=? AND it.code=sp.code;"
        values = ['sale']
        message = dao.get_rows(command,values)
        if message[0]==0:
            _help.show_message('error',f'While fetching item data {message[1]}')
            return
        
        self.item_list = message[1]
        print(message[1])
        self.showTable()
      
    def salesReport(self):
        # item manage main frame
        self.main_frame = tk.Frame(self.root,bg='white')
        self.main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

        # ======================== top frame ===================== #
        self.top_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.top_frame.place(relx=0,rely=0,relwidth=1,relheight=0.35)
        self.topFrame()
        
        # ======================== bottom frame ===================== #
        self.bottom_frame = tk.Frame(self.main_frame,bg=color.color_list[7])
        self.bottom_frame.place(relx=0,rely=0.35,relwidth=1,relheight=0.65)
        self.bottomFrame()

# root = tk.Tk();
# root.geometry('1100x650+10+10')
# sales_report(root)
# root.mainloop()
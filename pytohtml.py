import pdfkit
import os
class PythonToHtml:
    def __init__(self) -> None:
        self.total_info_name = ['Total','Discount','VAT','Payable','Paid','Change']
        self.config = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')        
        pass
    
    def saleReceipt(self,item_name,item_qty,item_price,total_info):
        self.html = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {{
            margin: 0px;
            padding: 0px;
        }}

        .page {{
            margin: 10px auto;
            height: max-content;
            padding: 10px;
            width: 350px;
            border: dashed;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}

        .shop-name {{
            font-size: 20px
        }}

        .dash-line {{
            width: 90%;
            border-top: 1px dashed;
            border-spacing: 20px;
            margin: 10px auto;
        }}

        .left-frame p {{
            padding: 5px 0px;
        }}

        .item-list-container {{
            display: flex;
            background-color: #d1d1d1;
        }}

        .item-list-container table {{
            margin: 0px auto;
            width: 90%;
            text-align: left;
        }}
    </style>
</head>

<body>
    <div class="page">
        <div class="shop-name">ABC Fashion House</div>
        <p style="font-size:16px">Transaction Receipt</p>
        <div class="dash-line"></div>
        <div class="item-list-container">
            <table>
                <tr>
                    <th>Item (qty)</th>
                    <th>Qty</th>
                    <th>Price</th>
                    <th>Total</th>
                </tr>
        """
        for i in range(0,len(item_name)):
            self.html += f"""
                <tr>
                    <td>{item_name[i]}</td>
                    <td>{item_qty[i]}</td>
                    <td>{format(float(item_price[i]),'.2f')}</td>
                    <td>{format(float(item_price[i]*item_qty[i]),'.2f')}</td>
                </tr>
        """
        self.html+="""
            </table>
        </div>
        <div class="dash-line"></div>
        <div class="item-list-container">
            <table>
        """
        for i in range(0,len(total_info)):
            self.html += f"""
                <tr>
                    <td>{self.total_info_name[i]}</td>
                    <td>{format(float(total_info[i]),'.2f')}</td>
                </tr>
        """
        self.html+="""
            </table>
        </div>
        <div class="dash-line"></div>
        <div style="font-size: 18px; text-align: center;">
            Thank You
        </div>
    </div>
</body>

</html>
        """
        with open("receipt.html", "w") as file:
            file.write(self.html)
        
        pdfkit.from_file('receipt.html', 'cash_memo.pdf',configuration=self.config)
        os.startfile('cash_memo.pdf')

    def stockReceipt(self,receipt_name, date, headings, rows, total_info_name, total_info):
        html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        .page {
            margin: 10px auto;
            height: max-content;
            padding: 10px;
            width: 90%;
            border: dashed;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }
        #receipt_name{
            text-align: left;
            margin-left: 5%;
        }
        #basic_info{
            text-align: right;
            margin-right: 5%;
        }
        .shop-name {
            font-size: 20px
        }

        .dash-line {
            width: 90%;
            border-top: 1px dashed;
            border-spacing: 20px;
            margin: 10px auto;
        }

        .left-frame p {
            padding: 5px 0px;
        }

        .item-list-container {
            display: flex;
            background-color: #fff;
        }
        .total-items-info {
            display: flex;
            background-color: #f1f1f1;
            width: 90%;
            margin: 0 auto;
        }
        .total-items-info table{
            text-decoration: none;
            width: 70%;
            margin: 10px auto;
        }
        .item-list-container table {
            margin: 0px auto;
            width: 90%;
            text-align: left;
        }
        .item-list-container table,
        .item-list-container tr,
        .item-list-container th,
        .item-list-container td{
            border: 1px solid black;
            border-collapse: collapse;
            padding: 3px;
        }
        .item-list-container th{
            background-color: #555;
            color: #fff;
        }
        .item-list-container tr:nth-child(odd){
            background-color: #d1d1d1;
        }
    </style>
</head>
"""
        html += f"""
<body>
    <div class="page">
        <div class="shop-name">ABC Fashion House</div>
        <p style="font-size:16px">Transaction Receipt</p>
        <table style="width: 90%; margin: auto;">
            <tr>
                <td align="left">Receipt Name:{receipt_name}</td>
                <td align="right">Date: {date}</td>
            </tr>
        </table>
        <div class="dash-line"></div>
        <div class="item-list-container">
            <table>
                <tr>"""
        for head in headings:
            html += f"""
                    <th align="center">{head}</th>"""
        html += """
                </tr>
"""
        for row in rows:
            html += """
                <tr>"""         
            for data in row:
                html += f"""
                    <td>{data}</td>"""
            html += """
                </tr>
            """
        html += """
            </table>
        </div>
        <div class="dash-line"></div>
        <div class="total-items-info">
            <table>
"""
        for name,info in zip(total_info_name,total_info):
            html += f"""
                <tr>
                    <th align="left">{name}</th>
                    <td>{info}</td>
                </tr>"""
        html += """
            </table>
        </div>
        <div class="dash-line"></div>
        <div style="font-size: 18px; text-align: center;">
            Thank You
        </div>
    </div>
</body>

</html>
        
        """
        with open("receipt.html", "w") as file:
            file.write(html)
        pdfkit.from_file("receipt.html", 'cash_memo.pdf',configuration=self.config)
        os.startfile('cash_memo.pdf')

# pdfkit.from_file('receipt.html','cash_memo.pdf',configuration=config)
# os.startfile('cash_memo.pdf')

# path = C:\Program Files (x86)\wkhtmltopdf

# obj = PythonToHtml()
# rows = [[2,2,2],[3,3,3],[1,1,1],[1,1,1]]
# obj.stockReceipt("stock item","03/02/2023",['name','id','value'],rows,['a','','b','c'],[1,'',2,3])
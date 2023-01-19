purchase_info_list = ['Total Item :', 'Total Price :', 'Discount :',
                      'Payable :', 'Total Paid :', 'Change/Due :']
for i in range(0,len(purchase_info_list)):
    left_frame_2_frame_payment_info_lbl = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text=purchase_info_list[i])
    left_frame_2_frame_payment_info_lbl.place(relx=0.01, rely=0.01+0.1*i, relwidth=0.4, relheight=0.08)     



# total item 
left_frame_2_frame_payment_info_lbl_1 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text='Total item :')
left_frame_2_frame_payment_info_lbl_1.place(relx=0.42, rely=0.01, relwidth=0.4, relheight=0.08)

# total price
left_frame_2_frame_payment_info_lbl_2 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text='Total price :')
left_frame_2_frame_payment_info_lbl_2.place(relx=0.42, rely=0.1, relwidth=0.4, relheight=0.08)

# discount 
left_frame_2_frame_payment_info_lbl_5 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text='Total item :')
left_frame_2_frame_payment_info_lbl_5.place(relx=0.42, rely=0.2, relwidth=0.4, relheight=0.08)

# Payable
left_frame_2_frame_payment_info_lbl_7 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text='Total item :')
left_frame_2_frame_payment_info_lbl_7.place(relx=0.42, rely=0.3, relwidth=0.4, relheight=0.08)

# total paid
left_frame_2_frame_payment_info_total_paid = tk.Entry(left_frame_2_frame_payment_info)
left_frame_2_frame_payment_info_total_paid.place(relx=0.42, rely=0.4, relwidth=0.4, relheight=0.08)

# change/due
left_frame_2_frame_payment_info_lbl_10 = tk.Label(left_frame_2_frame_payment_info,bg=left2_bg, anchor='w', font=('Times New Roman',12), text='Total item :')
left_frame_2_frame_payment_info_lbl_10.place(relx=0.42, rely=0.5, relwidth=0.4, relheight=0.08)

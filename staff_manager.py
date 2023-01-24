import tkinter as tk

import color_code as color


def back_home(main_frame):
    print("back home")
    main_frame.place_forget()
def add_new_staff(main_frame):
    pass
def manage_stuff(main_frame):
    pass
def stuff_payment(main_frame):
    pass
def payment_report(main_frame):
    pass
def staff_manager(root):
    main_frame = tk.Frame(root,bg=color.color_list[1])
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)
    staff_menu = tk.Menu(main_frame)
    main_frame.config(menu=staff_menu)
    # add_new_staff(main_frame)
    # staff_menu.add_command(
    #     label='Add New',
    #     command=lambda:add_new_staff(main_frame)
    # )
    # staff_menu.add_command(
    #     label='Manage Stuf',
    #     command=lambda:manage_stuff(main_frame)
    # )
    # staff_menu.add_command(
    #     label='Stuff Payment',
    #     command=lambda:stuff_payment(main_frame)
    # )
    # staff_menu.add_command(
    #     label='Payment Report',
    #     command=lambda:payment_report(main_frame)
    # )

root = tk.Tk()
root.geometry('1100x650+10+10')
staff_manager(root)
root.mainloop()
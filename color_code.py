import tkinter as tk
from tkinter import colorchooser

# color code 
# color1 = '#297592'
# color2 = '#ffffff'
# color3 = '#3bbd75'
# color4 = '#000000'
# color5 = '#13dbcc'
# color6 = '#b1b13d'
# red    = '#ff0000'
# light_grey = '#e1e1e1'
global color_list,temp_color_list
color_list = ['#297592','#ffffff','#3bbd75','#000000','#13dbcc','#b1b13d','#ff0000','#e1e1e1']
temp_color_list = [color for color in color_list]

def fun():
    print('button clicked')
def update_preview(main_frame):
    # preview
    tk.Label(main_frame,text='Top frame 1', bg=temp_color_list[0],fg=temp_color_list[1]).place(relx=0.34,rely=0.15,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Top frame 2', bg=temp_color_list[2],fg=temp_color_list[3]).place(relx=0.34,rely=0.2,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Left frame 1',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.25,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Left frame 2',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.3,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Left frame 3',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.35,relwidth=0.1,height=30)
    
def choose_color(idx,main_frame):
	# variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    global color_list,temp_color_list
    temp_color_list[idx] = color_code[1]
    print(color_code[1])
    update_preview(main_frame)
    
def backHome(main_frame):
    global color_list,temp_color_list
    print("back home")
    print(color_list)
    main_frame.place_forget()
    
    
def color_update_apply(main_frame):
    # print("update ",color_list)
    global color_list,temp_color_list
    color_list=[color for color in temp_color_list]
    print(color_list)
    backHome(main_frame)
    
    
def color_change(root):
    global color_list,temp_color_list
    temp_color_list = [color for color in color_list]
    print('I am here color change')
    main_frame = tk.Frame(root)
    main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    tk.Label(main_frame,text='Background Color', fg=color_list[1], bg=color_list[0]).place(relx=0.1,rely=0.1,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Font Color', fg=color_list[1], bg=color_list[0]).place(relx=0.22,rely=0.1,relwidth=0.1,height=30)
    tk.Label(main_frame,text='Preview', fg=color_list[1], bg=color_list[0]).place(relx=0.34,rely=0.1,relwidth=0.1,height=30)
    # background color 
    tk.Button(main_frame,text='Top frame 1',bg=color_list[2],fg=color_list[1],command= lambda:choose_color(0,main_frame)).place(relx=0.1,rely=0.15,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Top frame 2',bg=color_list[2],fg=color_list[1],command= lambda:choose_color(2,main_frame)).place(relx=0.1,rely=0.2,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 1',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.1,rely=0.25,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 2',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.1,rely=0.3,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 3',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.1,rely=0.35,relwidth=0.1,height=30)
    # text color 
    tk.Button(main_frame,text='Top frame 1',bg=color_list[2],fg=color_list[1],command= lambda:choose_color(1,main_frame)).place(relx=0.22,rely=0.15,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Top frame 2',bg=color_list[2],fg=color_list[1],command= lambda:choose_color(3,main_frame)).place(relx=0.22,rely=0.2,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 1',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.22,rely=0.25,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 2',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.22,rely=0.3,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Left frame 3',bg=color_list[2],fg=color_list[1],command=lambda:choose_color(1,main_frame)).place(relx=0.22,rely=0.35,relwidth=0.1,height=30)
    
    update_preview(main_frame)
    
    tk.Button(main_frame,text='Apply',bg=color_list[2],command=lambda:color_update_apply(main_frame)).place(relx=0.12,rely=0.65,relwidth=0.1,height=30)
    tk.Button(main_frame,text='Cancel',bg=color_list[2],command=lambda:backHome(main_frame)).place(relx=0.32,rely=0.65,relwidth=0.1,height=30)
# root = tk.Tk()
# root.geometry('1100x650+10+10')
# color_change(root)
# root.mainloop()
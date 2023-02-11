import tkinter as tk
from tkinter import colorchooser
import random
# color code 
# color1 = '#297592'
# color2 = '#ffffff'
# color3 = '#3bbd75'
# color4 = '#000000'
# color5 = '#13dbcc'
# color6 = '#b1b13d'
# red    = '#ff0000'
# light_grey = '#e1e1e1'
# ['#ae1e3a', '#ffffff', '#cbb6bb', '#000000', '#13dbcc', '#b1b13d', '#ff0000', '#e1e1e1']
global color_list,temp_color_list
color_list = ['#297592','#ffffff','#3bbd75','#000000','#13dbcc','#b1b13d','#ff0000','#e1e1e1']
temp_color_list = [color for color in color_list]

# bg = background
# fg = foreground
# lt = layout 
# f = frame
# b = button
# l = label
keys = ['bg_main1','fg_main1','bg_main2','fg_main2', # top 2 label
        'bg_lt1_f1','fg_lt1_f1','bg_lt1_f1_b1','fg_lt1_f1_b1', # layout 1 first(leftest) frame
        'bg_lt1_f2','fg_lt1_f2','bg_lt1_f2_l1','fg_lt1_f2_l1','bg_lt1_f2_b1','fg_lt1_f2_b1', # layout 1 second(middle) frame
        'bg_lt1_f3','fg_lt1_f3','bg_lt1_f3_l1','fg_lt1_f3_l1','bg_lt1_f3_b1','fg_lt1_f3_b1', # layout 1 third(last) frame
        'bg_lt2_f1','fg_lt2_f1','bg_lt2_f1_l1','fg_lt2_f1_l1','bg_lt1_f1_b1','fg_lt1_f1_b1', # layout 2 first frame 
        'bg_lt2_f2','fg_lt2_f2','bg_lt2_f2_l1','fg_lt2_f2_l1','bg_lt1_f2_b1','fg_lt1_f2_b1', # layout 2 second frame 
        'bg_lt3_f1','fg_lt3_f1','bg_lt3_f1_l1','fg_lt3_f1_l1','bg_lt1_f1_b1','fg_lt1_f1_b1', # laypit 3 first frame
        ]

cl = {
'bg_main1' : '#fdfdfd',
'fg_main1' : '#656532',    
'bg_main2' : '#d2d2a6',    
'fg_main2' : '#000000',    

'bg_frame' : '#f5f5f5',   

'bg_lbl' : '#f5f5f5',
'fg_lbl' : '#000000',

'bg_input' : '#ffffff',
'fg_input' : '#000000',
'bd_input' : '#b0a9a9',
'bd_input-h': '#2885e8',

'bg_button' : '#f8f5f5',
'fg_button' : '#000000',
'bd_button' : '#b0a9a9',

'bg_button-h' : '#e8f8f6',
'bd_button-h' : '#2885e8',
'bg_button_del-h' : '#fbf4f4',
'bd_button_del-h' : '#ef4242',

'bg_menu-button' : '#ffffff',
'fg_menu-button' : '#000000',
'bd_menu-button' : '#ffffff',
'bg_menu-button-h' : '#e8f8f6',
'bd_menu-button-h' : '#c7d4e0',
}
tcl = cl.copy()

background = None
foreground = None

# gmain_frame = tk.Frame()

def getColor(name):
    return cl[name]

def update_preview():
    global gmain_frame
    # preview
    tk.Label(gmain_frame,text='Top frame 1', bg=temp_color_list[0],fg=temp_color_list[1]).place(relx=0.34,rely=0.15,relwidth=0.1,height=30)
    tk.Label(gmain_frame,text='Top frame 2', bg=temp_color_list[2],fg=temp_color_list[3]).place(relx=0.34,rely=0.2,relwidth=0.1,height=30)
    tk.Label(gmain_frame,text='Left frame 1',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.25,relwidth=0.1,height=30)
    tk.Label(gmain_frame,text='Left frame 2',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.3,relwidth=0.1,height=30)
    tk.Label(gmain_frame,text='Left frame 3',bg=temp_color_list[7],fg=temp_color_list[3]).place(relx=0.34,rely=0.35,relwidth=0.1,height=30)

def choose_color_fg(lbl,fg):
	# variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose foreground color")
    global cl,tcl
    tcl[fg] = color_code[1]
    lbl.config(fg=tcl[fg])
    for child in lbl.winfo_children():
        relx = child.winfo_x()/lbl.winfo_width()
        rely = child.winfo_y()/lbl.winfo_height()
        relwidth = child.winfo_width()/lbl.winfo_width()
        relheight = child.winfo_height()/lbl.winfo_height()
        child.place(relx=relx,rely=rely,relwidth=relwidth,relheight=relheight)
    
def choose_color_bg(event,lbl,bg,fg):
    print(bg,fg)
	# variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose background color")
    global cl,tcl
    tcl[bg] = color_code[1]
    lbl.config(bg=color_code[1],highlightbackground=color_code[1],highlightcolor=color_code[1])
    choose_color_fg(lbl,fg)
    
    
def backHome(main_frame):
    global color_list,temp_color_list
    print("back home")
    print(color_list)
    main_frame.place_forget()
    
    
def color_update_apply(main_frame):
    global color_list,temp_color_list
    color_list=[color for color in temp_color_list]
    global tcl,cl 
    cl = tcl.copy()
    print(color_list)
    backHome(main_frame)
    
def set_entry_value(entry_name,entry_value):
    entry_name.delete(0,"end")
    entry_name.insert(0,entry_value)
def showColor(event,val):
    print("label pressed",val.cget('bg'),val.cget('fg'))
    global background,foreground
    h = val.cget('bg').lstrip('#')
    set_entry_value(background,tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
    h = val.cget('fg').lstrip('#')
    set_entry_value(foreground,tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

def layout1(frame):
    f = ['bg_lt1_f1','fg_lt1_f1','bg_lt1_f2','fg_lt1_f2','bg_lt1_f3','fg_lt1_f3',
        'bg_lt1_f1_b1','fg_lt1_f1_b1',
        'bg_lt1_f2_l1','fg_lt1_f2_l1','bg_lt1_f2_b1','fg_lt1_f2_b1',
        'bg_lt1_f3_l1','fg_lt1_f3_l1','bg_lt1_f3_b1','fg_lt1_f3_b1']
    
    
    lbl = [tk.Label(frame) for i in range(22)]
    lbl[0] = tk.Label(frame,bg=tcl[f[0]], fg=tcl[f[1]])
    lbl[0].place(relx=0,rely=0,relwidth=0.2,relheight=1)
    lbl[1] = tk.Label(frame,bg=tcl[f[2]], fg=tcl[f[3]])
    lbl[1].place(relx=0.2,rely=0,relwidth=0.3,relheight=1)
    lbl[2] = tk.Label(frame,bg=tcl[f[4]],fg=tcl[f[5]])
    lbl[2].place(relx=0.5,rely=0,relwidth=0.5,relheight=1)
    for i in range(3):
        lbl[i].bind("<Double-Button-1>",lambda e,val=lbl[i],bg=f[i*2],fg=f[i*2+1]:choose_color_bg(e,val,bg,fg))
    
    # frame-1
    for i in range(6):
        lbl[i+3] = tk.Button(lbl[0],bg=tcl[f[6]], fg=tcl[f[7]], text='Button' )
        lbl[i+3].place(relx=0.25,rely=0.05+i*0.12,relwidth=0.5,relheight=0.1)
        lbl[i+3].bind("<Double-Button-1>",lambda e,val=lbl[i+3],bg=f[3*2],fg=f[3*2+1]:choose_color_bg(e,val,bg,fg))

    # frame-2
    for i in range(5):
        lbl[i+9] = tk.Button(lbl[1],bg=tcl[f[8]], fg=tcl[f[9]], text='Label',bd=0 )
        lbl[i+9].place(relx=0.01,rely=0.05+i*0.12,relwidth=0.3,relheight=0.1)
        tk.Button(lbl[1],bg='#ffffff', text='input box' ,bd=0).place(relx=0.37,rely=0.05+i*0.12,relwidth=0.5,relheight=0.1)
        lbl[i+9].bind("<Double-Button-1>",lambda e,val=lbl[i+9],bg=f[4*2],fg=f[4*2+1]:choose_color_bg(e,val,bg,fg))
        
    lbl[15] = tk.Button(lbl[1],bg=tcl[f[10]], fg=tcl[f[11]], text='button' ,bd=0)
    lbl[15].place(relx=0.05,rely=0.05+6*0.12,relwidth=0.4,relheight=0.1)
    lbl[16] = tk.Button(lbl[1],bg=tcl[f[10]], fg=tcl[f[11]], text='button',bd=0 )
    lbl[16].place(relx=0.57,rely=0.05+6*0.12,relwidth=0.4,relheight=0.1)
    lbl[15].bind("<Double-Button-1>",lambda e,val=lbl[15],bg=f[10],fg=f[10+1]:choose_color_bg(e,val,bg,fg))
    lbl[16].bind("<Double-Button-1>",lambda e,val=lbl[16],bg=f[10],fg=f[10+1]:choose_color_bg(e,val,bg,fg))
        
    # frame-3
    for i in range(4):
        lbl[i+16] = tk.Button(lbl[2],bg=tcl[f[12]], fg=tcl[f[13]], bd=0, text='Label' )
        lbl[i+16].place(relx=0.01,rely=0.05+i*0.12,relwidth=0.3,relheight=0.1)
        tk.Button(lbl[2],bg='#ffffff', bd=0, text='input box' ).place(relx=0.37,rely=0.05+i*0.12,relwidth=0.5,relheight=0.1)
        lbl[i+16].bind("<Double-Button-1>",lambda e,val=lbl[i+16],bg=f[6*2],fg=f[6*2+1]:choose_color_bg(e,val,bg,fg))
        
    lbl[20] = tk.Button(lbl[2],bg=tcl[f[14]], fg=tcl[f[15]], bd=0, text='button' )
    lbl[20].place(relx=0.15,rely=0.05+4*0.12,relwidth=0.3,relheight=0.1)
    lbl[21] = tk.Button(lbl[2],bg=tcl[f[14]], fg=tcl[f[15]], bd=0, text='button' )
    lbl[21].place(relx=0.66,rely=0.05+4*0.12,relwidth=0.3,relheight=0.1)
    lbl[20].bind("<Double-Button-1>",lambda e,val=lbl[20],bg=f[14],fg=f[14+1]:choose_color_bg(e,val,bg,fg))
    lbl[21].bind("<Double-Button-1>",lambda e,val=lbl[21],bg=f[14],fg=f[14+1]:choose_color_bg(e,val,bg,fg))
        
    for i in range(22):
        lbl[i].bind("<Button-3>",lambda e,val=lbl[i]:showColor(e,val))
        
    tk.Label(lbl[2],bg='#ffffff', text='Table container').place(relx=0,rely=0.65,relwidth=1,relheight=0.35)

def layout2(frame):
    f = ['bg_lt2_f1','fg_lt2_f1','bg_lt2_f2','fg_lt2_f2',
        'bg_lt2_f1_l1','fg_lt2_f1_l1','bg_lt2_f1_b1','fg_lt2_f1_b1',
        'bg_lt2_f2_l1','fg_lt2_f2_l1','bg_lt2_f2_b1','fg_lt2_f2_b1']
    
    lbl = [tk.Label(frame) for i in range(16)]
    lbl[0] = tk.Label(frame,bg=tcl[f[0]], fg=tcl[f[1]])
    lbl[0].place(relx=0,rely=0,relwidth=0.4,relheight=1)
    lbl[1] = tk.Label(frame,bg=tcl[f[2]], fg=tcl[f[3]])
    lbl[1].place(relx=0.4,rely=0,relwidth=0.6,relheight=1)
    for i in range(2):
        lbl[i].bind("<Double-Button-1>",lambda e,val=lbl[i],bg=f[i*2],fg=f[i*2+1]:choose_color_bg(e,val,bg,fg))
    
    # frame-1
    for i in range(5):
        lbl[i+2] = tk.Button(lbl[0],bg=tcl[f[4]], fg=tcl[f[5]], text='Label',bd=0 )
        lbl[i+2].place(relx=0.01,rely=0.05+i*0.12,relwidth=0.3,relheight=0.1)
        tk.Button(lbl[0],bg='#ffffff', text='input box' ,bd=0).place(relx=0.37,rely=0.05+i*0.12,relwidth=0.5,relheight=0.1)
        lbl[i+2].bind("<Double-Button-1>",lambda e,val=lbl[i+2],bg=f[4],fg=f[5]:choose_color_bg(e,val,bg,fg))
        
    lbl[7] = tk.Button(lbl[0],bg=tcl[f[6]], fg=tcl[f[7]], text='button' ,bd=0)
    lbl[7].place(relx=0.05,rely=0.05+6*0.12,relwidth=0.4,relheight=0.1)
    lbl[8] = tk.Button(lbl[0],bg=tcl[f[6]], fg=tcl[f[7]], text='button',bd=0 )
    lbl[8].place(relx=0.57,rely=0.05+6*0.12,relwidth=0.4,relheight=0.1)
    lbl[7].bind("<Double-Button-1>",lambda e,val=lbl[7],bg=f[6],fg=f[7]:choose_color_bg(e,val,bg,fg))
    lbl[7].bind("<Double-Button-1>",lambda e,val=lbl[8],bg=f[6],fg=f[7]:choose_color_bg(e,val,bg,fg))
        
    # frame-2
    for i in range(4):
        lbl[i+7] = tk.Button(lbl[1],bg=tcl[f[8]], fg=tcl[f[9]], bd=0, text='Label' )
        lbl[i+7].place(relx=0.01,rely=0.05+i*0.12,relwidth=0.3,relheight=0.1)
        tk.Button(lbl[1],bg='#ffffff', bd=0, text='input box' ).place(relx=0.37,rely=0.05+i*0.12,relwidth=0.5,relheight=0.1)
        lbl[i+7].bind("<Double-Button-1>",lambda e,val=lbl[i+7],bg=f[8],fg=f[9]:choose_color_bg(e,val,bg,fg))
    
    lbl[14] = tk.Button(lbl[1],bg=tcl[f[10]], fg=tcl[f[11]], bd=0, text='button' )
    lbl[14].place(relx=0.15,rely=0.05+4*0.12,relwidth=0.3,relheight=0.1)
    lbl[15] = tk.Button(lbl[1],bg=tcl[f[10]], fg=tcl[f[11]], bd=0, text='button' )
    lbl[15].place(relx=0.66,rely=0.05+4*0.12,relwidth=0.3,relheight=0.1)
    lbl[14].bind("<Double-Button-1>",lambda e,val=lbl[14],bg=f[10],fg=f[11]:choose_color_bg(e,val,bg,fg))
    lbl[15].bind("<Double-Button-1>",lambda e,val=lbl[15],bg=f[10],fg=f[11]:choose_color_bg(e,val,bg,fg))
        
    for i in range(16):
        lbl[i].bind("<Button-3>",lambda e,val=lbl[i]:showColor(e,val))
        
    tk.Label(lbl[1],bg='#ffffff', text='Table container').place(relx=0,rely=0.65,relwidth=1,relheight=0.35)


def layout3(frame):
    f = ['bg_lt3_f1','fg_lt3_f1',
        'bg_lt3_f1_l1','fg_lt3_f1_l1','bg_lt3_f1_b1','fg_lt3_f1_b1']
    
    lbl = [tk.Label(frame) for i in range(7)]
    lbl[0] = tk.Label(frame,bg=tcl[f[0]], fg=tcl[f[1]])
    lbl[0].place(relx=0,rely=0,relwidth=1,relheight=0.4)
    for i in range(1):
        lbl[i].bind("<Double-Button-1>",lambda e,val=lbl[i],bg=f[i*2],fg=f[i*2+1]:choose_color_bg(e,val,bg,fg))
    
    # frame-1
    lbl[1] = tk.Button(lbl[0],text='Label',bg=tcl[f[2]], fg=tcl[f[3]], bd=0)
    lbl[1].place(relx=0.1,rely=0.01,relwidth=0.07,relheight=0.15)
    lbl[2] = tk.Button(lbl[0],text='Label',bg=tcl[f[2]], fg=tcl[f[3]], bd=0)
    lbl[2].place(relx=0.1,rely=0.2,relwidth=0.07,relheight=0.15)
    lbl[1].bind("<Double-Button-1>",lambda e,val=lbl[1],bg=f[2],fg=f[3]:choose_color_bg(e,val,bg,fg))
    lbl[2].bind("<Double-Button-1>",lambda e,val=lbl[2],bg=f[2],fg=f[3]:choose_color_bg(e,val,bg,fg))
    
    tk.Label(lbl[0],text='input box', bg='#ffffff', fg='#000000').place(relx=0.2,rely=0.01,relwidth=0.12,relheight=0.15)
    tk.Label(lbl[0],text='input box', bg='#ffffff', fg='#000000').place(relx=0.2,rely=0.2,relwidth=0.12,relheight=0.15)
    
    lbl[3] = tk.Button(lbl[0],text='Button',bg=tcl[f[4]], fg=tcl[f[5]], bd=0)
    lbl[3].place(relx=0.1,rely=0.5,relwidth=0.07,relheight=0.2)
    lbl[4] = tk.Button(lbl[0],text='Button',bg=tcl[f[4]], fg=tcl[f[5]], bd=0)
    lbl[4].place(relx=0.25,rely=0.5,relwidth=0.07,relheight=0.2)
    lbl[5] = tk.Button(lbl[0],text='Button',bg=tcl[f[4]], fg=tcl[f[5]], bd=0)
    lbl[5].place(relx=0.8,rely=0.5,relwidth=0.07,relheight=0.2)
    lbl[6] = tk.Button(lbl[0],text='Button',bg=tcl[f[4]], fg=tcl[f[5]], bd=0)
    lbl[6].place(relx=0.9,rely=0.5,relwidth=0.07,relheight=0.2)
    
    lbl[3].bind("<Double-Button-1>",lambda e,val=lbl[3],bg=f[4],fg=f[5]:choose_color_bg(e,val,bg,fg))
    lbl[4].bind("<Double-Button-1>",lambda e,val=lbl[4],bg=f[4],fg=f[5]:choose_color_bg(e,val,bg,fg))
    lbl[5].bind("<Double-Button-1>",lambda e,val=lbl[5],bg=f[4],fg=f[5]:choose_color_bg(e,val,bg,fg))
    lbl[6].bind("<Double-Button-1>",lambda e,val=lbl[6],bg=f[4],fg=f[5]:choose_color_bg(e,val,bg,fg)) 
    for i in range(6):
        lbl[i].bind("<Button-3>",lambda e,val=lbl[i]:showColor(e,val))
    tk.Label(frame,bg='#ffffff', text='Table container').place(relx=0,rely=0.4,relwidth=1,relheight=0.6)


def topLayout(top):
    f = ['bg_main1','fg_main1','bg_main2','fg_main2']
    lbl = [tk.Label(),tk.Label()]
    lbl[0] = tk.Label(top,bg=tcl[f[0]], fg=tcl[f[1]])
    lbl[0].place(relx=0,rely=0,relwidth=1,relheight=0.7)
    lbl[1] = tk.Label(top,bg=tcl[f[2]], fg=tcl[f[3]])
    lbl[1].place(relx=0,rely=0.7,relwidth=1,relheight=0.3)
    for i in range(2):
        lbl[i].bind("<Double-Button-1>",lambda e,val=lbl[i],bg=f[i*2],fg=f[i*2+1]:choose_color_bg(e,val,bg,fg))
    
    tk.Label(lbl[0],text='Text will look like',bg=tcl[f[0]], fg=tcl[f[1]], font=('',16)
        ).place(relx=0.05, rely=0.4)
    tk.Label(lbl[1],text='Text will look like',bg=tcl[f[2]], fg=tcl[f[3]], font=('',12)
        ).place(relx=0.05, rely=0.3)
    for i in range(2):
        lbl[i].bind("<Button-3>",lambda e,val=lbl[i]:showColor(e,val))
    
  
    
    
def color_change(root):
    global color_list,temp_color_list
    temp_color_list = [color for color in color_list]
    print('I am here color change')
    main_frame = tk.Frame(root)
    main_frame.place(relx=0,rely=0.172,relwidth=1,relheight=0.75)

    
    
    tk.Label(main_frame,text='Bgcolor: ').place(relx=0.37,rely=0,relheight=0.037)
    tk.Label(main_frame,text='Fgcolor: ').place(relx=0.37,rely=0.037)
    global background,foreground
    background =  tk.Entry(main_frame)
    background.place(relx=0.42,rely=0, relheight=0.037)
    foreground =  tk.Entry(main_frame)
    foreground.place(relx=0.42,rely=0.044,relheight=0.037)
    
    
    layout = tk.Frame(main_frame, bg='grey')
    layout.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=1)
    top = tk.Frame(layout, bg='blue')
    top.place(relx=0, rely=0, relwidth=1, relheight=0.3)
    topLayout(top)
    
    
    bottom = tk.Frame(layout,bg='#00aa00')
    bottom.place(relx=0,rely=0.3,relwidth=1,relheight=0.6)
    layout1(bottom)
    
    # layout select button
    tk.Button(main_frame,text='Layout-1',bg=color_list[2],command=lambda:layout1(bottom)
        ).place(relx=0.01,rely=0.01,relwidth=0.1,relheight=0.07)
    tk.Button(main_frame,text='Layout-2',bg=color_list[2],command=lambda:layout2(bottom)
        ).place(relx=0.13,rely=0.01,relwidth=0.1,relheight=0.07)
    tk.Button(main_frame,text='Layout-3',bg=color_list[2],command=lambda:layout3(bottom)
        ).place(relx=0.25,rely=0.01,relwidth=0.1,relheight=0.07)
    
    def apply():
        for key in tcl.keys():
            print(f"'{key}' : '{tcl[key]}',")
    # operation button
    tk.Button(main_frame,text='Refresh',bg=color_list[2],command=lambda:topLayout(top)
        ).place(relx=0.65,rely=0.01,relwidth=0.1,relheight=0.07)
    tk.Button(main_frame,text='Apply',bg=color_list[2],command=apply
        ).place(relx=0.77,rely=0.01,relwidth=0.1,relheight=0.07)
    tk.Button(main_frame,text='Cancel',bg=color_list[2],command=lambda:backHome(main_frame)
        ).place(relx=0.89,rely=0.01,relwidth=0.1,relheight=0.07)
    

# root = tk.Tk()
# root.geometry('1100x650+10+10')
# color_change(root)
# root.mainloop()
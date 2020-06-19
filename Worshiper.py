"""WORSHIP AND PRAISE application created by Magall George """
"""For HOLYSUM and Ministry of Holiness and Repentence"""
"""6/May 2020"""
#*************************************************
                    #IMPORTS
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
import supportA as sa
#*************************************************
#*************************************************
                #Create instance
chch = tk.Tk()
chch.title("WORSHITECH")
#bckLab = tk.Label(chch, image = sa.bg, border = 0)
#bckLab.place(x=0,y=0,relwidth=1, relheight=1)
#*************************************************
#Configuring Buttons
def Click_me1():
    action1.configure(text = "Dummy Button")
        
#***************************************************************************************************
fontstyle1 = tkFont.Font(family = 'Cambria', size = 10)

#***************************************************************************************************
        #Creating tabs for the three pages
tabcontrol = ttk.Notebook(chch)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1, text = 'SONGS')
tabcontrol.add(tab2, text = 'SCREEN')
tabcontrol.add(tab3, text = 'BIBLE')

tabcontrol.pack(expand=1, fill='both')

#*************************************************
        #Creating a container frames for page 1/tab 1
frame_1 = ttk.LabelFrame(tab1, text='')
frame_1.grid(column = 0, row = 0, padx = 1, pady = 2, sticky = tk.N)

frame_2 = ttk.LabelFrame(tab1, text='')
frame_2.grid(column = 1, row = 0, padx = 1, pady = 2,sticky = tk.N)

frame_3 = ttk.LabelFrame(tab1, text='')
frame_3.grid(column = 2, row = 0, padx = 1, pady = 2, sticky = tk.N)

        #Creating a container frames for page 2/tab 2
frame_4 = ttk.LabelFrame(tab2, text='')
frame_4.grid(column = 0, row = 0, padx = 1, pady = 2)

frame_5 = ttk.LabelFrame(tab2, text='')
frame_5.grid(column = 1, row = 0, padx = 1, pady = 2)

#*************************************************
#*************************************************
                #Configuring Buttons
def Click_me1():
    action1.configure(text = "Dummy Button")
    
#*************************************************
                #Configuring Displays
f = open('List.txt', 'r')
    
#*************************************************
                    #Page 1/ tab 1 content
title = tk.StringVar()
title_entered = ttk.Entry(frame_1, width=20, textvariable=title)
title_entered.grid(column = 0,row = 1, padx=10, pady=5)

action1 = tk.Button(frame_1,width = 15, text = "Search", command = Click_me1)
action1.grid(column=0,row=2, padx=5, pady=3)

class a():
    def on_click(self):
        scrn.delete(1.0, END)
        hit = listbox.get(listbox.curselection())
        hit = hit.rstrip()
        sn= (hit+".txt")
        with open(sn, mode = 'r') as bn:
            rj = bn.read()
            scrn.insert(tk.END, rj)
    
listbox = Listbox(frame_1, font =fontstyle1, width = 25, height=16, selectmode = SINGLE, yscrollcommand = 'TRUE') #adding a listbox
listbox.bind("<Double-1>", a.on_click)
listbox.grid(column = 0, row = 3)

for word in f:#inserting items to the listbox
    listbox.insert(END, word)
    
scrn = scrolledtext.ScrolledText(frame_2, font =fontstyle1, width = 35, height=20)#song display screen
scrn.grid(column=0, row = 0,padx = 2,pady = 2)


project = tk.Button(frame_3,width = 15, text = "Project", command = sa.p.on_click)
project.grid(column=1,row=1, padx=2, pady=10)

action4 = tk.Button(frame_3,width = 8, text ="Back", command = Click_me1)
action4.grid(column=0,row=5, padx=2, pady=10)

action5 = tk.Button(frame_3,width = 8, text ="Next", command = Click_me1)
action5.grid(column=2,row=5, padx=2, pady=10)

action6 = tk.Button(frame_3,width = 15, text = "End Show", command = Click_me1)
action6.grid(column=1,row=8, padx=2, pady=10)

bckgrnd = tk.Button(frame_3,width = 20, text ="Background", command = sa.bkg.on_click)
bckgrnd.grid(column=1,row=10, padx=2, pady=2)
                        #Page 2/ tab 2 content
style = ttk.Style(frame_4)
style.configure('lefttab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(frame_4, style='lefttab.TNotebook')
f1 = tk.Frame(notebook, width=500, height=350)
f2 = tk.Frame(notebook, width=500, height=350)
f3 = tk.Frame(notebook, width=500, height=350)
f4 = tk.Frame(notebook, width=500, height=350)
notebook.add(f1, text='      Screen Saver      ')
notebook.add(f2, text='  Communications  ')
notebook.add(f3, text='            About            ')
notebook.add(f4, text='            video            ')
notebook.pack()




#*************************************************

#*************************************************
#*************************************************
        # *************About*****************
frame_25 = ttk.LabelFrame(f3, text='')
frame_25.grid(column = 4, row = 4, padx = 1, pady = 2, sticky = 'we')

about = ttk.Label(frame_25, text = '''WORSHITECH Version 1.0.0
    Created by Magall George
        March 2020
     magallgeorge21@gmail.com ''')
about.grid(sticky = "ew")
#*************************************************

                 #Run the GUI
chch.mainloop()
#*************************************************


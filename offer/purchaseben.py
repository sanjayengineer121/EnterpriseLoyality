import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkwidgets.autocomplete import AutocompleteCombobox
import requests
from ttkbootstrap import Window, Style
import ttkbootstrap as tb
from itertools import cycle
from PIL import Image, ImageTk
import json,os


d = open('path.json')

# returns JSON object as
# a dictionary
data = json.load(d)


# Connect to the database

filepathof_database=data['filepath']
print(filepathof_database)

original_path = filepathof_database

new_path = os.path.dirname(original_path)

def sendtoparty():
    ph_no=my_entry.get()
    msg="this is a coupans code"
    attach='coupon_image5.png'
    import os
    x=os.path.abspath('coupon_image5.png')
    Api="http://127.0.0.1:8082/send_att?mobile="+ph_no+"&message="+msg+"&attach="+x
    whatsAppHitApi = requests.get(Api)
    print(whatsAppHitApi)

db_path=os.path.join(filepathof_database, "pingtowinggz.db")


def change_theme(theme_name):
    style.theme_use(theme_name)

# tb.Window(themename="solar")
root = tb.Window()
root.geometry("1050x550")  # width and height
root.resizable(FALSE,FALSE)
root.title("offers & Coupans")


navbar_frame = ttk.Frame(root, style="My.TFrame")
navbar_frame.pack(fill="x")

navbar_label = ttk.Label(navbar_frame, text="Loyality", font=("Helvetica", 16, "bold"))
navbar_label.grid(row=0, column=0, padx=10, pady=5)

button1 = tb.Button(
    navbar_frame,
    # image=img,
    text = "Coupans",
    width=20,
    compound=LEFT,
    style='INFO.Outline.TButton',
    command = sendtoparty,
    )
button1.grid(row=0, column=1, padx=10, pady=5)

button22 = tb.Button(
    navbar_frame,
    # image=img,
    text = "Monthly Target",
    width=20,
    compound=LEFT,
    style='INFO.Outline.TButton',
    command = sendtoparty,
    )
button22.grid(row=0, column=2, padx=10, pady=5)

button242 = tb.Button(
    navbar_frame,
    # image=img,
    text = "Purchased Benefit",
    width=20,
    compound=LEFT,
    style='INFO.Outline.TButton',
    command = sendtoparty,
    )
button242.grid(row=0, column=3, padx=10, pady=5)





style = Style(theme='solar')  # Set the initial theme

# Create a function to change the theme when the button is clicked
theme_options = ['flatly', 'cyborg', 'cosmo', 'darkly', 'journal', 'solar', 'superhero', 'morph', 'yeti', 'united', 'sandstone', 'pulse', 'minty', 'lumen', 'litera', 'flatly']

# Create a label to describe the theme changer
label = tb.Label(root, text="Change Theme")

# Create a dropdown menu for theme selection
theme_var = tb.StringVar()
theme_var.set(style.theme_use())  # Set the initial value to the current theme
theme_menu = tb.OptionMenu(root, theme_var, *theme_options, command=lambda x: change_theme(theme_var.get()))

# Create a button to apply the selected theme
#apply_button = tb.Button(root, width=10,text="Apply Theme",style='success.Outline.TButton', command=lambda: change_theme(theme_var.get()))

# Place the label, theme menu, and button on the right side
label.pack(side="right")
label.place(x=950,y=15)
theme_menu.pack(side="right")
theme_menu.place(x=845,y=10)
#apply_button.pack(side="right")
#apply_button.place(x=720,y=10)


font = ('arial', 14, 'bold')

lb=tb.Label(bootstyle="info",text="Target Name",font=font)
lb.place(x=100,y=100)

e = tb.Entry()
e.configure(state="success")
e.place(x=100,y=130,width=550)

font = ('arial', 14)

lb1=tb.Label(bootstyle="primary",text="Minimum Amount",font=font)
lb1.place(x=100,y=170)

font = ('arial', 14)


e1 = tb.Entry()
e1.configure(state="success")
e1.place(x=100,y=210,width=550)


lbframe=tb.Frame()

# info colored frame style
lbframe=tb.Frame(bootstyle="info",width=1050,height=50)
lbframe.place(x=0,y=270)

centered_text = "Target benifits"
label = tb.Label(lbframe, background="#3F98D7",text=centered_text, font=("Arial bold", 14), style="dark.TLabel")
label.place(relx=0.5, rely=0.5, anchor="center")


font = ('arial', 14, 'bold')

lb=tb.Label(bootstyle="info",text="Target Name",font=font)
lb.place(x=100,y=330)

emm = tb.Entry()
emm.configure(state="success")
emm.place(x=100,y=370,width=250)

font = ('arial', 14, 'bold')

lb=tb.Label(bootstyle="info",text="Start Date",font=font)
lb.place(x=100,y=410)

el = tb.Entry()
el.configure(state="success")
el.place(x=100,y=450,width=250)

font = ('arial', 14, 'bold')

lb=tb.Label(bootstyle="info",text="Expiry Date",font=font)
lb.place(x=500,y=410)

ex = tb.Entry()
ex.configure(state="success")
ex.place(x=500,y=450,width=250)



button5 = tb.Button(
    root,
    # image=img,
    text = "Create Target",
    width=20,
    compound=LEFT,
    style='success.Outline.TButton',
    command = sendtoparty,
    )
button5.place(x=100,y=500)

button6 = tb.Button(
    root,
    # image=img,
    text = "Qutt",
    width=20,
    compound=LEFT,
    style='warning.Outline.TButton',
    command = quit,
    )
button6.place(x=500,y=500)


def quit():
    quit()

con1 = sqlite3.connect(db_path)

cur1 = con1.cursor()

cur1.execute("SELECT id,name,mobile,points FROM customer_detail")

row = cur1.fetchall()




conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) as count_pet FROM customer_detail")
conn.commit()
s=cur.fetchall()

cur1 = conn.cursor()
cur1.execute("SELECT COUNT(*) as count_pet FROM customer_detail")
conn.commit()
totalamo=cur1.fetchall()


conn = sqlite3.connect(db_path)
cur = conn.cursor()

import datetime
x='{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())

cur2 = conn.cursor()
cur2.execute("SELECT SUM(points) FROM customer_detail")
conn.commit()
totalamo=cur2.fetchall()
totalamount=str(totalamo[0])[1:-2]
totalamount=1349553

mete=tb.Meter(root,bootstyle="success",
subtext="No. Of Customer",
border="2px",
interactive=True,
stripethickness=10,
amounttotal=str(s[0])[1:-2],
amountused=str(s[0])[1:-2],
metersize=150,)
mete.place(x=868,y=110)


import datetime
x='{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())


from datetime import date
today = str(date.today())
print(today)

#=================================================

conn = sqlite3.connect(db_path)
print("Connection.")


#=============================WHATSAPPP SEND BUTTON


# from tkinter import *



#app = ImageSlider(root)
root.mainloop()

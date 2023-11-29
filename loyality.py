import tkinter
import tkinter.messagebox
import customtkinter
import sqlite3
import tkinter as tk
from CTkDataVisualizingWidgets import *
from CTkTable import *
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
import tkinter.font as tkFont
import tkchart,os
from CTkMenuBar import *
import awesometkinter as atk
import json
from tkinter import messagebox

customtkinter.set_appearance_mode("System")    # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# Get the directory of the current script
script_directory = os.path.dirname(__file__)

# Specify the relative path to the database file

database_path=script_directory+"\database"
db_file_path = os.path.join(database_path, "pingtowinggz.db")

tier = ["filepath"]
number=[database_path]

db_file_path={tier: sales for tier, sales in zip(tier, number)}

with open('database\path.json', 'w') as f:
    json.dump(db_file_path, f, indent=4)

import shutil

source_path = database_path+'/path.json'
destination_path = script_directory+'/customerdet'
destination_path1 = script_directory+'/cusomrepo'
destination_path2 = script_directory+'/month'
destination_path3 = script_directory+'/aboutinfo'
destination_path4 = script_directory+'/offer'

shutil.copy(source_path, destination_path)
shutil.copy(source_path, destination_path1)
shutil.copy(source_path, destination_path2)
shutil.copy(source_path, destination_path3)
shutil.copy(source_path, destination_path4)

print(f"File copied from {source_path}")


d = open('database\path.json')

# returns JSON object as
# a dictionary
data = json.load(d)


# Connect to the database

filepathof_database=data['filepath']
print(filepathof_database)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("S K Loyality")
        self.attributes("-fullscreen", True)
        #self.geometry(f"{1100}x{580}")

        menu = CTkTitleMenu(self)
        button_1 = menu.add_cascade("Home")
        button_2 = menu.add_cascade("Reports & Info")
        button_3 = menu.add_cascade("Settings")
        button_4 = menu.add_cascade("About")
        button_5 = menu.add_cascade("QUIT")

        dropdown1 = CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="Open", command=lambda: print("Open"))
        dropdown1.add_option(option="Save")

        dropdown1.add_separator()

        sub_menu = dropdown1.add_submenu("Export As")
        sub_menu.add_option(option=".TXT")
        sub_menu.add_option(option=".PDF")

        dropdown2 = CustomDropdownMenu(widget=button_2)
        dropdown2.add_option(option="CUSTOMER INFO",command=self.genqr)
        dropdown2.add_option(option="MONTH REPORT",command=self.Paybyqr)
        dropdown2.add_option(option="CUSTOM REPO",command=self.scanqr)
        dropdown2.add_option(option="COUPONS&OFFERS",command=self.crnotes)

        dropdown3 = CustomDropdownMenu(widget=button_3)
        dropdown3.add_option(option="Preferences")
        dropdown3.add_option(option="Update")

        dropdown4 = CustomDropdownMenu(widget=button_4)
        dropdown4.add_option(option="About",command=self.aboutinfo)

        dropdown5 = CustomDropdownMenu(widget=button_5)
        dropdown5.add_option(option="QUIT",command=self.quit_application)


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # menu = CTkMenuBar(self)
        # button_1 = menu.add_cascade("File")

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", font=customtkinter.CTkFont("Courier Now",25))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="CUSTOMER INFO",command=self.genqr,font=customtkinter.CTkFont("Bodoni MT Black",14))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="MONTH REPORT",command=self.Paybyqr,font=customtkinter.CTkFont("Bodoni MT Black",14))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="CUSTOM REPO",command=self.scanqr,font=customtkinter.CTkFont("Bodoni MT Black",16))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="COUPONS&OFFERS",command=self.crnotes,font=customtkinter.CTkFont("Miya Mine",16))
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Mobile No.")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent",text="send", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        DB_NAME="pingtowinggz.db"

        #-----------------------------------------Last 7 Days
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = 'SELECT strftime("%Y-%m-%d", created_on) AS sale_date, SUM(bill_amount) AS total_sales FROM customer_point_transaction WHERE created_on >= date("2023-09-06 11:01:42", "-30 days") GROUP BY sale_date ORDER BY sale_date'
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        sales_data=data
        month = [sale[0] for sale in sales_data]
        total_sales = [sale[1] for sale in sales_data]
                # print(data)
        # month_sales = {sales: sales for sales in zip(total_sales)}

        print(total_sales)

        #create line chart

        chart_1 = tkchart.LineChart(master=self
                                    ,chart_fg='#101010'
                                    ,horizontal_bar_size=10 ,horizontal_bar_fg="#444444"
                                    ,vertical_bar_size=10 ,vertical_bar_fg="#444444"
                                    ,sections=True ,sections_fg="#444444" ,sections_count=10
                                    ,max_value=max(total_sales,default=0)+max(total_sales,default=0)*10/100
                                    ,values_labels=True ,values_labels_count=10
                                    ,chart_line_len=50
                                    ,text_color='#00ff00' ,font=('arial',10,'bold')
                                    ,left_space=10 ,right_space=10 ,bottom_space=40 ,top_space=40
                                    ,x_space=00 ,y_space=10)

        chart_1.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #create line for line chart
        line_1 = tkchart.Line(master=chart_1 ,height=4 ,color='#ffffff')

        #display values using loop


        # value = data

        values=total_sales

        line_1.configure(line_highlight=1,line_highlight_color="#ffffff" ,line_highlight_size=10)

        chart_1.display(line=line_1 ,values=values)

        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("ADD CUSTOMER")
        self.tabview.add("ADD POINT")
        self.tabview.add("REDEEM POINT")
        self.tabview.tab("ADD CUSTOMER").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("ADD POINT").grid_columnconfigure(0, weight=1)
        self.tabview.tab("REDEEM POINT").grid_columnconfigure(0, weight=1)


        self.optionmenu_1 = customtkinter.CTkEntry(self.tabview.tab("ADD CUSTOMER"),placeholder_text="CUS NAME")

        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.combobox_1 = customtkinter.CTkEntry(self.tabview.tab("ADD CUSTOMER"),placeholder_text="PH-No.")
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        #self.string_input_button = customtkinter.CTkEntry(self.tabview.tab("ADD CUSTOMER"),placeholder_text="BIRTHDAY")
        #self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.cal = DateEntry(self.tabview.tab("ADD CUSTOMER"),width=20,placeholder_text="BIRTHDAY")
        self.cal.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.string_input_button1 = DateEntry(self.tabview.tab("ADD CUSTOMER"),placeholder_text="ANIVERSARY",width=20,text="aniversasry")
        self.string_input_button1.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.string_input_button2 = customtkinter.CTkButton(self.tabview.tab("ADD CUSTOMER"),text="ADD CUSTOMER",command=self.addcustomer)
        self.string_input_button2.grid(row=4, column=0, padx=20, pady=(10, 10))


        self.name = customtkinter.CTkEntry(self.tabview.tab("ADD POINT"), placeholder_text="Customer Name")
        self.name.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.Mobile = customtkinter.CTkEntry(self.tabview.tab("ADD POINT"), placeholder_text="Mobile No")
        self.Mobile.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.Amount = customtkinter.CTkEntry(self.tabview.tab("ADD POINT"), placeholder_text="Amonut")
        self.Amount.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.buttonofpoint = customtkinter.CTkButton(self.tabview.tab("ADD POINT"),text="ADD POINTS",command=self.addpoints)
        self.buttonofpoint.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.customer = customtkinter.CTkEntry(self.tabview.tab("REDEEM POINT"), placeholder_text="Customer Name")
        self.customer.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.phoneno = customtkinter.CTkEntry(self.tabview.tab("REDEEM POINT"), placeholder_text="Mobile No")
        self.phoneno.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.pointofredeem = customtkinter.CTkEntry(self.tabview.tab("REDEEM POINT"), placeholder_text="Points")
        self.pointofredeem.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.buttonofpoint = customtkinter.CTkButton(self.tabview.tab("REDEEM POINT"),text="REDEEM POINTS",command=self.redeempoint)
        self.buttonofpoint.grid(row=3, column=0, padx=20, pady=(10, 10))

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)



        DB_NAME="pingtowinggz.db"

        #-----------------------------------------Last 7 Days
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        query = '''SELECT tier, COUNT(*) AS customer_count
            FROM (
                SELECT mobile_number,
                    CASE
                        WHEN SUM(CASE WHEN point_type = 1 THEN point_add ELSE 0 END) BETWEEN 0 AND 500 THEN 'Silver'
                        WHEN SUM(CASE WHEN point_type = 1 THEN point_add ELSE 0 END) BETWEEN 501 AND 1000 THEN 'Gold'
                        WHEN SUM(CASE WHEN point_type = 1 THEN point_add ELSE 0 END) BETWEEN 1001 AND 1500 THEN 'Platinum'
                        WHEN SUM(CASE WHEN point_type = 1 THEN point_add ELSE 0 END) BETWEEN 1501 AND 2000 THEN 'Rhodonium'
                        WHEN SUM(CASE WHEN point_type = 1 THEN point_add ELSE 0 END) > 2000 THEN 'Uranium'
                        ELSE 'Uncategorized'
                    END AS tier
                FROM customer_point_transaction
                WHERE created_on >= date("now", "-12 months")
                GROUP BY mobile_number
            )GROUP BY tier;'''

        import datetime,json

        # Get the current date
        current_date = datetime.date.today()

        # Check if it's the 1st of the month
        if 1 <= current_date.day <= 7:

            cursor.execute(query)

            data = cursor.fetchall()
            conn.close()

            tier = [sale[0] for sale in data]
            number=[sale[1] for sale in data]

            tier_calc={tier: sales for tier, sales in zip(tier, number)}
            print(tier_calc)


            with open('data.json', 'w') as f:
                json.dump(tier_calc, f, indent=4)



        #Opening JSON file

        f = open('data.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)


        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Tier")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # f=atk.Frame3d(self)
        self.lb = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Silver")
        self.lb.grid(row=1, column=1,pady=5, padx=5)

        # self.lb_ = customtkinter.CTkLabel(master=self.radiobutton_frame, text=data['Silver'])
        self.lb_=customtkinter.CTkLabel(self.radiobutton_frame, text=data['Silver'])
        self.lb_.grid(row=1, column=2,pady=5, padx=5)

        self.lb1 = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Gold")
        self.lb1.grid(row=2, column=1, pady=5, padx=5)

        self.lb1_ = customtkinter.CTkLabel(master=self.radiobutton_frame, text=data['Gold'])
        self.lb1_.grid(row=2, column=2, pady=5, padx=5)

        self.lb2 = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Platinum")
        self.lb2.grid(row=3, column=1, pady=5, padx=5)

        self.lb2_ = customtkinter.CTkLabel(master=self.radiobutton_frame, text=data['Platinum'])
        self.lb2_.grid(row=3, column=2, pady=5, padx=5)

        self.lb3 = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Rhodonium")
        self.lb3.grid(row=4, column=1, pady=5, padx=5)

        self.lb3_ = customtkinter.CTkLabel(master=self.radiobutton_frame, text=data['Rhodonium'])
        self.lb3_.grid(row=4, column=2, pady=5, padx=5)

        self.lb4 = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Uranium")
        self.lb4.grid(row=5, column=1, pady=5, padx=5)

        self.lb4_ = customtkinter.CTkLabel(master=self.radiobutton_frame, text=data['Uranium'])
        self.lb4_.grid(row=5, column=2, pady=5, padx=5)

        f.close()


        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        DB_NAME="pingtowinggz.db"

#-----------------------------------------Last 7 Days
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        query = 'SELECT strftime("%Y-%m", created_on) AS sale_month, SUM(bill_amount) AS total_sales FROM customer_point_transaction WHERE created_on >= date("now", "-11 months") GROUP BY sale_month ORDER BY sale_month'

        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        sales_data=data
        month1 = [sale[0] for sale in sales_data]
        total_sales = [round(sale[1]/100000,2) for sale in sales_data]

        # print(month)
        # print(total_sales)
        # ctk.set_appearance_mode("dark") 100000

        date_list = month1

        month = [date[2:] for date in date_list]

        # print(month)

        value = {}

        month_sales = {month: sales for month, sales in zip(month, total_sales)}

        # # Merge the 'month_sales' dictionary into the 'value' dictionary
        value.update(month_sales)

        # Now the 'value' dictionary includes 'month name': 'total sales' in order-wise
        # print(value)

        CTkChart(self, value, corner_radius=20, fg_color="#1a1a1a", stat_color="#1D6FFF", chart_fg_color="#1a1a1a",
        show_indicators=(True, True), stat_info_show=(True, True), chart_arrow="none", border_width=2,
        border_color="white", indicator_line_color="white", indicator_text_color="white", stat_width=28,
        stat_title_color="white", chart_axis_width=3).grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Top Customers")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []


        DB_NAME="pingtowinggz.db"

        #-----------------------------------------Last 7 Days
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = 'select mobile,points FROM customer_detail ORDER by points DESC LIMIT 10'
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        values=[('Mobile No.', 'Points')]

        for i in data:
            values.append(i)

        value=values

        for i in range(10):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            table = CTkTable(master=self, row=11, column=2, values=value,header_color='blue')
            table.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

            # switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(table)



        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")


        self.scaling_optionemenu.set("100%")

        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def quit_application(self):
        # Ask for confirmation before quitting
        confirmation = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if confirmation:
            # Destroy the Tkinter root window
            self.destroy()


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def aboutinfo(self):
        import os

        os.system("python aboutinfo/about")


    #==========================CALLING GENERATION OF QR CODE

    def genqr(self):
        #dialog = customtkinter.CTkInputDialog(text="ENTER UNIT HERE.:", title="UNITS")
        #print("Number is:", dialog.get_input())
        import os
        from subprocess import call
        call(["python", "customerdet\customerdet"])
        #exec(open('test.py').read())
        #from test import my_generate
        #Popen('scandocument.py')
        #import scandocument

#==========================GET PAYMENT FROM QR CODE

    def Paybyqr(self):
        from subprocess import call
        call(["python", "month/monthrepo"])

    #==========================SCAN DOWNLOADED QR CODE

    def scanqr(self):
        from subprocess import call
        call(["python", "cusomrepo/customrepo"])

    def crnotes(self):
        from subprocess import call
        call(["python", "offer/offers"])

    def addcustomer(self):
        name=self.optionmenu_1.get()
        mobile=self.combobox_1.get()
        dob=self.cal.get_date()
        y=self.string_input_button1.get_date()


        print(name)
        print(mobile)
        print(dob)
        print(y)

        x=name.upper()+" data has been added to Loyality database"

        tkinter.messagebox.showinfo(name.upper(), x)

    def addpoints(self):
        nameofc=self.name.get()
        phno=self.Mobile.get()
        amount=self.Amount.get()


        print(nameofc)
        print(phno)
        print(amount)

        pointredeem=int(amount)//100

        pointadd=color.BOLD +str(pointredeem) + color.END


        x=str(pointredeem).upper()+" has been added to "+nameofc.upper()+" account"

        tkinter.messagebox.showinfo("POINT ADD", x)

    def redeempoint(self):
        name=self.customer.get()
        mobile=self.phoneno.get()
        pointredeem=self.pointofredeem.get()


        print(name)
        print(mobile)
        print(pointredeem)

        x=pointredeem.upper()+" point has been redeemed from "+name.upper()+" account"

        tkinter.messagebox.showinfo(name,x )


if __name__ == "__main__":
    app = App()
    app.mainloop()

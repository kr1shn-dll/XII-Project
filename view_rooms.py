from tkinter import *
from tkinter import ttk
import mysql.connector as sql


connection = sql.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 database="Continental",
                                 auth_plugin='mysql_native_password')

cursor = connection.cursor()

window = Tk()

bg = PhotoImage(file=r"Resources\Home\bg.png")
logo = PhotoImage(file=r"Resources\Home\logo.png")
frame_bg = PhotoImage(file=r"Resources\Mcustomer\frame_bg.png")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("CONTINENTAL HOTEL | ROOM INFORMATION ")
window.iconphoto(True,logo)

canvas = Canvas(window,bg = "#FFFFFF",height = 720,width = 1280,highlightthickness = 0)
canvas.place(x = 0, y = 0)

canvas.create_image(640,360,image=bg)
canvas.create_text(47,0,anchor="nw",text="THE CONTINENTAL",fill="#950B3C",font=("Cinzel Decorative Black", 106 * -1))

menu = Frame(window,bg="#CDA84C")
menu.pack_propagate(False)
menu.configure(width=1280,height=100)
menu.pack(pady=135)

def switch(label,frame):
    all_label['bg'] = "#CDA84C"
    occupied_label['bg'] = "#CDA84C"
    available_label['bg'] = "#CDA84C"
    label['bg'] = "#950B3C"

    all_page.destroy()
    occupied_page.destroy()
    available_page.destroy()
    frame()

all_button = Button(menu,text="ALL ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                    fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                    command = lambda: switch(all_label,all_switch))
all_button.place(x=20,y=0,width=400)
all_label = Label(menu,bg="#950B3C")
all_label.place(x=20,y=90,width=400,height=3)

occupied_button = Button(menu,text="OCCUPIED ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                     fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                     command = lambda: switch(occupied_label,occupied_switch))
occupied_button.place(x=440,y=0,width=400)
occupied_label = Label(menu,bg="#CDA84C")
occupied_label.place(x=440,y=90,width=400,height=3)

available_button = Button(menu,text="AVAILABLE ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                       fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                       command = lambda: switch(available_label,available_switch))
available_button.place(x=860,y=0,width=400)
available_label = Label(menu,bg="#CDA84C")
available_label.place(x=860,y=90,width=400,height=3)

main = Frame(window,bg="#CDA84C")
main.configure(width=1280,height=470)
main.place(x=0,y=250)

def all_switch():
    global all_page
    all_page = Frame(main,bg="#CDA84C")
    all_page.configure(width=1280,height=470)
    all_page.place(x=0,y=0)
    canvas = Canvas(all_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    table = ttk.Treeview(all_page,columns=("rid","name","floor","ac","cost","occupant","checkout"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST PER NIGHT(₹)")
    table.heading("occupant",text="OCCUPANT")
    table.heading("checkout",text=" CHECKOUT")
    table.place(x=40,y=40,height=395,width=1200)
    cursor.execute("select * from rooms;")
    for i in cursor.fetchall():
        table.insert(parent="",index=END,values=i)

all_switch()

def occupied_switch():
    global occupied_page
    occupied_page = Frame(main,bg="#CDA84C")
    occupied_page.configure(width=1280,height=470)
    occupied_page.place(x=0,y=0)
    canvas = Canvas(occupied_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    table = ttk.Treeview(occupied_page,columns=("rid","name","floor","ac","cost","occupant","checkout"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST PER NIGHT(₹)")
    table.heading("occupant",text="OCCUPANT")
    table.heading("checkout",text=" CHECKOUT")
    table.place(x=40,y=40,height=395,width=1200)
    cursor.execute("select * from rooms where not occupant = 'N/A' and not checkout = 'N/A';")
    for i in cursor.fetchall():
        table.insert(parent="",index=END,values=i)
occupied_switch()
occupied_page.destroy()

def available_switch():
    global available_page
    available_page = Frame(main,bg="#CDA84C")
    available_page.configure(width=1280,height=470)
    available_page.place(x=0,y=0)
    canvas = Canvas(available_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    table = ttk.Treeview(available_page,columns=("rid","name","floor","ac","cost","occupant","checkout"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST")
    table.heading("occupant",text="OCCUPANT")
    table.heading("checkout",text=" CHECKOUT")
    cursor.execute("select * from rooms where occupant = 'N/A' and checkout = 'N/A';")
    table.place(x=40,y=40,height=395,width=1200)
    for i in cursor.fetchall():
        table.insert(parent="",index=END,values=i)
available_switch()
available_page.destroy()

window.resizable(False,False)
window.mainloop()
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
    table = ttk.Treeview(all_page,columns=("rid","name","floor","ac","cost","occupant"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST PER NIGHT(₹)")
    table.heading("occupant",text="OCCUPANT")
    table.pack()
    data = [("001","A123","12","AC",2000,"NULL"),
            ("002","B062","06","NON-AC",300,"NULL"),
            ("003","A223","22","AC",6000,"NULL")]
    for i in data:
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
    canvas.create_text(47,0,anchor="nw",text="OCCUPIED ROOMS PAGE",fill="#950B3C",font=("Cascadia Code SemiBold",32))
    table = ttk.Treeview(occupied_page,columns=("rid","name","floor","ac","cost","occupant"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST PER NIGHT(₹)")
    table.heading("occupant",text="OCCUPANT")
    table.pack()
    data = [("001","A123","12","AC",2000,"NULL"),
            ("002","B062","06","NON-AC",300,"NULL"),
            ("003","A223","22","AC",6000,"NULL")]
    for i in data:
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
    canvas.create_text(47,0,anchor="nw",text="AVAILABLE ROOMS PAGE",fill="#950B3C",font=("Cascadia Code SemiBold",32))
    table = ttk.Treeview(available_page,columns=("rid","name","floor","ac","cost","occupant"),show="headings")
    table.heading("rid",text="ROOM ID")
    table.heading("name",text="ROOM NAME")
    table.heading("floor",text="FLOOR")
    table.heading("ac",text="AC/NON-AC")
    table.heading("cost",text="ROOM COST PER NIGHT(₹)")
    table.heading("occupant",text="OCCUPANT")
    table.pack()
    data = [("001","A123","12","AC",2000,"NULL"),
            ("002","B062","06","NON-AC",300,"NULL"),
            ("003","A223","22","AC",6000,"NULL")]
    for i in data:
        table.insert(parent="",index=END,values=i)
available_switch()
available_page.destroy()

window.resizable(False,False)
window.mainloop()
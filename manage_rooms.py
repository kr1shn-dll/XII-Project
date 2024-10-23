from tkinter import *
from tkinter import messagebox
import mysql.connector as sql


connection = sql.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 database="Continental",
                                 auth_plugin='mysql_native_password')

cursor = connection.cursor()

window = Tk()

def add_submit(rid,name,floor,ac,cost):
    a = rid.get()
    b = name.get()
    c = floor.get()
    d = ac.get()
    e = cost.get()
    try:
       cursor.execute(f"insert into rooms values('{a}','{b}','{c}','{d}','{e}','N/A','N/A');")
       connection.commit()
    except:
        messagebox.showerror(title="STATUS",message="RID already in use")
    else:
        messagebox.showinfo(title="STATUS",message="Room Added successfuly")
    finally:
        add_page.destroy()
        add_switch()

def remove_submit(name):
    a = name.get()
    cursor.execute("select name,rid from rooms;")
    for i in cursor.fetchall():
        if i[0] == a:
            b = i[1]
            break
    answer = messagebox.askyesno(title="STATUS",message="Are you sure you want to remove occupant")
    if answer:
       cursor.execute(f"update rooms set occupant = 'N/A',checkout = 'N/A' where rid = {b};")
       cursor.execute(f"update customers set room = 'N/A' where room = '{a}'")
       connection.commit()
       messagebox.showinfo(title="STATUS",message="Room cleared successfully")
       remove_page.destroy() 
       remove_switch()
 
def book_submit(customer,room,checkout):
    a = customer.get()
    b = room.get()
    c = checkout.get()
    cursor.execute("select name,room from customers;")
    V1 = bool
    V2 = bool
    for i in cursor.fetchall():
        if a == i[0]:
            if i[1] == "N/A":
                V1 = True
                break
            else:
                V1 = False
    cursor.execute("select name,occupant,checkout from rooms;")
    for i in cursor.fetchall():
        if b == i[0] and i[1] == "N/A" and i[2] == "N/A":
            V2 = True
            break   
        else:
            V2 = False
    if V1 and V2:
            cursor.execute(f"update rooms set occupant = '{a}', checkout ='{c}' where name = '{b}';")
            cursor.execute(f"update customers set room  = '{b}' where name = '{a}'")
            connection.commit()
            messagebox.showinfo(title="STATUS",message="ROOM BOOKED SUCCESSFULLY")
    elif not V1:
        messagebox.showerror(title="STATUS",message="Customer already in a room ")
    elif not V2:
        messagebox.showerror(title="STATUS",message="Room already occupied")
    book_page.destroy()
    book_switch()

bg = PhotoImage(file=r"Resources\Home\bg.png")
logo = PhotoImage(file=r"Resources\Mcustomer\logo.png")
arrow = PhotoImage(file=r"Resources\Mcustomer\arrow.png")
frame_bg = PhotoImage(file=r"Resources\Mcustomer\frame_bg.png")
submitButton = PhotoImage(file=r"Resources\Mcustomer\submit_button.png") 
removeButton = PhotoImage(file=r"Resources\Mcustomer\remove_button.png")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("CONTINENTAL HOTEL | MANAGE ROOMS ")
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
    add_label['bg'] = "#CDA84C"
    remove_label['bg'] = "#CDA84C"
    book_label['bg'] = "#CDA84C"
    label['bg'] = "#950B3C"

    add_page.destroy()
    remove_page.destroy()
    book_page.destroy()
    frame()

add_button = Button(menu,text="ADD ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                    fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                    command = lambda: switch(add_label,add_switch))
add_button.place(x=20,y=0,width=400)
add_label = Label(menu,bg="#950B3C")
add_label.place(x=20,y=90,width=400,height=3)

remove_button = Button(menu,text="CLEAR ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                     fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                     command = lambda: switch(remove_label,remove_switch))
remove_button.place(x=440,y=0,width=400)
remove_label = Label(menu,bg="#CDA84C")
remove_label.place(x=440,y=90,width=400,height=3)

book_button = Button(menu,text="BOOK ROOMS",font=("Cascadia Code SemiBold",32),bd=0,
                       fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                       command = lambda: switch(book_label,book_switch))
book_button.place(x=860,y=0,width=400)
book_label = Label(menu,bg="#CDA84C")
book_label.place(x=860,y=90,width=400,height=3)

main = Frame(window,bg="#CDA84C")
main.configure(width=1280,height=470)
main.place(x=0,y=250)

def add_switch():
    global add_page
    add_page = Frame(main,bg="#CDA84C")
    add_page.configure(width=1280,height=470)
    add_page.place(x=0,y=0)
    canvas = Canvas(add_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    canvas.create_image(1032.0,151.0,image=logo)
    canvas.create_text(36.0,42.0,anchor="nw",text="ROOM ID",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,125.0,anchor="nw",text="ROOM NAME",fill="#000000",font=("Roboto Slab", 39 * -1))
    canvas.create_text(36.0,208.0,anchor="nw",text="FLOOR",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,291.0,anchor="nw",text="AC/NON-AC",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,374.0,anchor="nw",text="COST p/n",fill="#000000",font=("Roboto Slab", 40 * -1))
    rid = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    rid.place(x=290.0,y=42.0,width=459.0,height=53.0)
    cursor.execute("select MAX(RID) from rooms")
    data = cursor.fetchall()
    rid.insert(0,data[0][0]+1)
    name = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    name.place(x=290.0,y=127.0,width=459.0,height=53.0)
    floor = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    floor.place(x=290.0,y=212.0,width=459.0,height=53.0)
    ac = StringVar()
    ac.set("AC")
    OptionMenu(add_page,ac,"AC","NON-AC").place(x=290.0,y=297,width=459.0,height=53.0)
    cost = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    cost.place(x=290.0,y=382,width=459.0,height=53.0)
    Button(add_page,image=submitButton,borderwidth=0,highlightthickness=0,
                           command=lambda: add_submit(rid,name,floor,ac,cost)).place(x=836.0,y=289.0,width=391.0,height=113.0)

add_switch()

def remove_switch():
    global remove_page
    remove_page = Frame(main,bg="#CDA84C")
    remove_page.configure(width=1280,height=470)
    remove_page.place(x=0,y=0)
    canvas = Canvas(remove_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    canvas.create_image(1032.0,151.0,image=logo)
    canvas.create_text(36.0,125.0,anchor="nw",text="SELECT WHICH ROOM\nTO CLEAR/\nREMOVE OCCUPANT FROM",fill="#000000",font=("Roboto Slab", 40 * -1))
    name = StringVar()
    rooms = []
    cursor.execute("select name from rooms;")
    for i in cursor.fetchall():
        rooms.append(i[0])
    OptionMenu(remove_page,name,*rooms).place(x=290.0,y=42.0,width=459.0,height=53.0)
    Button(remove_page,image=removeButton,borderwidth=0,highlightthickness=0,relief="flat",
           command=lambda: remove_submit(name)).place(x=836.0,y=289.0,width=391.0,height=113.0)
remove_switch()
remove_page.destroy()

def book_switch():
    global book_page
    book_page = Frame(main,bg="#CDA84C")
    book_page.configure(width=1280,height=470)
    book_page.place(x=0,y=0)
    canvas = Canvas(book_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    canvas.create_image(1032.0,151.0,image=logo)
    canvas.create_image(520.0,190.0,image=arrow)
    canvas.create_text(36.0,42.0,anchor="nw",text="CUSTOMER",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,291.0,anchor="nw",text="ROOM",fill="#000000",font=("Roboto Slab", 39 * -1))
    canvas.create_text(36.0,374.0,anchor="nw",text="Checkout",fill="#000000",font=("Roboto Slab", 40 * -1))
    customer = StringVar()
    customers = []
    room = StringVar()
    rooms = []
    cursor.execute("select name from customers;")
    for i in cursor.fetchall():
        customers.append(i[0])
    cursor.execute("select name from rooms;")
    for i in cursor.fetchall():
        rooms.append(i[0])
    OptionMenu(book_page,customer,*customers).place(x=290.0,y=42.0,width=459.0,height=53.0)
    OptionMenu(book_page,room,*rooms).place(x=290.0,y=297,width=459.0,height=53.0)
    checkout = Entry(book_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    checkout.place(x=290.0,y=382,width=459.0,height=53.0)
    Button(book_page,image=submitButton,borderwidth=0,highlightthickness=0,
           command=lambda: book_submit(customer,room,checkout),relief="flat").place(x=836.0,y=289.0,width=391.0,height=113.0)

book_switch()
book_page.destroy()


window.resizable(False,False)
window.mainloop()
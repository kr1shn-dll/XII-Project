from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

connection = sql.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 database="Continental",
                                 auth_plugin='mysql_native_password')
cursor = connection.cursor()

def add_submit(uid,name,phone,email,address):
    a = int(uid.get())
    b = name.get()
    c = str(phone.get())
    d = email.get()
    e = address.get()
    try:
        cursor.execute(f"INSERT INTO customers VALUES('{a}','{b}','{c}','{d}','{e}','N/A');")
        connection.commit()
    except:
        messagebox.showerror(title="STATUS",message="UID already in use")
    else:
        messagebox.showinfo(title="STATUS",message="CUSTOMER ADDED SUCCESFULLY")
    finally:
        add_page.destroy()
        add_switch()

def edit_submit(uid,name,phone,email,address):
    a = uid.get()
    b = name.get()
    c = phone.get()
    d = email.get()
    e = address.get()
    answer = messagebox.askyesno(title="CONFIRM CHANGES",message="ARE YOU SURE YOU WANT TO EDIT INFO?")
    if answer:
        cursor.execute(f"update customers set Name = '{b}', Phone = {c}, Email='{d}',Address='{e}' WHERE UID = '{a}';")
        connection.commit()
        messagebox.showinfo(title="STATUS",message="CUSTOMER EDITED SUCCESFULLY")
        edit_page.destroy()
        edit_switch()
    
def remove_submit(name):
    answer = messagebox.askyesno(title="CONFIRM CHANGES",message="ARE YOU SURE YOU WANT TO DELETE CUSTOMER?")
    a = name.get()
    if answer:
        cursor.execute(f"delete from customers where name = '{a}';")
        connection.commit()
        messagebox.showinfo(title="STATUS",message="CUSTOMER DELETED  SUCCESFULLY")
        remove_page.destroy()
        remove_switch()


window = Tk()

bg = PhotoImage(file=r"Resources\Home\bg.png")
logo = PhotoImage(file=r"Resources\Mcustomer\logo.png")
frame_bg = PhotoImage(file=r"Resources\Mcustomer\frame_bg.png")
submitButton = PhotoImage(file=r"Resources\Mcustomer\submit_button.png") 
removeButton = PhotoImage(file=r"Resources\Mcustomer\remove_button.png")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("CONTINENTAL HOTEL | MANAGE CUSTOMERS ")
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
    edit_label['bg'] = "#CDA84C"
    remove_label['bg'] = "#CDA84C"
    label['bg'] = "#950B3C"

    add_page.destroy()
    edit_page.destroy()
    remove_page.destroy()
    frame()

add_button = Button(menu,text="ADD CUSTOMERS",font=("Cascadia Code SemiBold",32),bd=0,
                    fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                    command = lambda: switch(add_label,add_switch))
add_button.place(x=20,y=0,width=400)
add_label = Label(menu,bg="#950B3C")
add_label.place(x=20,y=90,width=400,height=3)

edit_button = Button(menu,text="EDIT CUSTOMERS",font=("Cascadia Code SemiBold",32),bd=0,
                     fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                     command = lambda: switch(edit_label,edit_switch))
edit_button.place(x=440,y=0,width=400)
edit_label = Label(menu,bg="#CDA84C")
edit_label.place(x=440,y=90,width=400,height=3)

remove_button = Button(menu,text="REMOVE CUSTOMERS",font=("Cascadia Code SemiBold",32),bd=0,
                       fg="#950B3C",activeforeground="#950B3C",bg="#CDA84C",activebackground="#CDA84C",
                       command = lambda: switch(remove_label,remove_switch))
remove_button.place(x=860,y=0,width=400)
remove_label = Label(menu,bg="#CDA84C")
remove_label.place(x=860,y=90,width=400,height=3)

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
    canvas.create_text(36.0,42.0,anchor="nw",text="UNIQUE ID",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,125.0,anchor="nw",text="FULL NAME",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,208.0,anchor="nw",text="PHONE NO.",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,291.0,anchor="nw",text="EMAIL ADD.",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,374.0,anchor="nw",text="ADDRESS",fill="#000000",font=("Roboto Slab", 40 * -1))
    uid = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    uid.place(x=290.0,y=42.0,width=459.0,height=53.0)
    cursor.execute("select MAX(UID) from customers")
    data = cursor.fetchall()
    uid.insert(0,data[0][0]+1)
    name = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    name.place(x=290.0,y=127.0,width=459.0,height=53.0)
    phone = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    phone.place(x=290.0,y=212.0,width=459.0,height=53.0)
    email = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    email.place(x=290.0,y=297,width=459.0,height=53.0)
    address = Entry(add_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    address.place(x=290.0,y=382,width=459.0,height=53.0)
    Button(add_page,image=submitButton,borderwidth=0,highlightthickness=0,
           command=lambda: add_submit(uid,name,phone,email,address),relief="flat").place(x=836.0,y=289.0,
                                                                               width=391.0,height=113.0)

add_switch()

def edit_switch():
    global edit_page
    edit_page = Frame(main,bg="#CDA84C")
    edit_page.configure(width=1280,height=470)
    edit_page.place(x=0,y=0)
    canvas = Canvas(edit_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    canvas.create_image(1032.0,151.0,image=logo)
    canvas.create_text(36.0,42.0,anchor="nw",text="UNIQUE ID",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,125.0,anchor="nw",text="FULL NAME",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,208.0,anchor="nw",text="PHONE NO.",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,291.0,anchor="nw",text="EMAIL ADD.",fill="#000000",font=("Roboto Slab", 40 * -1))
    canvas.create_text(36.0,374.0,anchor="nw",text="ADDRESS",fill="#000000",font=("Roboto Slab", 40 * -1))
    uid = StringVar()
    cursor.execute("select * from customers;")
    data =  cursor.fetchall()
    customers = []
    for i in data:
        customers.append(i[0])
    def select(uid):
        name.delete(0,END)
        phone.delete(0,END)
        email.delete(0,END)
        address.delete(0,END)
        for i in data:
            if i[0] == uid:
                name.insert(0,i[1])
                phone.insert(0,i[2])
                email.insert(0,i[3])
                address.insert(0,i[4])

    OptionMenu(edit_page,uid,*customers,command= lambda uid: select(uid) ).place(x=290.0,y=42.0,width=459.0,height=53.0)
    name = Entry(edit_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    name.place(x=290.0,y=127.0,width=459.0,height=53.0)
    phone = Entry(edit_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    phone.place(x=290.0,y=212.0,width=459.0,height=53.0)
    email = Entry(edit_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    email.place(x=290.0,y=297,width=459.0,height=53.0)
    address = Entry(edit_page,bd=0,bg="#FFFFFF",fg="#000000",highlightthickness=0,font=("Calibri",40))
    address.place(x=290.0,y=382,width=459.0,height=53.0)
    Button(edit_page,image=submitButton,borderwidth=0,highlightthickness=0,
                           command=lambda: edit_submit(uid,name,phone,email,address),relief="flat").place(x=836.0,y=289.0,
                                                                                               width=391.0,height=113.0)
edit_switch()
edit_page.destroy()

def remove_switch():
    global remove_page
    remove_page = Frame(main,bg="#CDA84C")
    remove_page.configure(width=1280,height=470)
    remove_page.place(x=0,y=0)
    canvas = Canvas(remove_page,bg = "#FFFFFF",height = 470,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_image(640.0,235.0,image=frame_bg)
    canvas.create_image(1032.0,151.0,image=logo)
    canvas.create_text(36.0,125.0,anchor="nw",text="SELECT WHICH CUSTOMER\nTO DELETE",fill="#000000",font=("Roboto Slab", 40 * -1))
    name = StringVar()
    customers = []
    cursor.execute("select name from customers;")
    for i in cursor.fetchall():
        customers.append(i[0])
    OptionMenu(remove_page,name,*customers).place(x=290.0,y=42.0,width=459.0,height=53.0)
    Button(remove_page,image=removeButton,borderwidth=0,highlightthickness=0,
                           command=lambda: remove_submit(name),relief="flat").place(x=836.0,y=289.0,
                                                                                               width=391.0,height=113.0)
remove_switch()
remove_page.destroy()



window.resizable(False,False)
window.mainloop()
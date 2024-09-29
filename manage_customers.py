from tkinter import *
import mysql.connector as sql

connection = sql.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 database="project",
                                 auth_plugin='mysql_native_password')
cursor = connection.cursor()

window = Tk()

bg = PhotoImage(file=r"Resources\bg.png")
logo = PhotoImage(file=r"Resources\logo.png")

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
main.configure(width=1280,height=450)
main.place(x=0,y=250)

def add_switch():
    global add_page
    add_page = Frame(main,bg="#CDA84C")
    add_page.configure(width=1280,height=450)
    Label(add_page,text="ADD CUSTOMERS PAGE",font=("Cascadia Code SemiBold",32)).pack()
    add_page.place(x=0,y=0)
add_switch()

def edit_switch():
    global edit_page
    edit_page = Frame(main,bg="#CDA84C")
    edit_page.configure(width=1280,height=450)
    Label(edit_page,text="EDIT CUSTOMERS PAGE",font=("Cascadia Code SemiBold",32)).pack()
    edit_page.place(x=0,y=0)
edit_switch()
edit_page.destroy()

def remove_switch():
    global remove_page
    remove_page = Frame(main,bg="#CDA84C")
    remove_page.configure(width=1280,height=450)
    Label(remove_page,text="REMOVE CUSTOMERS PAGE",font=("Cascadia Code SemiBold",32)).pack()
    remove_page.place(x=0,y=0)
remove_switch()
remove_page.destroy()


window.resizable(False,False)
window.mainloop()
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
frame_bg  = PhotoImage(file=r"Resources\Vcustomer\frame_bg.png")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("CONTINENTAL HOTEL |  CUSTOMER INFORMATION ")
window.iconphoto(True,logo)

canvas = Canvas(window,bg = "#FFFFFF",height = 720,width = 1280,highlightthickness = 0)
canvas.place(x = 0, y = 0)

canvas.create_image(640,360,image=bg)
canvas.create_text(47,0,anchor="nw",text="THE CONTINENTAL",fill="#950B3C",font=("Cinzel Decorative Black", 106 * -1))
canvas.create_image(640.0,422.5,image=frame_bg)

CustomerTable = ttk.Treeview(window,columns=("uid","name","phone","email","address","room"),show="headings")
CustomerTable.heading("uid",text="UNIQUE ID")
CustomerTable.heading("name",text="CUSTOMER NAME")
CustomerTable.heading("phone",text="PHONE NO.")
CustomerTable.heading("email",text="EMAIL ADD.")
CustomerTable.heading("address",text="ADDRESS")
CustomerTable.heading("room",text="ROOM")
CustomerTable.place(x=40,y=160,height=530)

cursor.execute("select * from customers;")
data = cursor.fetchall()
for i in data:
    CustomerTable.insert(parent="",index=END,values=i)

window.resizable(False,False)
window.mainloop()
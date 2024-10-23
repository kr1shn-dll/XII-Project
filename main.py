from tkinter import *
import os

def switch_1():
    os.system("python manage_customers.py")
def switch_2():
    os.system("python manage_rooms.py")
def switch_3():
    os.system("python view_rooms.py")
def switch_4():
    os.system("python view_customers.py")

window = Tk()

bg = PhotoImage(file=r"Resources\Home\bg.png")
logo = PhotoImage(file=r"Resources\Home\logo.png")
button_image_1 = PhotoImage(file=r"Resources\Home\button_1.png")
button_image_2 = PhotoImage(file=r"Resources\Home\button_2.png")
button_image_3 = PhotoImage(file=r"Resources\Home\button_3.png")
button_image_4 = PhotoImage(file=r"Resources\Home\button_4.png")

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("CONTINENTAL HOTEL | HOME PAGE ")
window.iconphoto(True,logo)

canvas = Canvas(window,bg = "#FFFFFF",height = 720,width = 1280,highlightthickness = 0)
canvas.place(x = 0, y = 0)

canvas.create_image(640,360,image=bg)
canvas.create_image(1030,420,image=logo)

canvas.create_text(975,696,anchor="nw",text="Made by Krishn XII-O 2025",fill="#950B3C",font=("Cascadia Code SemiBold", 20 * -1))
canvas.create_text(47,0,anchor="nw",text="THE CONTINENTAL",fill="#950B3C",font=("Cinzel Decorative Black", 106 * -1))

button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=switch_1,relief="flat")
button_1.place(x=0,y=194,width=658,height=136)

button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=switch_2,relief="flat")
button_2.place(x=0,y=330,width=658,height=120)

button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=switch_3,relief="flat")
button_3.place(x=0,y=440,width=658,height=152)

button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=switch_4,relief="flat")
button_4.place(x=0,y=580,width=658,height=140)

window.resizable(False,False)
window.mainloop()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

SAGE = "#84994F"
YELLOW = "#FFE797"
ORANGE = "#FCB53B"
MAROON = "#A72703"
FONT_NAME = "Courier"


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=300,height=400)
window.config(padx=20,pady=20,bg=SAGE)
window.title("Password Manager")

canvas = Canvas(width=200,height=200,background=SAGE,highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(90,100,image=pass_img)
canvas.grid(row=0,column=1)

label_r1 = Label(text="Website",bg=SAGE ,fg=MAROON,font=(FONT_NAME,10))
label_r1.grid(row=1,column=0)

label_r2 = Label(text="Email/UserName",bg=SAGE ,fg=MAROON,font=(FONT_NAME,10))
label_r2.grid(row=2,column=0)

label_r3 = Label(text="Password",bg=SAGE ,fg=MAROON,font=(FONT_NAME,10))
label_r3.grid(row=3,column=0)

entry_r1 = Entry(width=35,bg=YELLOW,fg=MAROON,font=(FONT_NAME,10))
entry_r1.grid(row=1,column=1,columnspan=2)

entry_r2 = Entry(width=35,bg=YELLOW,fg=MAROON,font=(FONT_NAME,10))
entry_r2.grid(row=2,column=1,columnspan=2)

entry_r3 = Entry(width=21,bg=YELLOW,fg=MAROON,font=(FONT_NAME,10))
entry_r3.grid(row=3,column=1)

button_r3 = Button(text="Generate Password")
button_r3.grid(row=3,column=2)

button_add = Button(text="Add",width=35)
button_add.grid(row=4,column=1,columnspan=2,pady=10)

window.mainloop()



from tkinter import *


def miletokm():
    km=0
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.geometry("500x500")
window.config(bg="lightblue")

heading = Label(text="Miles to KM convertor", bg="yellow",font=("Times New Roman",12))
heading.grid(row=1,column=1)

miles_entry = Entry(width=5,fg="white",bg="blue",font=("Verdana",20,"bold"))
miles_entry.grid(row=2,column=2)

lb_Miles = Label(text="Miles",font=("Verdana",20,"bold"))
lb_Miles.grid(row=2,column=3)

km_result = Label(text="000",width=5,font=("Verdana",20,"bold"))
km_result.grid(row=3,column=2)

km_label = Label(text="KM",font=("Verdana",20,"bold"))
km_label.grid(row=3,column=3)

btn = Button(text="Calculate", command=miletokm)
btn.grid(row=6,column=2,columnspan=3)



window.mainloop()
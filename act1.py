import tkinter as tk

window = tk.Tk()

window.title("Sample Window")
window.configure(background="yellow",border=5, borderwidth=1)
window.minsize(200,200)
window.maxsize(500,500)
window.geometry("1000x500")

label1 = tk.Label(window, text="Grocery Shop Management System")
label1.pack()

tk.Label(window, text="Right Side").pack(side="right")

tk.Checkbutton(window,text="An option at the Bottom").pack(side="bottom")
## Label(text = “ ”, fg = “white”, bg = “black”, height=10, width=10)
## Label is used to display text on the screen

## Button(text = “ ”, fg = “white”, bg = “black”, height=10, width=10,command = func_name)

## entry_name = Entry(fg="yellow", bg="blue", width=50) - 
# Take I/p from User. You can also retrieve the i/p from the user by entry_name.get()

## Frame(master=window_name, relief=RAISED, borderwidth=5) - Container to hold

## widget_name.pack() - To make a widget visible on the screen

## Tkinter Grid - Its a Geometry Manager. It organizes widgets in 2-Dimensional Table.Use padx - for horizontal Spacing and pady for vertical spacing around the widget.
# frame.grid(row=1, column=2, padx=5,pady=5) - 

window.mainloop()



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, UnidentifiedImageError

window = tk.Tk()
window.title("Sign In")
window.minsize(500,500)
tk.Label(window,text="Sign in to Tkinter",font=("Font",30)).pack(ipady=5, fill="x")

img = Image.open("internship_pic.png")
image = ImageTk.PhotoImage(image=img)
tk.Label(window,image=image).pack(pady=5)

def check_input():
    secret_username = "username"
    secret_password = "password"
    username = username_entry.get()
    password = password_entry.get()
    if username == secret_username and password == secret_password:
        messagebox.showinfo("Info","User Logged In !")
    else:
        messagebox.showerror("Error","Invalid Username and Password")
tk.Label(window,text="Your Username").pack(anchor="w",padx=30)
username_entry = tk.Entry(window)
username_entry.pack()
tk.Label(window,text="Password").pack(anchor="w",padx=30)
password_entry = tk.Entry(window)
password_entry.pack()

tk.Button(window,text="Sign In",command=check_input,width=18).pack(pady=10,padx=30,fill="x")

tk.Checkbutton(
    window,
    text="Remember me",
    command=lambda: print("The check button works."),
).pack(side="left", padx=20, pady=5)
tk.Label(
    window,
    text="Forgot password?",
    fg="blue",
    cursor="hand2",
).pack(side="right", padx=20, pady=5)
window.mainloop()
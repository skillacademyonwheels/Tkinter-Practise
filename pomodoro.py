
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   global reps
   reps += 1

   work_sec = WORK_MIN * 60
   short_break_secs = SHORT_BREAK_MIN * 60
   long_break_secs = LONG_BREAK_MIN * 60


   if reps % 8 == 0:
      count_down(long_break_secs)
      title_label.config(text="BREAK", fg=RED)
   elif reps % 2 == 0:
    count_down(short_break_secs)
    title_label.config(text="BREAK", fg=PINK)
   else:
      count_down(work_sec)
      title_label.config(text="WORK",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = count // 60
    secs = count % 60

    if secs == 0:
       secs = "00"
    elif secs < 10:
       secs = f"0{secs}"
    else:
       secs = secs

    if mins <= 10:
      mins = f"0{mins}"
    

    timer = f"{mins}:{secs}"

    canvas.itemconfig(timer_text,text=timer)
    if count > 0:
      window.after(1000,count_down,count-1)
    else:
       start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer")
window.config(padx=100,pady=50,bg=YELLOW)
title_label = Label(text="Timer",bg=YELLOW ,fg=GREEN,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset")
reset_button.grid(column=2,row=2)

check_marks = Label(text="✅",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()
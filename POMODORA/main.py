from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#FFE3A9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    #go back to 00:00
    canvas.itemconfig(timer_text, text = "00:00")
    #title changes to 'Timer'
    title_label.config(text = "Timer")
    #reset check_marks
    check_marks.config(text = " ")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        title_label = Label(text='Long Break', fg=PINK, bg=BACKGROUND, font=(FONT_NAME, 45, 'bold'))
        title_label.grid(column=1, row=0)
    elif reps % 2 == 0:  # means it is even 0, 2, 4, 6
        count_down(work_sec)
        title_label = Label(text='Work', fg=RED, bg=BACKGROUND, font=(FONT_NAME, 45, 'bold'))
        title_label.grid(column=1, row=0)
    else:
        count_down(short_break_sec)
        title_label = Label(text='Short Break', fg=GREEN, bg=BACKGROUND, font=(FONT_NAME, 45, 'bold'))
        title_label.grid(column=1, row=0)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # "01:35"
    min = math.floor(count / 60)
    sec = int(count % 60)
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✅ "
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=BACKGROUND)

# title_label = Label(text='Timer', fg=GREEN, bg=BACKGROUND,  font= (FONT_NAME, 45, 'bold'))
title_label = Label(text= "Timer", fg=PINK, bg=BACKGROUND, font=(FONT_NAME, 45, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(103, 132, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
# canvas.pack()

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

start_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
start_button.grid(column=2, row=2)

check_marks = Label()  # ✔") #✅
check_marks.grid(column=1, row=2)

# start_timer()

window.mainloop()

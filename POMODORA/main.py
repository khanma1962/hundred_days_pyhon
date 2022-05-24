from tkinter import *
import time

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


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text = count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 132, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()
count_down(5)

window.mainloop()
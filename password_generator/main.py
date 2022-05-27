# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#FFE3A9"
FONT_NAME = "Courier"

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file(website, email, password):
    with open("data.txt", mode='w') as data_file:
        data = website + email + password
        data_file.write(data)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
# canvas.pack()

web_label = Label(text = 'Website: ', bg='white', highlightthickness=0)
web_label.grid(row=1, column=0)

web_entry = Entry(width=39)
web_entry.insert(END, string="")
website = web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_label = Label(text = 'Email/Username: ', bg='white', highlightthickness=0)
email_label.grid(row=2, column=0)

email_entry = Entry(width=39)
email = email_entry.insert(0, string="khan_m_a@hotmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text = 'Password: ', bg='white', highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = Entry(width=22)
password = password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

add_button = Button(text='Add', width=37 , bg='white', highlightthickness=0, command=add_to_file(website, email, password))
add_button.grid(row=4, column=1, columnspan=2)

gen_password_button = Button(text='Generate Password', highlightthickness=0)
gen_password_button.grid(row=3, column=2)

window.mainloop()

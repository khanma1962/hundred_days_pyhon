from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#FFE3A9"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_pass = [choice(letters) for _ in range(randint(8, 10))]
    symbol_pass = [choice(symbols) for _ in range(randint(2, 4))]
    number_pass = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_pass + symbol_pass + number_pass

    shuffle(password_list)

    password = "".join(password_list)  # converting list to a single password

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="One of field is empty. Please enter all info.")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"These are details entered {email}\n Password: {password}\n Is it OK to save?")

        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # read the dictionary
                data = json.load(data_file)

        except FileNotFoundError:
            print("Creating a new json file")
            with open("data.json", "w") as data_file:
                # read the dictionary
                json.dump(new_data, data_file, indent=4)

        else:
            # update the dictionary with new data
            data.update(new_data)

            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def search_password():

    website = web_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="File Error", message="File not found.")

    else:
        if website in data:
            email_found = data[website]["email"]
            password_found = data[website]["password"]

            # email_entry.insert(0, string="")
            # password_entry.insert(0, string="")

            email_entry.insert(0, string=email_found)
            password_entry.insert(END, string=password_found)
            messagebox.showinfo(title="Website", message=f"email is {email_found} and password is {password_found}")

        else:
            # print("No Email/Password found for this website.")
            messagebox.showinfo(title="Website Error", message=f"No data found website {website}.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
# canvas.pack()

web_label = Label(text='Website: ', bg='white', highlightthickness=0)
web_label.grid(row=1, column=0)

web_entry = Entry(width=21)
web_entry.insert(END, string="")
web_entry.grid(row=1, column=1)  # , columnspan=2)
web_entry.focus()
# print(web_entry)

email_label = Label(text='Email/Username: ', bg='white', highlightthickness=0)
email_label.grid(row=2, column=0)

email_entry = Entry(width=21)
email_entry.insert(0, string="khan_m_a@hotmail.com")
email_entry.grid(row=2, column=1)  # , columnspan=2)

password_label = Label(text='Password: ', bg='white', highlightthickness=0)
password_label.grid(row=3, column=0)

password_entry = Entry(width=22)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

add_button = Button(text='Add', width=37, bg='white', highlightthickness=0, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)

gen_password_button = Button(text='Generate Password', highlightthickness=0, command=generate_password)
gen_password_button.grid(row=3, column=2)

search_button = Button(text='Search', width=13, highlightthickness=0, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()

from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = (miles) * 1.69
    kilometer_res.config(text = f"{km}")
    # return miles * 1.69

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Mile to Kilometer Convertor ")
window.config(padx = 20, pady= 20)

miles_input = Entry(width=9)
miles_input.grid(column= 1, row= 0)

miles_label = Label(text = "Miles")
miles_label.grid(column= 2, row= 0)

is_equal_to = Label(text = "is equal to ")
is_equal_to.grid(column= 0, row= 1)

kilometer_lable = Label(text= "km")
kilometer_lable.grid(column= 2, row= 1)

# result = miles_input.get()
# print(type(result))
# print(result)
kilometer_res = Label(text= '0')
kilometer_res.grid(column= 1, row= 1)

calculate_button = Button(text = "Calculate", command = miles_to_km)
calculate_button.grid(column= 1, row= 2)


window.mainloop()
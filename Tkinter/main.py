
import tkinter

window = tkinter.Tk()
window.title("My first GUI program ")
window.minsize(width= 500, height= 300)

#label
my_label = tkinter.Label(text = "I am a label", font= ('Aerial', 15, "bold"))
my_label.pack(expand = 10)


window.mainloop()

import turtle

t = turtle.Turtle()
t.write("some stupid text")


# Graphical User Interface (GUI) using Tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = Label(text="Hello, Tkinter!", font=("Arial", 24, "italic"))
label.pack()

# Button
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    label.config(text=new_text) # Update label text when button is clicked

button = Button(text="Click Me", font=("Arial", 14), command=button_clicked)
button.pack()

# Entry+
input = Entry(width=30)
input.pack()
input.get()




# Keep the window open
window.mainloop()
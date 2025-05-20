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
    label.config(text="Button Clicked!") # Update label text when button is clicked

# button = Button(text="Click Me", font=("Arial", 14), command=button_clicked)
# button.pack()

# Entry
input = Entry(width=30)
input.pack()
input.get() # Get the text from the entry field
def get_input():
    user_input = input.get()
    label.config(text=user_input)

button = Button(text="Submit", font=("Arial", 14), command=get_input)
button.pack()





# Keep the window open
window.mainloop()
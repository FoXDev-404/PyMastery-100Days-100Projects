# Graphical User Interface (GUI) using Tkinter
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="Hello, Tkinter!", font=("Arial", 24, "italic"))
label.pack()






# Keep the window open
window.mainloop()
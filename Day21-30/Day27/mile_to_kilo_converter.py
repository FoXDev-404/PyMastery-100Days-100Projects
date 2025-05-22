# Mile to Kilometer Converter
from tkinter import *

# Conversion function
def mile_to_km():
    try:
        miles = float(miles_input.get())
        kilometers = round(miles * 1.60934, 2)  # Rounded to 2 decimal places
        kilometers_result_label.config(text=f"{kilometers}")
    except ValueError:
        kilometers_result_label.config(text="Invalid input 😢")

# Window setup
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Input Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# "Miles" label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to" label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# Result label
kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

# "KM" label
kilometers_label = Label(text="KM")
kilometers_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

# Run the GUI
window.mainloop()

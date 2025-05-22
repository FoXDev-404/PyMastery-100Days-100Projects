from tkinter import *

def convert():
    try:
        # Get value from input
        value = float(input_entry.get())
        
        # Determine direction and convert
        if conversion_direction.get() == 1:  # Miles to KM
            result = round(value * 1.60934, 2)
            formula_label.config(text=f"Formula: {value} miles × 1.60934 = {result} km")
        else:  # KM to Miles
            result = round(value * 0.621371, 2)
            formula_label.config(text=f"Formula: {value} km × 0.621371 = {result} miles")
            
        # Update result display
        result_label.config(text=f"{result}")
        
        # Add to history
        history_box.insert(0, f"{value} {'miles to km' if conversion_direction.get() == 1 else 'km to miles'} = {result}")
        if history_box.size() > 5:  # Keep only 5 recent conversions
            history_box.delete(5)
            
    except ValueError:
        result_label.config(text="Invalid input 😢")
        formula_label.config(text="Please enter a valid number")

def reset():
    input_entry.delete(0, END)
    result_label.config(text="0")
    formula_label.config(text="")
    input_entry.focus()

def update_labels():
    if conversion_direction.get() == 1:  # Miles to KM
        from_label.config(text="Miles")
        to_label.config(text="KM")
        direction_label.config(text="is equal to")
    else:  # KM to Miles
        from_label.config(text="KM")
        to_label.config(text="Miles")
        direction_label.config(text="is equal to")

# Window setup
window = Tk()
window.title("Enhanced Converter")
window.config(padx=25, pady=25, bg="#f0f0f0")
window.resizable(False, False)

# Add title
title_label = Label(
    window, 
    text="Miles ↔ Kilometers Converter",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0",
    fg="#333333"
)
title_label.grid(column=0, row=0, columnspan=3, pady=(0, 15))

# Conversion direction
conversion_direction = IntVar(value=1)  # Default: Miles to KM

direction_frame = Frame(window, bg="#f0f0f0")
direction_frame.grid(column=0, row=1, columnspan=3, pady=(0, 15))

miles_to_km_radio = Radiobutton(
    direction_frame,
    text="Miles to Kilometers",
    variable=conversion_direction,
    value=1,
    command=update_labels,
    bg="#f0f0f0"
)
miles_to_km_radio.pack(side=LEFT, padx=(0, 10))

km_to_miles_radio = Radiobutton(
    direction_frame,
    text="Kilometers to Miles",
    variable=conversion_direction,
    value=2,
    command=update_labels,
    bg="#f0f0f0"
)
km_to_miles_radio.pack(side=LEFT)

# Input Entry with label
input_entry = Entry(window, width=12, font=("Arial", 11))
input_entry.grid(column=1, row=2)
input_entry.focus()

# From label (Miles/KM)
from_label = Label(window, text="Miles", width=8, bg="#f0f0f0")
from_label.grid(column=2, row=2)

# Direction label ("is equal to")
direction_label = Label(window, text="is equal to", bg="#f0f0f0")
direction_label.grid(column=0, row=3)

# Result label
result_label = Label(
    window, 
    text="0",
    width=12,
    font=("Arial", 11, "bold"),
    relief=SUNKEN,
    borderwidth=1,
    bg="white"
)
result_label.grid(column=1, row=3, pady=10)

# To label (KM/Miles)
to_label = Label(window, text="KM", width=8, bg="#f0f0f0")
to_label.grid(column=2, row=3)

# Formula display
formula_label = Label(
    window,
    text="",
    font=("Arial", 9, "italic"),
    bg="#f0f0f0",
    fg="#555555"
)
formula_label.grid(column=0, row=4, columnspan=3, sticky=W, pady=(0, 10))

# Buttons frame
button_frame = Frame(window, bg="#f0f0f0")
button_frame.grid(column=0, row=5, columnspan=3, pady=5)

calculate_button = Button(
    button_frame,
    text="Calculate",
    command=convert,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=10
)
calculate_button.pack(side=LEFT, padx=(0, 5))

reset_button = Button(
    button_frame,
    text="Reset",
    command=reset,
    bg="#f44336",
    fg="white",
    font=("Arial", 10),
    width=10
)
reset_button.pack(side=LEFT)

# History section
history_frame = LabelFrame(
    window,
    text="Recent Conversions",
    bg="#f0f0f0",
    padx=10,
    pady=10
)
history_frame.grid(column=0, row=6, columnspan=3, sticky=EW, pady=(15, 0))

history_box = Listbox(
    history_frame,
    height=5,
    width=40,
    font=("Arial", 9)
)
history_box.pack()

# Keyboard bindings
window.bind("<Return>", lambda event: convert())
window.bind("<Escape>", lambda event: reset())

# Run the GUI
window.mainloop()
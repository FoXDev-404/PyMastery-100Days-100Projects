import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 10, "bold")
# New color palette
MAUVE = "#C599B6"
PINK = "#E6B2BA"
PEACH = "#FAD0C4"
BG_COLOR = "#FFF7F3"  # Light background color
TEXT_COLOR = "#333333"  # Dark text for contrast
WHITE = "#FFFFFF"  # White background for entries
DATA_FILE = "data.txt"
SEPARATOR = "=" * 50  # Separator for entries in the text file

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a secure random password containing letters, numbers, and symbols.
    The password is then inserted into the password entry field.
    """
    # Use string module for character sets
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Create password list with random characters using list comprehensions
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    
    # Combine and shuffle the password
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    
    # Update entry and clipboard
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- TEXT FILE FUNCTIONS ------------------------------- #
def save_to_text_file(data_dict):
    """Save the data dictionary to a beautifully formatted text file."""
    with open(DATA_FILE, "w") as data_file:
        for website, details in data_dict.items():
            data_file.write(f"Website: {website}\n")
            data_file.write(f"Email: {details['email']}\n")
            data_file.write(f"Password: {details['password']}\n")
            data_file.write(f"{SEPARATOR}\n")

def load_from_text_file():
    """Load data from the text file into a dictionary."""
    data_dict = {}
    try:
        with open(DATA_FILE, "r") as data_file:
            content = data_file.read().strip()
            if not content:  # Empty file
                return {}
                
            # Split by separator to get individual entries
            entries = content.split(SEPARATOR)
            for entry in entries:
                if not entry.strip():  # Skip empty entries
                    continue
                    
                lines = entry.strip().split("\n")
                if len(lines) >= 3:  # Ensure we have website, email, and password
                    website = lines[0].replace("Website: ", "")
                    email = lines[1].replace("Email: ", "")
                    password = lines[2].replace("Password: ", "")
                    
                    data_dict[website] = {
                        "email": email,
                        "password": password
                    }
        return data_dict
    except FileNotFoundError:
        return {}

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please enter a website to search.")
        return
    
    try:
        data = load_from_text_file()
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Error reading data file: {str(e)}")
        return
    
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty.")
        return
    
    is_ok = messagebox.askokcancel(title=website, 
                                   message=f"These are the details entered:\nEmail: {email}\n"
                                           f"Password: {password}\nIs it ok to save?")
    if not is_ok:
        return
    
    # Load existing data
    try:
        data = load_from_text_file()
    except Exception:
        data = {}
    
    # Update the data dictionary with new data
    data.update(new_data)
    
    # Write updated data to file
    save_to_text_file(data)
        
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)

# Canvas with logo
canvas = tk.Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 20))

# Labels with consistent styling
website_label = tk.Label(text="Website:", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, anchor="e", width=13)
website_label.grid(row=1, column=0, sticky="e", pady=5)

email_label = tk.Label(text="Email/Username:", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, anchor="e", width=13)
email_label.grid(row=2, column=0, sticky="e", pady=5)

password_label = tk.Label(text="Password:", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, anchor="e", width=13)
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entry fields with improved styling
website_entry = tk.Entry(width=21, font=FONT, bg=WHITE, insertbackground="gray")
website_entry.grid(row=1, column=1, sticky="ew", pady=5)
website_entry.focus()

email_entry = tk.Entry(width=38, font=FONT, bg=WHITE, insertbackground="gray")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
email_entry.insert(0, "rajpal010304@gmail.com")

password_entry = tk.Entry(width=21, font=FONT, bg=WHITE, insertbackground="gray")
password_entry.grid(row=3, column=1, sticky="ew", pady=5)

# Buttons with improved styling and new color palette
search_button = tk.Button(
    text="Search", 
    command=find_password,
    width=13, 
    font=FONT,
    bg=MAUVE,
    fg=TEXT_COLOR,  # Dark text color for better visibility
    borderwidth=1,
    cursor="hand2"
)
search_button.grid(row=1, column=2, sticky="ew", padx=(5, 0), pady=5)

generate_password_button = tk.Button(
    text="Generate Password", 
    command=generate_password,
    width=17,  # Increased from 13 to 17 for better text fit
    font=FONT,
    bg=PINK,
    fg=TEXT_COLOR,  # Dark text color for better visibility
    borderwidth=1,
    cursor="hand2"
)
generate_password_button.grid(row=3, column=2, sticky="ew", padx=(5, 0), pady=5)

add_password_button = tk.Button(
    text="Add", 
    width=36, 
    command=save,
    font=FONT,
    bg=PEACH,
    fg=TEXT_COLOR,  # Dark text color for better visibility
    borderwidth=1,
    cursor="hand2"
)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(10, 0))

# Configure grid column weights for proper resizing
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
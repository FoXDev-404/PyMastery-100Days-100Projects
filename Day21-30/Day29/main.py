import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import json
import os

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Arial", 10, "bold")
# New color palette
MAUVE = "#C599B6"
PINK = "#E6B2BA"
PEACH = "#FAD0C4"
BG_COLOR = "#FFF7F3"
TEXT_COLOR = "#333333"
WHITE = "#FFFFFF"
DATA_FILE = "data.json"

# ---------------------------- HELPER FUNCTIONS ------------------------------- #
def create_button(parent, text, command, bg=PINK, width=None, grid_args=None):
    """Create a styled button with consistent appearance"""
    btn = tk.Button(
        parent, text=text, command=command, font=FONT, bg=bg, fg=TEXT_COLOR,
        borderwidth=1, cursor="hand2", width=width
    )
    if grid_args:
        btn.grid(**grid_args)
    return btn

def create_label(parent, text, width=None, grid_args=None):
    """Create a styled label with consistent appearance"""
    lbl = tk.Label(
        parent, text=text, font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, 
        anchor="e", width=width
    )
    if grid_args:
        lbl.grid(**grid_args)
    return lbl

def create_entry(parent, width, grid_args=None, initial_text=None):
    """Create a styled entry with consistent appearance"""
    entry = tk.Entry(parent, width=width, font=FONT, bg=WHITE, insertbackground="gray")
    if grid_args:
        entry.grid(**grid_args)
    if initial_text:
        entry.insert(0, initial_text)
    return entry

def show_message(title, message, is_error=False):
    """Show a message dialog"""
    if is_error:
        messagebox.showerror(title=title, message=message)
    else:
        messagebox.showinfo(title=title, message=message)

def ask_question(title, message):
    """Ask a yes/no question"""
    return messagebox.askokcancel(title=title, message=message)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a secure random password"""
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- FILE OPERATIONS ------------------------------- #
def save_data(data):
    """Save data to file with backup"""
    if os.path.exists(DATA_FILE):
        backup_file = f"{DATA_FILE}.bak"
        try:
            with open(DATA_FILE, "r") as source, open(backup_file, "w") as target:
                target.write(source.read())
        except Exception as e:
            print(f"Backup creation failed: {e}")
    
    try:
        with open(DATA_FILE, "w") as data_file:
            json.dump(data, data_file, indent=4)
        return True
    except Exception as e:
        show_message("Save Error", f"Failed to save data: {e}", is_error=True)
        return False

def load_data():
    """Load data from file with fallback to backup"""
    try:
        if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
            with open(DATA_FILE, "r") as data_file:
                return json.load(data_file)
        return {}
    except json.JSONDecodeError:
        # Try to load from backup
        backup_file = f"{DATA_FILE}.bak"
        if os.path.exists(backup_file):
            try:
                with open(backup_file, "r") as backup:
                    return json.load(backup)
            except:
                pass
        return {}
    except:
        return {}

def find_website(website, data=None):
    """Find website in data (case-insensitive)"""
    if data is None:
        data = load_data()
    
    # Exact match check (case-insensitive)
    for site in data.keys():
        if site.lower() == website.lower():
            return site
    
    # Partial match check
    partial_matches = {site: info for site, info in data.items() 
                      if website.lower() in site.lower()}
    return partial_matches

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Search for website and display credentials"""
    website = website_entry.get().strip()
    if not website:
        show_message("Error", "Please enter a website to search.", is_error=True)
        return
    
    data = load_data()
    exact_match = find_website(website, data)
    
    if isinstance(exact_match, str):  # Found one exact match
        credentials = data[exact_match]
        show_message(exact_match, f"Email: {credentials['email']}\nPassword: {credentials['password']}")
    elif exact_match:  # Found partial matches
        if len(exact_match) == 1:
            site = list(exact_match.keys())[0]
            credentials = exact_match[site]
            show_message(f"Found: {site}", f"Email: {credentials['email']}\nPassword: {credentials['password']}")
        else:
            # Multiple matches - use simpledialog to choose
            sites = list(exact_match.keys())
            choice = simpledialog.askstring(
                "Multiple Matches", 
                f"Found {len(sites)} matches. Choose one:\n" + "\n".join([f"{i+1}. {s}" for i, s in enumerate(sites)]),
                parent=window
            )
            if choice and choice.isdigit() and 0 < int(choice) <= len(sites):
                site = sites[int(choice)-1]
                credentials = exact_match[site]
                show_message(f"Details for: {site}", f"Email: {credentials['email']}\nPassword: {credentials['password']}")
    else:
        show_message("Not Found", f"No details for '{website}' exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save website credentials"""
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    if not website or not password:
        show_message("Error", "Please don't leave any fields empty.", is_error=True)
        return
    
    data = load_data()
    existing_site = find_website(website, data)
    
    if isinstance(existing_site, str):  # Site exists
        # Ask what to do
        if not ask_question("Entry Exists", 
                          f"An entry for '{existing_site}' already exists.\nDo you want to update it?"):
            # Ask if user wants to create new entry
            create_new = ask_question("Create New", 
                                    f"Would you like to create a new entry instead?")
            if not create_new:
                return
            
            # Create with different name
            website = f"{website} ({len([k for k in data.keys() if website.lower() in k.lower()])})"
    
    # Save new or updated entry
    data[website] = {"email": email, "password": password}
    
    if save_data(data):
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()
        show_message("Success", f"Saved details for '{website}'")

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

# Labels
create_label(window, "Website:", width=13, grid_args={"row": 1, "column": 0, "sticky": "e", "pady": 5})
create_label(window, "Email/Username:", width=13, grid_args={"row": 2, "column": 0, "sticky": "e", "pady": 5})
create_label(window, "Password:", width=13, grid_args={"row": 3, "column": 0, "sticky": "e", "pady": 5})

# Entries
website_entry = create_entry(window, width=21, 
                            grid_args={"row": 1, "column": 1, "sticky": "ew", "pady": 5})
email_entry = create_entry(window, width=38, initial_text="rajpal010304@gmail.com",
                          grid_args={"row": 2, "column": 1, "columnspan": 2, "sticky": "ew", "pady": 5})
password_entry = create_entry(window, width=21,
                             grid_args={"row": 3, "column": 1, "sticky": "ew", "pady": 5})

# Buttons
create_button(window, "Search", find_password, bg=MAUVE, width=13,
             grid_args={"row": 1, "column": 2, "sticky": "ew", "padx": (5, 0), "pady": 5})
create_button(window, "Generate Password", generate_password, bg=PINK, width=17,
             grid_args={"row": 3, "column": 2, "sticky": "ew", "padx": (5, 0), "pady": 5})
create_button(window, "Add", save, bg=PEACH, width=36,
             grid_args={"row": 4, "column": 1, "columnspan": 2, "sticky": "ew", "pady": (10, 0)})

# Set focus to website entry
website_entry.focus()

# Configure grid column weights for proper resizing
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
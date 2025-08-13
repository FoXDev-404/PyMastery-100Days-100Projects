# ☕ Coffee & Wifi Directory

A Flask web application that helps remote workers and digital nomads find cafes with good coffee, reliable wifi, and power outlets. Perfect for when you need to work outside of home or the office!

## 🚀 Features

- **Home Page**: Welcome page with project introduction
- **View Cafes**: Browse all cafes with their ratings and details
- **Add New Cafe**: Contribute to the directory by adding new cafes
- **Comprehensive Ratings**: Rate cafes on:
  - ☕ Coffee Quality (1-5 cups)
  - 💪 Wifi Strength (1-5 strength levels)
  - 🔌 Power Socket Availability (1-5 socket levels)

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Forms**: Flask-WTF with WTForms validation
- **Data Storage**: CSV file
- **Styling**: Custom CSS with Bootstrap integration

## 📋 Requirements

- Python 3.7+
- Flask 2.3.2
- Flask-Bootstrap 2.2.0
- Flask-WTF 1.2.1
- WTForms 3.0.1
- Werkzeug 3.0.0

## 🔧 Installation

1. **Clone or download the project**
   ```bash
   cd coffee-and-wifi
   ```

2. **Install required packages**
   
   On Windows:
   ```cmd
   python -m pip install -r requirements.txt
   ```
   
   On macOS/Linux:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the application**
   Open your browser and go to: `http://127.0.0.1:5002`

## 📁 Project Structure

```
coffee-and-wifi/
├── main.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── cafe-data.csv       # Cafe data storage
├── static/
│   └── css/
│       └── styles.css  # Custom styling
└── templates/
    ├── base.html       # Base template with Bootstrap
    ├── index.html      # Home page
    ├── add.html        # Add cafe form
    └── cafes.html      # View all cafes
```

## 🎯 Usage

### Adding a New Cafe

1. Click "Show Me!" on the home page or navigate to `/add`
2. Fill out the cafe form with:
   - **Cafe Name**: The name of the cafe
   - **Location**: Google Maps URL for the cafe
   - **Opening Time**: When the cafe opens (e.g., "8AM")
   - **Closing Time**: When the cafe closes (e.g., "5:30PM")
   - **Coffee Rating**: Rate the coffee quality (☕ to ☕☕☕☕☕)
   - **Wifi Rating**: Rate the wifi strength (💪 to 💪💪💪💪💪)
   - **Power Rating**: Rate socket availability (🔌 to 🔌🔌🔌🔌🔌)
3. Submit the form to add the cafe to the directory

### Viewing Cafes

Navigate to `/cafes` to see a table of all cafes with their ratings and details.

## 🎨 Styling

The application uses a dark theme with:
- Dark gray background (#333)
- White text for readability
- Yellow accent color (#ffc107) for links
- Bootstrap components for responsive design
- Custom CSS for enhanced visual appeal

## 📝 Data Format

Cafe data is stored in CSV format with the following columns:
- Cafe Name
- Location (Google Maps URL)
- Opening Time
- Closing Time
- Coffee Rating (☕ symbols)
- Wifi Rating (💪 symbols)
- Power Rating (🔌 symbols)

## 🔒 Security Features

- CSRF protection with Flask-WTF
- URL validation for location field
- Data validation for all form fields
- Secure file handling with absolute paths

## 🚨 Troubleshooting

**FileNotFoundError for cafe-data.csv**
- The application automatically handles file paths relative to the script location
- Ensure `cafe-data.csv` exists in the same directory as `main.py`

**Port Already in Use**
- The app runs on port 5002 by default
- Change the port number in `main.py` if needed: `app.run(debug=True, port=YOUR_PORT)`

## 🤝 Contributing

Feel free to contribute by:
- Adding new cafes to the directory
- Improving the UI/UX
- Adding new features
- Fixing bugs
- Enhancing documentation

## 📄 License

This project is part of the 100 Days of Code Python course and is for educational purposes.

## 🎓 Learning Objectives

This project demonstrates:
- Flask web application development
- HTML form handling with Flask-WTF
- CSV file operations in Python
- Bootstrap integration
- Template inheritance
- URL routing and redirects
- Form validation
- File path handling

---

**Happy cafe hunting! ☕💻**

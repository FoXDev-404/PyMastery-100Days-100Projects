# Birthday Wisher - Automated Email Sender

## Project Overview

This application automatically sends birthday wishes via email to people in your contacts list. It checks a CSV file of birthdays against the current date and sends personalized birthday emails when there's a match.

## Environment Variables Setup

For security reasons, this application uses environment variables to store sensitive information.

### Option 1: Using a .env file (Development Only)

1. Install python-dotenv:

   ```
   pip install python-dotenv
   ```

2. Create a `.env` file in the project directory with:

   ```
   MY_EMAIL=your_email@gmail.com
   MY_PASSWORD=your_app_password
   ```

3. **IMPORTANT**: Add `.env` to your `.gitignore` file to prevent accidental commits.

## Project Structure

- `main.py`: Main script that checks birthdays and sends emails
- `birthdays.csv`: CSV file containing name, email, and birthday information
- `letter_templates/`: Directory containing birthday message templates

## Gmail Setup Note

If using Gmail, you'll need to generate an App Password:

1. Enable 2-Step Verification in your Google Account
2. Go to App Passwords in your Google Account security settings
3. Generate a new app password for "Mail"
4. Use this password in your .env file

# Email Sender - Security Setup

## Environment Variables Setup

For security reasons, this application uses environment variables to store sensitive information.

### Option 1: Using a .env file (Development Only)

1. Install python-dotenv:

   ```
   pip install python-dotenv
   ```

2. Create a `.env` file in the project directory with:

   ```
   EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   EMAIL_RECIPIENT=recipient@example.com
   ```

3. **IMPORTANT**: Add `.env` to your `.gitignore` file to prevent accidental commits.

### Option 2: System Environment Variables (Recommended)

#### Windows:

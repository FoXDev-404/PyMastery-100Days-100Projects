import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(subject, body, to_email=None, from_email=None, password=None):
    # Get credentials from environment variables if not provided
    from_email = from_email or os.environ.get("EMAIL")
    password = password or os.environ.get("EMAIL_PASSWORD")
    to_email = to_email or os.environ.get("EMAIL_RECIPIENT")
    
    # Validate credentials
    if not from_email:
        raise ValueError("Sender email address not provided")
    if not password:
        raise ValueError("Email password not provided")
    if not to_email:
        raise ValueError("Recipient email address not provided")
    
    # Format the email message
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        # Connect to Gmail SMTP server
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()  # Secure the connection
        
        # Login to sender account
        connection.login(user=from_email, password=password)
        
        # Send email
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=message
        )
        
        print("Email sent successfully!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
        
    finally:
        # Always close the connection
        if 'connection' in locals():
            connection.close()
            print("Connection closed.")


if __name__ == "__main__":
    # Example usage
    subject = "Hello from Python Email Sender"
    body = "This is a test email sent from the Python Email Sender application.\n\nRegards,\nPython Script"
    
    success = send_email(subject, body)
    
    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email. Check the error messages for details.")

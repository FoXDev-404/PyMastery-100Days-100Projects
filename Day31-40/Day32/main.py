import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(subject, body, to_email=None):
    # Get credentials from environment variables
    sender_email = os.environ.get("EMAIL")
    password = os.environ.get("EMAIL_PASSWORD")
    recipient = to_email or os.environ.get("EMAIL_RECIPIENT")
    
    # Validate credentials
    if not sender_email:
        raise ValueError("Sender email address not found in environment variables")
    if not password:
        raise ValueError("Email password not found in environment variables")
    if not recipient:
        raise ValueError("Recipient email address not found in environment variables")
    
    # Compose the email message
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        # Connect to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Secure the connection
            connection.starttls()
            
            # Login to sender account
            connection.login(user=sender_email, password=password)
            
            # Send email
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient,
                msg=message
            )
            
        print(f"Email sent successfully to {recipient}")
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


if __name__ == "__main__":
    # Example usage
    subject = "Test Email from Python"
    body = "Hello from Python!\n\nThis is a test email sent using smtplib.\n\nBest regards,\nPython Script"
    
    send_email(subject, body)

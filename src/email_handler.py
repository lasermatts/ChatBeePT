# Contains functions and classes to send emails using SMTP, including authentication and error handling.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve email credentials and recipient email
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_email(subject, body):
    """
    Sends an email with the provided subject and body.
    
    :param subject: str, subject of the email
    :param body: str, body/content of the email
    """
    # Creating the Email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Establish a secure session with Gmail's outgoing SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        
        # Login to sender email account
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send email
        server.send_message(msg)
        
        # Terminate the SMTP session
        server.quit()
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Example Usage
if __name__ == "__main__":
    send_email("Test Subject", "Hello, this is a test email body.")

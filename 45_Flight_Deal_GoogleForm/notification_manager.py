import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotificationManager:

    def __init__(self):
        # Set up Twilio client
        self.client = None
        twilio_sid = os.getenv("TWILIO_SID")
        twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
        
        if twilio_sid and twilio_token:
            from twilio.rest import Client
            self.client = Client(twilio_sid, twilio_token)
        else:
            print("Twilio credentials not found. SMS/WhatsApp functionality disabled.")
            
        # Set up email credentials
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_enabled = bool(self.email_user and self.email_password)
        
        if not self.email_enabled:
            missing = []
            if not self.email_user:
                missing.append("EMAIL_USER")
            if not self.email_password:
                missing.append("EMAIL_PASSWORD")
            print(f"Email functionality disabled: Missing {', '.join(missing)} in .env file.")

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_PHONE_NUMBER` and `MY_PHONE_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        if not self.client:
            print("SMS not sent: Twilio client not initialized due to missing credentials")
            return
            
        # Use the environment variables in the .env file, with fallbacks for different naming conventions
        from_number = os.getenv("TWILIO_PHONE_NUMBER") or os.getenv("TWILIO_VIRTUAL_NUMBER")
        to_number = os.getenv("MY_PHONE_NUMBER") or os.getenv("TWILIO_VERIFIED_NUMBER")
        
        if not from_number or not to_number:
            print("SMS not sent: Missing phone number configuration")
            return
            
        try:
            message = self.client.messages.create(
                from_=from_number,
                body=message_body,
                to=to_number
            )
            # Prints if successfully sent.
            print(f"SMS sent successfully. SID: {message.sid}")
        except Exception as e:
            print(f"Error sending SMS: {e}")

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        if not self.client:
            print("WhatsApp message not sent: Twilio client not initialized due to missing credentials")
            return
            
        # Use the environment variables in the .env file, with fallbacks for different naming conventions
        from_number = os.getenv("TWILIO_PHONE_NUMBER") or os.getenv("TWILIO_WHATSAPP_NUMBER") or os.getenv("TWILIO_VIRTUAL_NUMBER")
        to_number = os.getenv("MY_PHONE_NUMBER") or os.getenv("TWILIO_VERIFIED_NUMBER")
        
        if not from_number or not to_number:
            print("WhatsApp message not sent: Missing phone number configuration")
            return
            
        try:
            message = self.client.messages.create(
                from_=f'whatsapp:{from_number}',
                body=message_body,
                to=f'whatsapp:{to_number}'
            )
            print(f"WhatsApp message sent successfully. SID: {message.sid}")
        except Exception as e:
            print(f"Error sending WhatsApp message: {e}")
            
    def send_email(self, to_email, subject, body):
        """
        Sends an email notification about a flight deal.
        
        Args:
            to_email (str): Recipient's email address
            subject (str): Email subject line
            body (str): Email body text
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        if not self.email_enabled:
            print(f"Email not sent to {to_email}: Email functionality disabled due to missing credentials")
            return False
            
        try:
            # Create a MIMEText object to represent the email
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email_user
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Create both plain text and HTML versions of the message
            text_part = MIMEText(body, 'plain')
            
            # Convert plain text to HTML with clickable links
            html_body = body.replace("Book here:", "<br><br>Book here:")
            # Look for URLs in the text and make them clickable
            import re
            url_pattern = r'(https?://[^\s]+)'
            html_body = re.sub(url_pattern, r'<a href="\1">\1</a>', html_body)
            html_body = html_body.replace('\n', '<br>')
            
            html_part = MIMEText(html_body, 'html')
            
            # Attach both versions (email clients will use the best one they support)
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Connect to Gmail SMTP server
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                # Secure the connection
                connection.starttls()
                
                # Login to Gmail
                connection.login(user=self.email_user, password=self.email_password)
                
                # Send the email
                connection.send_message(msg)
                
            print(f"Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")
            return False

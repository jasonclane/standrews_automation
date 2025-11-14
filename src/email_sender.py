"""
Email module for sending filled PDF schedules.
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import os


class EmailSender:
    """Class for sending emails with PDF attachments."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize email sender.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            username: Email account username
            password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_schedule(self, recipient: str, pdf_path: str, subject: str = None, body: str = None) -> bool:
        """
        Send the filled schedule PDF via email.
        
        Args:
            recipient: Email address of the recipient
            pdf_path: Path to the filled PDF file
            subject: Email subject (optional)
            body: Email body text (optional)
            
        Returns:
            True if email sent successfully, False otherwise
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject or f"Service Schedule - {datetime.now().strftime('%Y-%m-%d')}"
            
            # Add body
            body_text = body or f"Please find attached the service schedule for this week.\n\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            msg.attach(MIMEText(body_text, 'plain'))
            
            # Attach PDF
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
            with open(pdf_path, 'rb') as f:
                pdf_attachment = MIMEApplication(f.read(), _subtype='pdf')
                pdf_filename = os.path.basename(pdf_path)
                pdf_attachment.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
                msg.attach(pdf_attachment)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
            
            return True
        
        except Exception as e:
            raise Exception(f"Error sending email: {str(e)}")

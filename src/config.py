"""
Configuration management for the service scheduling automation.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class to manage all settings."""
    
    # Notion Configuration
    NOTION_API_KEY = os.getenv('NOTION_API_KEY')
    NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
    
    # Email Configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
    
    # PDF Configuration
    PDF_TEMPLATE_PATH = os.getenv('PDF_TEMPLATE_PATH', 'templates/service_schedule_template.pdf')
    OUTPUT_PDF_PATH = os.getenv('OUTPUT_PDF_PATH', 'output/filled_schedule.pdf')
    
    @classmethod
    def validate(cls):
        """Validate that all required configuration is present."""
        required_fields = [
            ('NOTION_API_KEY', cls.NOTION_API_KEY),
            ('NOTION_DATABASE_ID', cls.NOTION_DATABASE_ID),
            ('SMTP_USERNAME', cls.SMTP_USERNAME),
            ('SMTP_PASSWORD', cls.SMTP_PASSWORD),
            ('RECIPIENT_EMAIL', cls.RECIPIENT_EMAIL),
        ]
        
        missing_fields = [field for field, value in required_fields if not value]
        
        if missing_fields:
            raise ValueError(f"Missing required configuration: {', '.join(missing_fields)}")
        
        return True

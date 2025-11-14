"""
Main orchestration script for service scheduling automation.
"""
import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from config import Config
from notion_integration import NotionClient
from pdf_filler import PDFFiller
from email_sender import EmailSender


def main():
    """Main function to orchestrate the service schedule automation."""
    
    print("=" * 60)
    print("St Andrews Service Schedule Automation")
    print("=" * 60)
    print()
    
    try:
        # Validate configuration
        print("1. Validating configuration...")
        Config.validate()
        print("   ✓ Configuration validated")
        print()
        
        # Fetch schedule data from Notion
        print("2. Fetching schedule data from Notion...")
        notion_client = NotionClient(
            api_key=Config.NOTION_API_KEY,
            database_id=Config.NOTION_DATABASE_ID
        )
        schedule_data = notion_client.fetch_schedule_data()
        print(f"   ✓ Fetched {len(schedule_data)} schedule entries")
        
        # Display fetched data
        if schedule_data:
            print("\n   Schedule Data:")
            for entry in schedule_data:
                position = entry.get('position', 'Unknown')
                name = entry.get('name', 'Unknown')
                print(f"   - {position}: {name}")
        print()
        
        # Fill PDF template
        print("3. Filling PDF template...")
        pdf_filler = PDFFiller(Config.PDF_TEMPLATE_PATH)
        output_path = pdf_filler.fill_template(schedule_data, Config.OUTPUT_PDF_PATH)
        print(f"   ✓ PDF filled and saved to: {output_path}")
        print()
        
        # Send email
        print("4. Sending email...")
        email_sender = EmailSender(
            smtp_server=Config.SMTP_SERVER,
            smtp_port=Config.SMTP_PORT,
            username=Config.SMTP_USERNAME,
            password=Config.SMTP_PASSWORD
        )
        
        email_sender.send_schedule(
            recipient=Config.RECIPIENT_EMAIL,
            pdf_path=output_path,
            subject=f"Service Schedule - {datetime.now().strftime('%B %d, %Y')}",
            body=f"Dear Team,\n\nPlease find attached the service schedule.\n\nBlessings,\nSt Andrews Automation System"
        )
        print(f"   ✓ Email sent to: {Config.RECIPIENT_EMAIL}")
        print()
        
        print("=" * 60)
        print("✓ Automation completed successfully!")
        print("=" * 60)
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nPlease ensure you have:")
        print("1. Created a .env file based on .env.example")
        print("2. Filled in all required values")
        sys.exit(1)
    
    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")
        print("\nPlease ensure:")
        print("1. Your PDF template exists at the specified path")
        print("2. The templates directory exists")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# St Andrews Service Schedule Automation

Repository for automation of St Andrews McKinney church processes, specifically for automating the weekly service scheduling workflow.

## Overview

This automation system:
1. Fetches service schedule data from a Notion database
2. Fills the data into a PDF template
3. Emails the completed schedule to the church email

## Features

- **Notion Integration**: Automatically retrieves schedule data from your Notion database
- **PDF Generation**: Fills a blank PDF template with the correct names in the correct positions
- **Email Automation**: Sends the completed schedule via email
- **Easy Configuration**: Simple environment variable configuration

## Prerequisites

- Python 3.7 or higher
- A Notion account with API access
- A Notion database containing your service schedule
- A PDF template for your service schedule
- Email account with SMTP access (Gmail, Outlook, etc.)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jasonclane/standrews_automation.git
cd standrews_automation
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on the example:
```bash
cp .env.example .env
```

4. Edit the `.env` file with your actual configuration values (see Configuration section below)

## Configuration

### Notion Setup

1. **Create a Notion Integration**:
   - Go to https://www.notion.so/my-integrations
   - Click "New integration"
   - Give it a name (e.g., "Service Schedule Automation")
   - Copy the "Internal Integration Token" - this is your `NOTION_API_KEY`

2. **Get your Database ID**:
   - Open your Notion database
   - Click "Share" and invite your integration
   - The database ID is in the URL: `https://www.notion.so/[workspace]/[DATABASE_ID]?v=...`

3. **Database Structure**:
   Your Notion database should have at least these properties:
   - `Position`: The service position (e.g., "Worship Leader", "Sound", "Usher 1")
   - `Name`: The name of the person serving in that position
   - `Date` (optional): The date of service

### Email Setup

For Gmail:
1. Enable 2-factor authentication on your Google account
2. Generate an "App Password": https://myaccount.google.com/apppasswords
3. Use this app password as your `SMTP_PASSWORD`

For other email providers, use their SMTP settings.

### PDF Template

1. Place your blank PDF template in the `templates/` directory
2. Update `PDF_TEMPLATE_PATH` in `.env` to point to your template

**PDF Template Options**:
- **Form Fields**: If your PDF has fillable form fields, name them to match your positions (e.g., "worship_leader", "sound_technician")
- **Text Overlay**: If no form fields exist, the system will overlay text at predefined coordinates (you may need to adjust coordinates in `src/pdf_filler.py`)

### Environment Variables

Edit your `.env` file with the following values:

```env
# Notion API Configuration
NOTION_API_KEY=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password_here
RECIPIENT_EMAIL=church@example.com

# PDF Template Path
PDF_TEMPLATE_PATH=templates/service_schedule_template.pdf
OUTPUT_PDF_PATH=output/filled_schedule.pdf
```

## Usage

Run the automation script:

```bash
python main.py
```

The script will:
1. Validate your configuration
2. Fetch schedule data from Notion
3. Fill the PDF template
4. Send the email with the attached PDF
5. Display progress and confirmation messages

## Project Structure

```
standrews_automation/
├── main.py                 # Main orchestration script
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment configuration
├── .env                   # Your actual configuration (not in git)
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── src/
│   ├── __init__.py
│   ├── config.py         # Configuration management
│   ├── notion_client.py  # Notion API integration
│   ├── pdf_filler.py     # PDF manipulation
│   └── email_sender.py   # Email functionality
├── templates/            # PDF templates go here
│   └── service_schedule_template.pdf
└── output/              # Generated PDFs (not in git)
    └── filled_schedule.pdf
```

## Troubleshooting

### "Missing required configuration" error
- Ensure your `.env` file exists and contains all required values
- Check that there are no typos in variable names

### "PDF template not found" error
- Verify the PDF template exists at the specified path
- Check that the `templates/` directory exists

### Notion API errors
- Verify your integration token is correct
- Ensure the integration has access to your database (check database sharing settings)
- Verify the database ID is correct

### Email errors
- For Gmail: Ensure you're using an App Password, not your regular password
- Check SMTP server and port settings
- Verify your firewall allows SMTP connections

### PDF filling issues
- If form fields aren't filling correctly, check that field names in your PDF match position names
- For text overlay, you may need to adjust coordinates in `src/pdf_filler.py` based on your template layout

## Scheduling Automation

To run this automatically on a schedule:

### Linux/Mac (cron)
```bash
# Edit crontab
crontab -e

# Add line to run every Sunday at 8 AM
0 8 * * 0 cd /path/to/standrews_automation && /usr/bin/python3 main.py
```

### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create a new task
3. Set trigger (e.g., weekly on Sunday)
4. Set action to run Python with main.py

## Security Notes

- Never commit your `.env` file to version control
- Use app-specific passwords for email when available
- Keep your Notion API key secure
- Regularly rotate credentials

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

See LICENSE file for details.

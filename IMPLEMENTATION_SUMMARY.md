# Implementation Summary

## What Was Built

This repository now contains a complete automation system for St Andrews church service scheduling that:

1. **Fetches schedule data from Notion** - Connects to your Notion database and retrieves position/name assignments
2. **Fills PDF templates** - Takes your blank PDF template and fills it with the correct names in the correct positions
3. **Sends emails automatically** - Emails the completed schedule to your church email address

## Files Created

### Core Application Files
- **`main.py`** - Main orchestration script that runs the entire workflow
- **`requirements.txt`** - Python dependencies (notion-client, PyPDF2, reportlab, etc.)
- **`.env.example`** - Template for configuration (copy to `.env` and fill in your values)
- **`.gitignore`** - Ensures sensitive files and build artifacts aren't committed

### Source Code Modules (`src/`)
- **`config.py`** - Configuration management and validation
- **`notion_integration.py`** - Notion API integration to fetch schedule data
- **`pdf_filler.py`** - PDF manipulation to fill templates (supports form fields and text overlay)
- **`email_sender.py`** - Email functionality with SMTP support

### Documentation
- **`README.md`** - Complete documentation with setup and usage instructions
- **`QUICKSTART.md`** - 5-minute quick start guide
- **`SETUP.md`** - Detailed step-by-step setup instructions
- **`docs/NOTION_SETUP.md`** - Guide for configuring your Notion database
- **`docs/PDF_TEMPLATE_GUIDE.md`** - Guide for creating and configuring PDF templates

### Directories
- **`templates/`** - Place your PDF template here
- **`output/`** - Generated PDFs are saved here (not tracked in git)

## Key Features

### ✓ Secure Configuration
- Uses environment variables (`.env` file) for sensitive credentials
- Never commits secrets to git
- Validates configuration before running

### ✓ Flexible PDF Handling
- Supports PDF form fields (recommended)
- Supports text overlay for non-form PDFs
- Adjustable coordinates for custom layouts

### ✓ Robust Error Handling
- Clear error messages for configuration issues
- Validation of required fields
- Helpful troubleshooting guidance

### ✓ Easy to Use
- Simple command: `python main.py`
- Clear progress messages
- Detailed logging of each step

### ✓ Well Documented
- Multiple documentation levels (Quick Start, Setup Guide, Technical Docs)
- Inline code comments
- Troubleshooting sections

## How to Use

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Configuration
```bash
cp .env.example .env
# Edit .env with your values:
# - Notion API key and database ID
# - Email SMTP settings
# - PDF template path
```

### 3. Prepare Your Notion Database
- Create a Notion integration at https://www.notion.so/my-integrations
- Set up a database with "Position" and "Name" properties
- Share the database with your integration
- Copy the database ID from the URL

### 4. Add Your PDF Template
- Create or obtain a PDF template
- Place it in `templates/` directory
- Optionally add form fields for automatic filling

### 5. Run the Automation
```bash
python main.py
```

The script will:
1. Validate your configuration
2. Fetch schedule data from Notion
3. Fill the PDF template
4. Email the completed schedule

## Scheduling Automation

You can schedule this to run automatically:

**Linux/Mac (cron):**
```bash
# Run every Sunday at 8 AM
0 8 * * 0 cd /path/to/standrews_automation && python3 main.py
```

**Windows (Task Scheduler):**
Create a task that runs Python with `main.py` on your desired schedule.

## Customization

### Adjust PDF Coordinates
If using text overlay, edit `src/pdf_filler.py` and modify the `position_coordinates` dictionary.

### Change Notion Property Names
If your Notion properties are named differently, edit `src/notion_integration.py` in the `_extract_schedule_entry` method.

### Modify Email Template
Edit `main.py` to customize the email subject and body text.

## Security Notes

- ✓ All dependencies checked for vulnerabilities (none found)
- ✓ CodeQL security scan passed (0 issues)
- ✓ Credentials stored in `.env` file (not in git)
- ✓ Uses app passwords for email (not plain passwords)

## Testing

Basic syntax and import tests pass:
- ✓ All modules import correctly
- ✓ Configuration validation works
- ✓ Error messages are helpful and clear

## Next Steps for You

1. **Set up your Notion integration and database** (see SETUP.md)
2. **Configure your email SMTP settings** (see SETUP.md)
3. **Create or add your PDF template** (see docs/PDF_TEMPLATE_GUIDE.md)
4. **Create your `.env` file** with actual credentials
5. **Run a test** to verify everything works
6. **Schedule it** to run automatically (optional)

## Support

If you need help:
1. Check the relevant documentation file (QUICKSTART.md, SETUP.md, etc.)
2. Review the troubleshooting sections
3. Open an issue on GitHub with details of any errors

## Architecture

```
User's Notion Database
        ↓
   [main.py orchestrates]
        ↓
notion_integration.py → Fetches data
        ↓
pdf_filler.py → Fills template
        ↓
email_sender.py → Sends email
        ↓
Church Email Inbox
```

The system is modular and maintainable, with each component handling a specific responsibility.

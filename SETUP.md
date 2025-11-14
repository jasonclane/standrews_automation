# Setup Guide

Follow these steps to set up the St Andrews Service Schedule Automation.

## Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up Notion Integration

1. **Create Notion Integration**:
   - Visit: https://www.notion.so/my-integrations
   - Click "New integration"
   - Name it: "Service Schedule Automation"
   - Select your workspace
   - Click "Submit"
   - **Copy the Integration Token** (starts with `secret_`)

2. **Prepare Your Notion Database**:
   - Create or open your service schedule database in Notion
   - Ensure it has these properties:
     - `Position` (Select or Title): Service position names
     - `Name` (Rich Text or Title): Person's name
     - `Date` (Date): Service date (optional)

3. **Share Database with Integration**:
   - Open your database in Notion
   - Click "..." menu → "Share"
   - Find and select your integration
   - Click "Invite"

4. **Get Database ID**:
   - Copy the URL of your database
   - Format: `https://www.notion.so/workspace/DATABASE_ID?v=...`
   - Extract the `DATABASE_ID` part (32-character hex string)

## Step 3: Set Up Email Configuration

### For Gmail:

1. Enable 2-Factor Authentication:
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. Create App Password:
   - Go to: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other (Custom name)" → "Church Automation"
   - Click "Generate"
   - **Copy the 16-character password**

### For Other Email Providers:

Look up SMTP settings for your email provider:
- **Outlook/Hotmail**: smtp-mail.outlook.com, port 587
- **Yahoo**: smtp.mail.yahoo.com, port 587
- **Office 365**: smtp.office365.com, port 587

## Step 4: Create Configuration File

1. Copy the example configuration:
```bash
cp .env.example .env
```

2. Edit `.env` with your actual values:
```env
NOTION_API_KEY=secret_your_token_here
NOTION_DATABASE_ID=your_database_id_here
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password_here
RECIPIENT_EMAIL=church@example.com
```

## Step 5: Add Your PDF Template

1. Create or obtain your service schedule PDF template
2. Place it in the `templates/` directory
3. Name it `service_schedule_template.pdf` or update `PDF_TEMPLATE_PATH` in `.env`

### Creating a PDF Template:

**Option A - Using LibreOffice (Free)**:
1. Create your schedule layout in LibreOffice Writer
2. Add form fields for each position
3. File → Export as PDF → Check "Create PDF form"

**Option B - Using Word + PDF Converter**:
1. Create layout in Microsoft Word
2. Save/Export as PDF
3. Use a PDF form editor to add fillable fields

**Option C - Online Tools**:
- Use services like PDFescape or JotForm to create form fields
- Export the PDF with form fields

## Step 6: Test the Setup

Run a test:
```bash
python main.py
```

Expected output:
```
============================================================
St Andrews Service Schedule Automation
============================================================

1. Validating configuration...
   ✓ Configuration validated

2. Fetching schedule data from Notion...
   ✓ Fetched X schedule entries

3. Filling PDF template...
   ✓ PDF filled and saved to: output/filled_schedule.pdf

4. Sending email...
   ✓ Email sent to: church@example.com

============================================================
✓ Automation completed successfully!
============================================================
```

## Step 7: Schedule Automatic Runs (Optional)

### On Linux/Mac (using cron):

```bash
# Edit crontab
crontab -e

# Run every Sunday at 8 AM
0 8 * * 0 cd /path/to/standrews_automation && python3 main.py

# Or run every Friday at 5 PM
0 17 * * 5 cd /path/to/standrews_automation && python3 main.py
```

### On Windows (using Task Scheduler):

1. Open Task Scheduler
2. Click "Create Basic Task"
3. Name: "Service Schedule Automation"
4. Trigger: Weekly (select day/time)
5. Action: Start a program
   - Program: `C:\Python3X\python.exe`
   - Arguments: `main.py`
   - Start in: `C:\path\to\standrews_automation`
6. Finish

## Troubleshooting

### Error: "Missing required configuration"
- Check that `.env` file exists
- Verify all required fields are filled in
- No extra spaces in variable values

### Error: "PDF template not found"
- Ensure template file exists in `templates/` directory
- Check filename matches `PDF_TEMPLATE_PATH` in `.env`
- Verify file path is correct (use absolute path if needed)

### Error: "Error fetching data from Notion"
- Verify Integration Token is correct
- Ensure database is shared with the integration
- Check Database ID is correct
- Verify database has required properties (Position, Name)

### Error: "Error sending email"
- For Gmail: Use App Password, not regular password
- Verify SMTP server and port are correct
- Check username/password are correct
- Ensure less secure app access is enabled (if not using App Password)
- Check firewall isn't blocking SMTP

### PDF not filling correctly
- Verify form field names match position names
- For text overlay: Adjust coordinates in `src/pdf_filler.py`
- Check that schedule data is being fetched correctly

## Need Help?

If you encounter issues:
1. Check this troubleshooting section
2. Review the main README.md
3. Check Python error messages carefully
4. Open an issue on GitHub with error details

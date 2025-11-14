# Quick Start Guide

Get up and running in 5 minutes!

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. Configure Environment
```bash
# Copy example config
cp .env.example .env

# Edit with your values
nano .env  # or use your favorite editor
```

Required values:
- `NOTION_API_KEY` - Get from https://www.notion.so/my-integrations
- `NOTION_DATABASE_ID` - From your database URL
- `SMTP_USERNAME` - Your email address
- `SMTP_PASSWORD` - App password (for Gmail: https://myaccount.google.com/apppasswords)
- `RECIPIENT_EMAIL` - Where to send the schedule

## 3. Add Your PDF Template
```bash
# Place your PDF template in the templates directory
cp /path/to/your/template.pdf templates/service_schedule_template.pdf
```

## 4. Set Up Notion Database
Your Notion database needs these properties:
- **Position** (Select or Title) - e.g., "Worship Leader", "Sound"
- **Name** (Rich Text or Title) - e.g., "John Smith"
- **Date** (Date) - Optional

Don't forget to share the database with your integration!

## 5. Run It!
```bash
python main.py
```

## Example Output
```
============================================================
St Andrews Service Schedule Automation
============================================================

1. Validating configuration...
   ✓ Configuration validated

2. Fetching schedule data from Notion...
   ✓ Fetched 12 schedule entries

   Schedule Data:
   - Worship Leader: John Smith
   - Sound: Jane Doe
   ...

3. Filling PDF template...
   ✓ PDF filled and saved to: output/filled_schedule.pdf

4. Sending email...
   ✓ Email sent to: church@example.com

============================================================
✓ Automation completed successfully!
============================================================
```

## Next Steps

- **Schedule it**: Set up a cron job or Task Scheduler to run automatically
- **Customize**: Adjust PDF coordinates or field mappings in `src/pdf_filler.py`
- **Test**: Run a few times to ensure everything works as expected

## Need More Help?

- See [SETUP.md](SETUP.md) for detailed setup instructions
- See [README.md](README.md) for full documentation
- Open an issue on GitHub if you encounter problems

# Workflow Documentation

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Configuration                        │
│  (.env file with API keys, email settings, PDF template)   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      main.py                                 │
│              (Orchestrates the workflow)                     │
└─┬───────────────────────────────────────────────────────────┘
  │
  │ Step 1: Validate Configuration
  ├──────────────────────────────────────┐
  │                                      ▼
  │                           ┌─────────────────────┐
  │                           │   config.py         │
  │                           │ - Load .env         │
  │                           │ - Validate settings │
  │                           └─────────────────────┘
  │
  │ Step 2: Fetch Schedule Data
  ├──────────────────────────────────────┐
  │                                      ▼
  │                           ┌─────────────────────────────┐
  │                           │  notion_integration.py      │
  │                           │ - Connect to Notion API     │
  │                           │ - Query database            │
  │                           │ - Extract positions & names │
  │                           └──────────┬──────────────────┘
  │                                      │
  │                                      ▼
  │                           ┌─────────────────────┐
  │                           │  Notion Database    │
  │                           │ ┌─────────────────┐ │
  │                           │ │ Position | Name │ │
  │                           │ ├─────────────────┤ │
  │                           │ │ Worship  | John │ │
  │                           │ │ Sound    | Jane │ │
  │                           │ │ ...      | ...  │ │
  │                           │ └─────────────────┘ │
  │                           └─────────────────────┘
  │
  │ Step 3: Fill PDF Template
  ├──────────────────────────────────────┐
  │                                      ▼
  │                           ┌─────────────────────────┐
  │                           │   pdf_filler.py         │
  │                           │ - Read template PDF     │
  │                           │ - Fill form fields OR   │
  │                           │ - Overlay text          │
  │                           │ - Generate output PDF   │
  │                           └──────────┬──────────────┘
  │                                      │
  │                                      ▼
  │                           ┌─────────────────────┐
  │                           │  output/            │
  │                           │ filled_schedule.pdf │
  │                           └─────────────────────┘
  │
  │ Step 4: Send Email
  └──────────────────────────────────────┐
                                         ▼
                              ┌─────────────────────────┐
                              │  email_sender.py        │
                              │ - Create MIME message   │
                              │ - Attach PDF            │
                              │ - Connect to SMTP       │
                              │ - Send email            │
                              └──────────┬──────────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │  Church Email       │
                              │  📧 Inbox           │
                              └─────────────────────┘
```

## Data Flow

### 1. Configuration Phase
```
.env file → config.py → Validate → Ready
```

### 2. Data Retrieval Phase
```
Notion API → notion_integration.py → Parse Properties → Schedule Data
```

**Example Data Structure:**
```python
[
    {"position": "Worship Leader", "name": "John Smith"},
    {"position": "Sound", "name": "Jane Doe"},
    {"position": "Usher 1", "name": "Bob Johnson"}
]
```

### 3. PDF Generation Phase
```
Template PDF + Schedule Data → pdf_filler.py → Filled PDF
```

**Two Methods:**
- **Form Fields**: Direct field population
- **Text Overlay**: Coordinate-based text placement

### 4. Email Distribution Phase
```
Filled PDF → email_sender.py → SMTP Server → Recipient
```

## Error Handling Flow

```
┌─────────────┐
│  main.py    │
└──────┬──────┘
       │
       ├─ Configuration Error → Display helpful message → Exit
       │
       ├─ Notion API Error → Show connection issue → Exit
       │
       ├─ PDF Error → Show template issue → Exit
       │
       └─ Email Error → Show SMTP issue → Exit
```

## Success Path

```
Start
  ↓
Validate Config ✓
  ↓
Fetch from Notion ✓ (Shows count of entries)
  ↓
Fill PDF ✓ (Shows output path)
  ↓
Send Email ✓ (Shows recipient)
  ↓
Complete! 🎉
```

## Integration Points

### External Systems

1. **Notion API**
   - Endpoint: `https://api.notion.com/v1/databases/{id}/query`
   - Authentication: Bearer token
   - Data Format: JSON

2. **SMTP Server**
   - Common servers: Gmail, Outlook, Office365
   - Authentication: Username/Password or App Password
   - Protocol: TLS/STARTTLS

### File System

1. **Input**
   - `.env` - Configuration
   - `templates/[template].pdf` - PDF template

2. **Output**
   - `output/filled_schedule.pdf` - Generated PDF
   - Console logs - Progress messages

## Customization Points

Users can customize:

1. **Notion Database Structure** (`src/notion_integration.py`)
   - Property names
   - Data extraction logic
   - Filtering criteria

2. **PDF Layout** (`src/pdf_filler.py`)
   - Text coordinates
   - Font sizes
   - Position mappings

3. **Email Template** (`main.py`)
   - Subject line
   - Body text
   - Attachment name

## Scheduling Options

### Cron Job (Linux/Mac)
```bash
# Every Sunday at 8 AM
0 8 * * 0 /path/to/python /path/to/main.py

# Every Friday at 5 PM
0 17 * * 5 /path/to/python /path/to/main.py
```

### Task Scheduler (Windows)
- Trigger: Weekly on specific day/time
- Action: Run Python script
- Arguments: Path to main.py

### Cloud Services
- AWS Lambda with CloudWatch Events
- Google Cloud Scheduler
- Azure Functions with Timer Trigger

## Performance Considerations

- **Notion API**: Rate limited to 3 requests per second
- **PDF Generation**: Fast (<1 second for typical templates)
- **Email Sending**: Depends on SMTP server and attachment size
- **Total Runtime**: Typically 2-5 seconds

## Security Considerations

1. **Credentials**: Stored in `.env` (not committed to git)
2. **API Keys**: Never logged or displayed
3. **Email**: Uses TLS encryption
4. **Dependencies**: Regular security scanning recommended

## Troubleshooting Flow

```
Issue Reported
     ↓
Check Logs/Error Messages
     ↓
Identify Component
     ↓
     ├─ Config Issue → Check .env file
     ├─ Notion Issue → Verify API key and database access
     ├─ PDF Issue → Check template and coordinates
     └─ Email Issue → Verify SMTP settings
     ↓
Apply Fix
     ↓
Test Again
```

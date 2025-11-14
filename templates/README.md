# Templates Directory

Place your PDF template file in this directory.

## Template Guidelines

Your PDF template should be a blank form with spaces for the following service positions (adjust based on your needs):

- Worship Leader
- Assistant Worship Leader
- Sound Technician
- Video Technician
- Slides Operator
- Usher 1
- Usher 2
- Greeter 1
- Greeter 2
- Communion Prep
- Communion Server 1
- Communion Server 2

## Options for PDF Templates

### Option 1: PDF with Form Fields (Recommended)
Create a PDF with fillable form fields. Name the fields to match your positions:
- `worship_leader`
- `assistant_worship_leader`
- `sound`
- `video`
- etc.

You can create this using:
- Adobe Acrobat
- LibreOffice Writer (File > Export as PDF > check "Create PDF form")
- Online PDF form creators

### Option 2: Plain PDF
If your PDF doesn't have form fields, the system will overlay text at predefined coordinates. You may need to adjust the coordinates in `src/pdf_filler.py` to match your template layout.

## Naming Convention

Save your template as: `service_schedule_template.pdf`

Or update the `PDF_TEMPLATE_PATH` in your `.env` file to match your chosen filename.

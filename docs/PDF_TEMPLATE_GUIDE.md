# PDF Template Guide

This guide explains how to create and configure PDF templates for the automation system.

## Template Requirements

Your PDF template should have designated spaces or form fields for each service position.

## Option 1: PDF with Form Fields (Recommended)

### Creating Form Fields

**Using LibreOffice (Free)**:
1. Create your layout in LibreOffice Writer
2. Insert form fields: View > Toolbars > Form Controls
3. Add text boxes for each position
4. Name each field to match position names (e.g., "worship_leader", "sound")
5. File > Export as PDF > Check "Create PDF form"

**Using Adobe Acrobat**:
1. Create your layout
2. Tools > Prepare Form
3. Add text fields for each position
4. Name fields appropriately
5. Save

### Field Naming Convention

Match these names in your PDF form fields:
- `worship_leader`
- `assistant_worship_leader`
- `sound` or `sound_technician`
- `video` or `video_technician`
- `slides` or `slides_operator`
- `usher_1`
- `usher_2`
- `greeter_1`
- `greeter_2`
- `communion_prep`
- `communion_serve_1`
- `communion_serve_2`

## Option 2: Plain PDF with Text Overlay

If your PDF doesn't have form fields, the system will overlay text at predefined coordinates.

### Adjusting Coordinates

Edit `src/pdf_filler.py` and modify the `position_coordinates` dictionary:

```python
position_coordinates = {
    'worship_leader': (200, 700),  # (x, y) coordinates
    'sound': (200, 670),
    # ... add more positions
}
```

To find the right coordinates:
1. Start with approximate values
2. Run the automation
3. Check the output PDF
4. Adjust coordinates and re-run
5. Repeat until positions are correct

### Coordinate System

- Origin (0, 0) is at bottom-left corner
- X increases to the right
- Y increases upward
- Standard letter size: 612 x 792 points

## Template Layout Suggestions

### Minimal Template
```
SERVICE SCHEDULE
Date: _________________

Worship Leader: _________________
Sound: _________________
Video: _________________
Slides: _________________
```

### Complete Template
```
ST ANDREWS CHURCH
WEEKLY SERVICE SCHEDULE
Date: _________________

WORSHIP TEAM
Worship Leader: _________________
Assistant Worship Leader: _________________

TECH TEAM
Sound Technician: _________________
Video Technician: _________________
Slides Operator: _________________

HOSPITALITY
Usher 1: _________________
Usher 2: _________________
Greeter 1: _________________
Greeter 2: _________________

COMMUNION
Preparation: _________________
Server 1: _________________
Server 2: _________________
```

## Testing Your Template

1. Place your template in `templates/` directory
2. Update `.env` with the template path
3. Run `python main.py`
4. Check `output/filled_schedule.pdf`
5. Verify all names appear in correct positions
6. Adjust as needed

## Tips

1. **Keep it Simple**: Start with a simple layout, add complexity later
2. **Leave Space**: Ensure enough space for longer names
3. **Font Size**: Use 10-12pt fonts for readability
4. **Test Names**: Test with various name lengths
5. **Margins**: Leave adequate margins for printing

## Common Issues

### Names not appearing
- Check form field names match position names
- Verify coordinates are within page bounds
- Ensure PDF isn't password-protected

### Names in wrong positions
- Adjust coordinates in `position_coordinates` dictionary
- Check form field names

### Names cut off
- Increase field width in PDF form
- Use smaller font size
- Adjust layout spacing

## Example Templates

The `templates/` directory includes:
- `README.md` - Instructions for your template
- Place your actual template here as `service_schedule_template.pdf`

You can create multiple templates for different service types and switch between them using the `.env` configuration.

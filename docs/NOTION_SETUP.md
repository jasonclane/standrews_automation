# Notion Database Configuration Guide

This guide explains how to structure your Notion database for the automation system.

## Required Properties

Your Notion database must have at least these two properties:

### 1. Position
- **Type**: Select, Title, or Rich Text
- **Purpose**: The service position/role
- **Examples**: 
  - "Worship Leader"
  - "Assistant Worship Leader"
  - "Sound Technician"
  - "Video Technician"
  - "Slides Operator"
  - "Usher 1"
  - "Usher 2"
  - "Greeter 1"
  - "Greeter 2"
  - "Communion Prep"
  - "Communion Server 1"
  - "Communion Server 2"

### 2. Name
- **Type**: Rich Text or Title
- **Purpose**: The name of the person serving in that position
- **Examples**:
  - "John Smith"
  - "Jane Doe"
  - "TBD" (if not yet assigned)

## Optional Properties

### Date
- **Type**: Date
- **Purpose**: The date of the service
- **Format**: Any date format (YYYY-MM-DD recommended)

### Status
- **Type**: Select
- **Purpose**: Track confirmation status
- **Options**: "Confirmed", "Pending", "Need Replacement"

## Example Database Structure

| Position | Name | Date | Status |
|----------|------|------|--------|
| Worship Leader | John Smith | 2024-01-07 | Confirmed |
| Assistant Worship Leader | Jane Doe | 2024-01-07 | Confirmed |
| Sound Technician | Bob Johnson | 2024-01-07 | Confirmed |
| Video Technician | Alice Brown | 2024-01-07 | Pending |
| Usher 1 | Charlie Wilson | 2024-01-07 | Confirmed |
| Usher 2 | David Lee | 2024-01-07 | Confirmed |

## Database Setup Steps

1. **Create the Database**:
   - In Notion, create a new database (Table, Board, or Gallery view)
   - Add the required properties: Position and Name

2. **Populate with Data**:
   - Add rows for each service position
   - Fill in the names of people serving

3. **Share with Integration**:
   - Click the "..." menu in top right
   - Select "Add connections"
   - Choose your integration
   - Click "Confirm"

4. **Get Database ID**:
   - Copy the database URL
   - Extract the DATABASE_ID (32-character hex string)
   - Add to your `.env` file

## Tips

1. **Consistent Naming**: Use consistent position names that match your PDF template
2. **Regular Updates**: Update the database weekly with new assignments
3. **Templates**: Use Notion's template feature to quickly add a full week's schedule

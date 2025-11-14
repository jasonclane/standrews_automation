"""
PDF manipulation module for filling service schedule template.
"""
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from typing import Dict, List


class PDFFiller:
    """Class for filling PDF templates with schedule data."""
    
    def __init__(self, template_path: str):
        """
        Initialize PDF filler with template path.
        
        Args:
            template_path: Path to the PDF template file
        """
        self.template_path = template_path
        
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"PDF template not found: {template_path}")
    
    def fill_template(self, schedule_data: List[Dict[str, str]], output_path: str) -> str:
        """
        Fill PDF template with schedule data.
        
        Args:
            schedule_data: List of dictionaries with 'position' and 'name' keys
            output_path: Path where the filled PDF should be saved
            
        Returns:
            Path to the filled PDF file
        """
        try:
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            
            # Read the template PDF
            template_pdf = PdfReader(self.template_path)
            writer = PdfWriter()
            
            # Try to fill form fields if they exist
            if template_pdf.get_form_text_fields():
                writer = self._fill_form_fields(template_pdf, schedule_data)
            else:
                # If no form fields, overlay text on the PDF
                writer = self._overlay_text(template_pdf, schedule_data)
            
            # Write the output
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            return output_path
        
        except Exception as e:
            raise Exception(f"Error filling PDF template: {str(e)}")
    
    def _fill_form_fields(self, template_pdf: PdfReader, schedule_data: List[Dict[str, str]]) -> PdfWriter:
        """
        Fill PDF form fields with schedule data.
        
        Args:
            template_pdf: PdfReader object of the template
            schedule_data: List of schedule entries
            
        Returns:
            PdfWriter with filled form fields
        """
        writer = PdfWriter()
        
        # Copy all pages
        for page in template_pdf.pages:
            writer.add_page(page)
        
        # Get form fields
        form_fields = template_pdf.get_form_text_fields()
        
        # Create a mapping of position to name
        position_name_map = {entry['position']: entry['name'] for entry in schedule_data}
        
        # Update form fields
        for field_name in form_fields:
            # Try to match field name with position
            for position, name in position_name_map.items():
                if position.lower().replace(' ', '_') in field_name.lower():
                    writer.update_page_form_field_values(
                        writer.pages[0], {field_name: name}
                    )
        
        return writer
    
    def _overlay_text(self, template_pdf: PdfReader, schedule_data: List[Dict[str, str]]) -> PdfWriter:
        """
        Overlay text on PDF when form fields are not available.
        
        Args:
            template_pdf: PdfReader object of the template
            schedule_data: List of schedule entries
            
        Returns:
            PdfWriter with text overlay
        """
        writer = PdfWriter()
        
        # Create overlay with text
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Position mapping (these need to be adjusted based on your template)
        # Format: position_name: (x, y)
        position_coordinates = {
            'worship_leader': (200, 700),
            'assistant_worship_leader': (200, 670),
            'sound': (200, 640),
            'video': (200, 610),
            'slides': (200, 580),
            'usher_1': (200, 550),
            'usher_2': (200, 520),
            'greeter_1': (200, 490),
            'greeter_2': (200, 460),
            'communion_prep': (200, 430),
            'communion_serve_1': (200, 400),
            'communion_serve_2': (200, 370),
        }
        
        # Write schedule data to overlay
        for entry in schedule_data:
            position = entry['position'].lower().replace(' ', '_')
            name = entry['name']
            
            # Find matching coordinate
            for pos_key, (x, y) in position_coordinates.items():
                if pos_key in position or position in pos_key:
                    can.drawString(x, y, name)
                    break
        
        can.save()
        
        # Move to the beginning of the BytesIO buffer
        packet.seek(0)
        overlay_pdf = PdfReader(packet)
        
        # Merge overlay with template
        page = template_pdf.pages[0]
        page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
        
        # Copy remaining pages if any
        for i in range(1, len(template_pdf.pages)):
            writer.add_page(template_pdf.pages[i])
        
        return writer

"""
Notion API integration for fetching service schedule data.
"""
from notion_client import Client
from typing import Dict, List, Any


class NotionClient:
    """Client for interacting with Notion API to fetch schedule data."""
    
    def __init__(self, api_key: str, database_id: str):
        """
        Initialize Notion client.
        
        Args:
            api_key: Notion API integration token
            database_id: ID of the Notion database containing schedule data
        """
        self.client = Client(auth=api_key)
        self.database_id = database_id
    
    def fetch_schedule_data(self) -> List[Dict[str, Any]]:
        """
        Fetch schedule data from Notion database.
        
        Returns:
            List of schedule entries with position and name information
        """
        try:
            response = self.client.databases.query(database_id=self.database_id)
            
            schedule_data = []
            for page in response.get('results', []):
                properties = page.get('properties', {})
                
                # Extract relevant fields
                entry = self._extract_schedule_entry(properties)
                if entry:
                    schedule_data.append(entry)
            
            return schedule_data
        
        except Exception as e:
            raise Exception(f"Error fetching data from Notion: {str(e)}")
    
    def _extract_schedule_entry(self, properties: Dict[str, Any]) -> Dict[str, str]:
        """
        Extract position and name from Notion page properties.
        
        Args:
            properties: Notion page properties
            
        Returns:
            Dictionary with 'position' and 'name' keys
        """
        entry = {}
        
        # Extract position (adjust property names based on your Notion database)
        if 'Position' in properties:
            position_data = properties['Position']
            if position_data.get('type') == 'select':
                entry['position'] = position_data.get('select', {}).get('name', '')
            elif position_data.get('type') == 'title':
                title_array = position_data.get('title', [])
                entry['position'] = title_array[0].get('text', {}).get('content', '') if title_array else ''
        
        # Extract name (adjust property names based on your Notion database)
        if 'Name' in properties:
            name_data = properties['Name']
            if name_data.get('type') == 'rich_text':
                text_array = name_data.get('rich_text', [])
                entry['name'] = text_array[0].get('text', {}).get('content', '') if text_array else ''
            elif name_data.get('type') == 'title':
                title_array = name_data.get('title', [])
                entry['name'] = title_array[0].get('text', {}).get('content', '') if title_array else ''
        
        # Extract date if available
        if 'Date' in properties:
            date_data = properties['Date']
            if date_data.get('type') == 'date':
                date_value = date_data.get('date')
                if date_value:
                    entry['date'] = date_value.get('start', '')
        
        return entry if 'position' in entry and 'name' in entry else None

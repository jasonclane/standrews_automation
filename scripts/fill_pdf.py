from pdfrw import PdfReader, PdfWriter, PdfDict
import json

data = json.load(open('data/this_week.json'))

fields = {
    'Date': data.get('date', ''),
    'Service Time': data.get('service_time', ''),
    'Lay Eucharistic Ministers': ', '.join(data.get('lay_eucharistic_ministers', [])),
    'Lay Readers': ', '.join(data.get('lay_readers', [])),
    'SCRIPTURE & PSALM': data.get('scripture_psalm', ''),
    'PRAYERS': data.get('prayers', ''),
    'Hospitality (Coffee/Donuts)': ', '.join(data.get('hospitality', [])),
    'Prayer Partners': ', '.join(data.get('prayer_partners', [])),
    'Ushers': ', '.join(data.get('ushers', [])),
    'Greeters': ', '.join(data.get('greeters', [])),
    'CRUCIFER': data.get('crucifer', ''),
    'TORCHBEARER_1': data.get('torchbearer_1', ''),
    'TORCHBEARER_2': data.get('torchbearer_2', ''),
    'TEAM LEAD': data.get('team_lead', ''),
}

pdf = PdfReader('pdfs/blank/WorshipTeam_Official.pdf')
for page in pdf.pages:
    if getattr(page, 'Annots', None):
        for annot in page.Annots or []:
            if annot.Subtype == '/Widget' and annot.T:
                name = annot.T[1:-1]
                if name in fields:
                    annot.V = PdfDict(v=str(fields[name]))
                    annot.AP = None

PdfWriter().write('pdfs/output/WorshipTeam_Filled.pdf', pdf)
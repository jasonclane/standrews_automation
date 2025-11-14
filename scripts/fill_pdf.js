import fs from 'fs';
import { PDFDocument } from 'pdf-lib';

const data = JSON.parse(fs.readFileSync('data/this_week.json', 'utf8'));

const fieldText = {
  DATE: data.date,
  SERVICE_TIME: data.service_time,
  LEMS: (data.lay_eucharistic_ministers || []).join(', '),
  LAY_READERS: (data.lay_readers || []).join(', '),
  SCRIPTURE_PsALM: data.scripture_psalm || '',
  PRAYERS: data.prayers || '',
  HOSPITALITY: (data.hospitality || []).join(', '),
  PRAYER_PARTNERS: (data.prayer_partners || []).join(', '),
  USHERS: (data.ushers || []).join(', '),
  GREETERS: (data.greeters || []).join(', '),
  CRUCIFER: data.crucifer || '',
  TORCH1: data.torchbearer_1 || '',
  TORCH2: data.torchbearer_2 || '',
  TEAM_LEAD: data.team_lead || ''
};

async function main() {
  const pdfBytes = fs.readFileSync('pdfs/blank/WorshipTeam_Official.pdf');
  const pdfDoc = await PDFDocument.load(pdfBytes);
  const form = pdfDoc.getForm();

  // Map these names to the actual AcroForm field names in your PDF.
  const map = {
    DATE: 'Date',
    SERVICE_TIME: 'Service Time',
    LEMS: 'Lay Eucharistic Ministers',
    LAY_READERS: 'Lay Readers',
    SCRIPTURE_PsALM: 'SCRIPTURE & PSALM',
    PRAYERS: 'PRAYERS',
    HOSPITALITY: 'Hospitality (Coffee/Donuts)',
    PRAYER_PARTNERS: 'Prayer Partners',
    USHERS: 'Ushers',
    GREETERS: 'Greeters',
    CRUCIFER: 'CRUCIFER',
    TORCH1: 'TORCHBEARER_1',
    TORCH2: 'TORCHBEARER_2',
    TEAM_LEAD: 'TEAM LEAD'
  };

  for (const [key, fieldName] of Object.entries(map)) {
    try {
      const f = form.getTextField(fieldName);
      f.setText(fieldText[key] || '');
    } catch (e) {
      console.warn(`Field not found: ${fieldName}`);
    }
  }

  form.updateFieldAppearances();
  const filled = await pdfDoc.save();
  fs.writeFileSync('pdfs/output/WorshipTeam_Filled.pdf', filled);
}

main();
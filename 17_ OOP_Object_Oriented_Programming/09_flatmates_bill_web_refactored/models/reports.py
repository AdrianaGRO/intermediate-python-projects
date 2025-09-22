import webbrowser
import os
from pathlib import Path

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Ensure uploads directory exists and use absolute path
        current_dir = Path(__file__).parent.parent
        upload_dir = current_dir / "uploads"
        upload_dir.mkdir(exist_ok=True)
        
        upload_path = upload_dir / self.filename
        pdf.output(str(upload_path))
        return str(upload_path)


class FileSharer:
    def __init__(self, filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        try:
            # Check if file exists before trying to upload
            if not Path(self.filepath).exists():
                return f"Error: File not found at {self.filepath}"
            
            client = Client(self.api_key)
            new_filelink = client.upload(filepath=self.filepath)
            return new_filelink.url
        except Exception as e:
            error_message = str(e)
            print(f"Error sharing file: {error_message}")
            # Return local file path when upload fails
            if Path(self.filepath).exists():
                return f"PDF generated successfully! File saved locally at: {self.filepath}"
            else:
                return f"Error: Could not generate or share file - {error_message}"
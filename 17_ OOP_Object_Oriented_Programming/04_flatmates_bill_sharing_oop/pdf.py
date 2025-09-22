from fpdf import FPDF
import os
import webbrowser



class PdfReport:
    """Creates a PDF file that contains data about the flatmates such as
    their names, their due amount and the period of the bill."""

    def __init__(self, filename, flatmate1, flatmate2, bill):
        self.filename = filename
        self.flatmate1 = flatmate1
        self.flatmate2 = flatmate2
        self.bill = bill

    def generate(self):
        pdf = FPDF(orientation="L", unit="pt", format="letter")
        pdf.add_page()

        # Add icon
        pdf.image("17_ OOP_Object_Oriented_Programming/ 04_flatmates_bill_sharing_oop/files/house.png", w=30, h=30)

        # Add title
        pdf.set_font(family="Times", size=54, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.ln(20)

        # Add period label and value
        pdf.set_font(family="Times", size=24)
        pdf.cell(w=100, h=40, txt=f"Period: {self.bill.period}", border=0, ln=1)

        pdf.ln(20)

        # Add the name of the first flatmate and how much they have to pay
        pdf.cell(w=150, h=25, txt=f"{self.flatmate1.name} pays:", border=0)
        pdf.multi_cell(
            w=400, h=25,
            txt=f"${self.flatmate1.pays(self.bill, self.flatmate2):.2f}, because they stayed {self.flatmate1.days_in_house} days and the percentage of the bill is {self.flatmate1.pays(self.bill, self.flatmate2) / self.bill.amount * 100:.2f}%",
            border=0
        )
        pdf.ln(20)

        # Add the name of the second flatmate and how much they have to pay
        pdf.cell(w=150, h=25, txt=f"{self.flatmate2.name} pays:", border=0)
        pdf.multi_cell(
            w=400, h=25,
            txt=f"${self.flatmate2.pays(self.bill, self.flatmate1):.2f}, because they stayed {self.flatmate2.days_in_house} days and the percentage of the bill is {self.flatmate2.pays(self.bill, self.flatmate1) / self.bill.amount * 100:.2f}%",
            border=0
        )

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        pdf.output(self.filename)
        
        # Open the PDF file in the default viewer
        abs_path = os.path.abspath(self.filename)
        if os.path.exists(abs_path):
            webbrowser.open('file://' + abs_path)
        else:
            print(f"PDF not found at {abs_path}")


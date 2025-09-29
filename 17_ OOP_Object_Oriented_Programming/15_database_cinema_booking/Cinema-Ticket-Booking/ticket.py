
import sqlite3
from fpdf import FPDF

class Ticket:
    def __init__(self, ticket_id, user, price, seat):
        self.id = ticket_id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Cinema Ticket", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Ticket ID: {self.id}", ln=True)
        pdf.cell(200, 10, txt=f"User: {self.user}", ln=True)
        pdf.cell(200, 10, txt=f"Seat: {self.seat}", ln=True)
        pdf.cell(200, 10, txt=f"Price: {self.price}", ln=True)
        pdf.output(path)

    def save_to_db(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tickets (user, price, seat) VALUES (?, ?, ?)",
                       (str(self.user), self.price, str(self.seat)))
        connection.commit()
        connection.close()
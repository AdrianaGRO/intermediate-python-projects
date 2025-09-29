import sqlite3
from ticket import Ticket
from seat import Seat
from card import Card


class User:
    def load_tickets(self):
        # Placeholder: Load tickets for the user from the database if needed
        self.tickets = []
    def __init__(self, name):
        self.name = name
        self.card = None
        self.id = None
        self.balance = 0.0
        self.tickets = []
        self.load_user()
        self.load_tickets()

    def load_user(self):
        customer = self.name if self.name else input("Enter your name: ")
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM User WHERE name = ?""", (customer,))
        record = cursor.fetchone()
        if record:
            self.id = record[0]
            self.name = record[1]
            print(f"Welcome back, {self.name}!")
        else:
            cursor.execute("""INSERT INTO User (name) VALUES (?)""", (customer,))
            connection.commit()
            self.id = cursor.lastrowid
            self.name = customer
            print(f"New user created. Welcome, {self.name}!")
        connection.close()

    def check_seat_availability(self):
        while True:
            seat_id = input("Enter the seat ID you want to book (e.g., A1, B2): ")
            connection = sqlite3.connect("cinema.db")
            cursor = connection.cursor()
            cursor.execute("SELECT taken FROM Seat WHERE seat_id = ?", (seat_id,))
            result = cursor.fetchone()
            if result is None:
                print(f"Seat {seat_id} does not exist. Please choose a valid seat from the list.")
                connection.close()
                continue
            if result[0] == 0:
                print(f"Seat {seat_id} is available.")
                connection.close()
                return seat_id
            else:
                print(f"Seat {seat_id} is already taken. Please choose another seat.")
                connection.close()

    def check_balance(self, price):
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT balance FROM Card WHERE user_id = ?""", (self.id,))
        record = cursor.fetchone()
        if record:
            self.balance = record[0]
            if self.balance < price:
                print(f"I am sorry, you do not have enough balance to book this seat. Your current balance is ${self.balance:.2f}. Please top up your card.")
                connection.close()
                return False
            else:
                print("Transaction is successful.")
                self.balance -= price
                cursor.execute("""UPDATE Card SET balance = ? WHERE user_id = ?""", (self.balance, self.id))
                connection.commit()
                connection.close()
                return True
        connection.close()
        return False

    def buy(self, seat, card):
        if seat.is_free():
            if card.validate(seat.price):
                seat.occupy()
                card.deduct(seat.price)
                ticket_id = 1  # This should be replaced with the actual ticket ID generation logic
                ticket = Ticket(ticket_id, self.name, seat.price, seat.seat_id)
                pdf_filename = f"/Users/adricati/Personal Development/intermediate-python-projects/17_ OOP_Object_Oriented_Programming/15_database_cinema_booking/Cinema-Ticket-Booking/ticket_{self.name}_{seat.seat_id}.pdf"
                ticket.to_pdf(pdf_filename)
                ticket.save_to_db()
                print(f"Purchase successful! Ticket generated: {pdf_filename}")
            else:
                print("Insufficient balance on card.")
        else:
            print("Seat is already taken.")


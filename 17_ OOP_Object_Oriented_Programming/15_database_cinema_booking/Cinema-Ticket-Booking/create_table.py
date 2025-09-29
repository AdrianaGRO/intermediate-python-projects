
import sqlite3

# Create User table in cinema.db if not exists
cinema_conn = sqlite3.connect('cinema.db')
cinema_cursor = cinema_conn.cursor()
cinema_cursor.execute('''CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)''')
cinema_conn.commit()

# Create Seat table in cinema.db if not exists
cinema_cursor.execute('''CREATE TABLE IF NOT EXISTS Seat (
    seat_id TEXT PRIMARY KEY,
    price REAL NOT NULL,
    taken INTEGER DEFAULT 0
)''')
cinema_conn.commit()

# Create tickets table in cinema.db if not exists
cinema_cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    price REAL NOT NULL,
    seat TEXT NOT NULL
)''')
cinema_conn.commit()

# Insert seats (A1-H10) if not already present
import string
rows = list(string.ascii_uppercase[:8])  # A-H
cols = range(1, 11)  # 1-10
for row in rows:
    for col in cols:
        seat_id = f"{row}{col}"
        # Example pricing: front rows more expensive
        price = 20.0 if row in ['A', 'B'] else 15.0 if row in ['C', 'D', 'E'] else 10.0
        cinema_cursor.execute("SELECT seat_id FROM Seat WHERE seat_id = ?", (seat_id,))
        if not cinema_cursor.fetchone():
            cinema_cursor.execute("INSERT INTO Seat (seat_id, price, taken) VALUES (?, ?, 0)", (seat_id, price))
cinema_conn.commit()

# Create Card table in banking.db if not exists
banking_conn = sqlite3.connect('banking.db')
banking_cursor = banking_conn.cursor()
banking_cursor.execute('''CREATE TABLE IF NOT EXISTS Card (
    user_id INTEGER PRIMARY KEY,
    type TEXT,
    number TEXT,
    cvc TEXT,
    holder TEXT,
    balance REAL
)''')
banking_conn.commit()

# Optional: print confirmation
print("User table ensured in cinema.db.")
print("Card table ensured in banking.db.")

cinema_conn.close()
banking_conn.close()
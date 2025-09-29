import sqlite3

class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.price = self.get_price()
        self.taken = self.get_taken_status()

    def is_free(self):
        return self.taken == 0
    
    def occupy(self):
        if self.is_free():
            connection = sqlite3.connect("cinema.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE Seat SET taken = 1 WHERE seat_id = ?", (self.seat_id,))
            connection.commit()
            connection.close()
            self.taken = 1

    def get_price(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute("SELECT price FROM Seat WHERE seat_id = ?", (self.seat_id,))
        record = cursor.fetchone()
        connection.close()
        return record[0] if record else None

    def get_taken_status(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute("SELECT taken FROM Seat WHERE seat_id = ?", (self.seat_id,))
        record = cursor.fetchone()
        connection.close()
        return record[0] if record else None



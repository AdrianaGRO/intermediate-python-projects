import sqlite3

class Card:
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.type = None
        self.number = None
        self.cvc = None
        self.holder = None
        self.balance = 0.0
        self.load_card()
        
    def load_card(self):
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Card WHERE user_id = ?", (self.user_id,))
        record = cursor.fetchone()
        if record:
            self.type = record[1]
            self.number = record[2]
            self.cvc = record[3]
            self.holder = record[4]
            self.balance = record[5]
        connection.close()

    def validate(self, price):
        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Card WHERE user_id = ?", (self.user_id,))
        record = cursor.fetchone()
        if record:
            self.type = record[1]
            self.number = record[2]
            self.cvc = record[3]
            self.holder = record[4]
            self.balance = record[5]
            if self.balance >= price:
                print(f"Card validated. Current balance: ${self.balance:.2f}")
                connection.close()
                return True
            else:
                print(f"Insufficient balance. Current balance: ${self.balance:.2f}")
                connection.close()
                return False
        else:
            print("No card found for this user.")
            connection.close()
            return False
        
    def deduct(self, price):
        if self.balance >= price:
            self.balance -= price
            connection = sqlite3.connect("banking.db")
            cursor = connection.cursor()
            cursor.execute("UPDATE Card SET balance = ? WHERE user_id = ?", (self.balance, self.user_id))
            connection.commit()
            connection.close()
            print(f"${price:.2f} deducted. New balance: ${self.balance:.2f}")
        else:
            
            print("Insufficient balance.")

import sqlite3

def create_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""CREATE TABLE "Seat" (
    "seat_id"	TEXT,
    "taken"	INTEGER,
    "price"	REAL
);""")

    connection.commit()
    connection.close()
    print("Table created successfully.")


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""INSERT INTO Seat ("seat_id", "taken", "price") VALUES ('A1', 0, 10.0), ('A2', 0, 10.0), ('A3', 0, 10.0);""")
    connection.commit()
    connection.close()
    print("Record inserted successfully.")

# insert_record()

def fetch_records():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Seat""")
    records = cursor.fetchall()
    connection.close()
    return records

print(f"This are all the entries in the Seat table: {fetch_records()}")

def specific_fetch(seat_id):
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Seat WHERE seat_id = ?""", (seat_id,))
    records = cursor.fetchall()
    connection.close()
    return records

print(f"This is the result of specific_fetch('A1'): {specific_fetch('A1')}")

def specific_column_fetch(column):
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    query = f"SELECT {column} FROM Seat"
    cursor.execute(query)
    records = cursor.fetchall()
    connection.close()
    return records

print(f"This is the result of specific_column_fetch('price'): {specific_column_fetch('price')}")

def select_with_condition(price):
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Seat WHERE price > ?""", (price,))
    records = cursor.fetchall()
    if len(records) == 0:
        return "No records found with the specified condition."
    connection.close()
    return records

print(f"This is the result of select_with_condition: {select_with_condition(11.0)}")



def update_record(seat_id, taken):
    connection = sqlite3.connect("cinema.db")
    connection.execute("""UPDATE Seat SET taken = ? WHERE seat_id = ?""", (taken, seat_id))
    connection.commit()
    connection.close()
    print("Record updated successfully.")

update_record('A1', 0)
print(fetch_records())

def update_column(column, value, seat_id):
    connection = sqlite3.connect("cinema.db")
    query = f"UPDATE Seat SET {column} = ? WHERE seat_id = ?"
    connection.execute(query, (value, seat_id))
    connection.commit()
    connection.close()
    print("Column updated successfully.")
    
update_column('price', 80.0, 'A2')
print(f"This are all the entries in the Seat table: {fetch_records()}")

def delete_record(seat_id):
    connection = sqlite3.connect("cinema.db")
    connection.execute("""DELETE FROM Seat WHERE seat_id = ?""", (seat_id,))
    connection.commit()
    connection.close()
    print("Record deleted successfully.")
    
delete_record('A3')
print(f"This are all the entries in the Seat table: {fetch_records()}")

def delete_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""DROP TABLE Seat""")
    connection.commit()
    connection.close()
    print("Table deleted successfully.")
    

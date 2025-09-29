import sqlite3
from user import User
from seat import Seat
from card import Card

def main():
	print("Welcome to the Cinema Ticket Booking System!")
	name = input("Enter your name: ")
	user = User(name)
	card = Card(user.id)
	# If no card found, prompt for card details and create one
	if card.type is None:
		print("No card found for this user. Please enter your card details.")
		card.type = input("Card type (e.g., Visa, MasterCard): ")
		card.number = input("Card number: ")
		card.cvc = input("CVC: ")
		card.holder = input("Card holder name: ")
		while True:
			try:
				card.balance = float(input("Initial card balance: "))
				break
			except ValueError:
				print("Please enter a valid number for balance.")
		# Save card to database
		import sqlite3
		connection = sqlite3.connect("banking.db")
		cursor = connection.cursor()
		cursor.execute("INSERT INTO Card (user_id, type, number, cvc, holder, balance) VALUES (?, ?, ?, ?, ?, ?)",
					   (user.id, card.type, card.number, card.cvc, card.holder, card.balance))
		connection.commit()
		connection.close()
		print("Card created and saved.")

	seat_id = user.check_seat_availability()
	if seat_id:
		seat = Seat(seat_id)
		if user.check_balance(seat.price):
			user.buy(seat, card)
		else:
			print("Transaction failed: insufficient balance.")
	else:
		print("No seat selected or seat unavailable.")

if __name__ == "__main__":
	main()



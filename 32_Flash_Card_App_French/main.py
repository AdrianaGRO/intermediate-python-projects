# --------------------------- Constants ------------------------------- #
import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
# --------------------------- Functions ------------------------------ #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    



def flip_timer():
    global flip_timer
    flip_timer = window.after(3000, func=flip_card)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    global to_learn, current_card
    # Remove the card by value, not by object identity
    to_learn = [card for card in to_learn if card != current_card]
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- FLASH CARD UI ------------------------------- #

window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

my_image_right = tk.PhotoImage(file="images/right.png")
right_button= tk.Button(image=my_image_right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)  
my_image_wrong = tk.PhotoImage(file="images/wrong.png")
wrong_button= tk.Button(image=my_image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# Show the first card automatically when the app starts
next_card()

window.mainloop()
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import json
import tkinter.font as font
from tkmacosx import Button
import tkinter.font as font


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password and insert it into the password entry field.
    """    
    password_entry.delete(0, tk.END)
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_characters = letters + numbers + symbols
    password = "".join(random.sample(password_characters, 12))
    password_entry.insert(0, password)
    
    # Copy the generated password to clipboard
    pyperclip.copy(password)
    

def find_password():
    """Find the password for the given website and display it in a message box.
    """
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save the password information to a file and delete the entries after saving.
    """
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }
    
    #Validation to check if any field is empty
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        #Read the existing data from the file
        with open("data.json", "r") as data_file:
            try:
                data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            #Update the existing data with new data
            else:
                data.update(new_data)
            
                #Save the updated data back to the file
                with open("data.json", "w") as data_file:   
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=400, height=400)



canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
my_pass_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=my_pass_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(window, text="Search", background="#233361", foreground="#FFFFFF", width=150, command=find_password)
search_button.grid(column=2, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = tk.Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@example.com")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)
password_generate_button = tk.Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

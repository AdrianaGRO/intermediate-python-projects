from cProfile import label
import tkinter as tk

print("Starting GUI...")

root = tk.Tk()
root.title("Miles to Km Converter")
root.config(padx=20, pady=20)
root.geometry("300x150")


# Entry for miles 
input = tk.Entry(width=7)
input.grid(column=1, row=0)

# Labels
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

km_result_label = tk.Label(text="0")
km_result_label.grid(column=1, row=1)


def calculate_km():
    miles = float(input.get())
    km = round(miles * 1.60934)
    km_result_label.config(text=f"{km}")
    
button = tk.Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()

# Set the window size and title
window.geometry("400x400")
window.title("Length Converter App")

# Set colors for the widgets
bg_color = "#f0f0f0"
button_color = "#4CAF50"
entry_color = "#fff"

# Function to perform length conversion
def convert_length():
    try:
        meters = float(entry.get())
        km = meters / 1000
        cm = meters * 100
        mm = meters * 1000

        # Update the labels with the converted values
        km_label.config(text=f"Kilometers: {km:.3f}")
        cm_label.config(text=f"Centimeters: {cm:.3f}")
        mm_label.config(text=f"Millimeters: {mm:.3f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Header label
header_label = tk.Label(window, text="Meters to Length Units Converter", font=("Arial", 16), bg=bg_color)
header_label.pack(pady=20)

# Entry widget for user input
entry_label = tk.Label(window, text="Enter value in meters:", bg=bg_color)
entry_label.pack(pady=5)

entry = tk.Entry(window, width=20, bg=entry_color)
entry.pack(pady=5)

# Button to trigger the conversion
convert_button = tk.Button(window, text="Convert", command=convert_length, bg=button_color, fg="white")
convert_button.pack(pady=20)

# Labels to display the results
km_label = tk.Label(window, text="Kilometers: ", bg=bg_color)
km_label.pack(pady=5)

cm_label = tk.Label(window, text="Centimeters: ", bg=bg_color)
cm_label.pack(pady=5)

mm_label = tk.Label(window, text="Millimeters: ", bg=bg_color)
mm_label.pack(pady=5)

# Set the background color of the window
window.configure(bg=bg_color)
window.mainloop()

import tkinter as tk
from tkinter import messagebox

# Function to evaluate password strength
def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length <= 5:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", fg="lightgreen")
    else:
        strength_label.config(text="Very Strong", fg="darkgreen")

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Define the background color for the window and widget colors
bg_color = "#f0f0f0"
label_color = "#333333"
entry_color = "#ffffff"
button_color = "#00796b"

# Set the background color for the window
root.configure(bg=bg_color)

# Create Labels and Entry Widget for Password Input
password_label = tk.Label(root, text="Enter Password:", bg=bg_color, fg=label_color, font=("Arial", 12))
password_label.pack(pady=20)

password_entry = tk.Entry(root, show="*", bg=entry_color, width=30)
password_entry.pack(pady=10)

# Create a button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength, bg=button_color, fg="white", font=("Arial", 12))
check_button.pack(pady=20)

# Create a label to display the password strength
strength_label = tk.Label(root, text="Password Strength: ", bg=bg_color, fg=label_color, font=("Arial", 12))
strength_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

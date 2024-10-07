import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest and compound interest
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        # Calculate simple interest
        simple_interest = (principal * time * rate) / 100

        # Calculate compound interest (assuming it's compounded annually)
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display the results in labels
        si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        ci_label.config(text=f"Compound Interest: {compound_interest:.2f}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
window = tk.Tk()
window.geometry("400x400")
window.title("Interest Calculator App")

# Define background color for the window and widget colors
bg_color = "#e0f7fa"
label_color = "#004d40"
entry_color = "#ffffff"
button_color = "#00796b"
result_color = "#004d40"

# Set the background color for the window
window.configure(bg=bg_color)

# Create Labels and Entry Widgets for Principal, Time, and Rate of Interest
principal_label = tk.Label(window, text="Principal:", bg=bg_color, fg=label_color, font=("Arial", 12))
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
principal_entry = tk.Entry(window, bg=entry_color, width=20)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

time_label = tk.Label(window, text="Time (Years):", bg=bg_color, fg=label_color, font=("Arial", 12))
time_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
time_entry = tk.Entry(window, bg=entry_color, width=20)
time_entry.grid(row=1, column=1, padx=10, pady=10)

rate_label = tk.Label(window, text="Rate of Interest (%):", bg=bg_color, fg=label_color, font=("Arial", 12))
rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
rate_entry = tk.Entry(window, bg=entry_color, width=20)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to calculate interest
calculate_button = tk.Button(window, text="Calculate Interest", command=calculate_interest, bg=button_color, fg="white", font=("Arial", 12))
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Create labels to display the results for Simple Interest and Compound Interest
si_label = tk.Label(window, text="Simple Interest: ", bg=bg_color, fg=result_color, font=("Arial", 12))
si_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ci_label = tk.Label(window, text="Compound Interest: ", bg=bg_color, fg=result_color, font=("Arial", 12))
ci_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()

import tkinter as tk
import random
from tkinter import messagebox

# Function to decide the winner
def determine_winner(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
    else:
        result = "Computer wins!"

    # Update the result label with the outcome
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissor")

# Set background color for the window
bg_color = "#e0f7fa"
root.configure(bg=bg_color)

# Create a label to prompt the user
prompt_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg=bg_color, font=("Arial", 14))
prompt_label.pack(pady=20)

# Create buttons for user choices: Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner('Rock'), font=("Arial", 12), width=10, bg="#00796b", fg="white")
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner('Paper'), font=("Arial", 12), width=10, bg="#00796b", fg="white")
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner('Scissors'), font=("Arial", 12), width=10, bg="#00796b", fg="white")
scissors_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", bg=bg_color, font=("Arial", 14))
result_label.pack(pady=30)

# Run the Tkinter event loop
root.mainloop()

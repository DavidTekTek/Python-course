import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main window (text editor)
window = tk.Tk()
window.title("Codingal Text Editor")
window.geometry("600x400")

# Create a Text Widget (for editing and displaying text)
text_area = tk.Text(window, wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# File handling functions
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)  # Clear the text area before loading new content
                text_area.insert(tk.INSERT, content)  # Insert the file content into the text area
                window.title(f"Simple Text Editor - {file_path}")  # Update the window title with file name
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                content = text_area.get(1.0, tk.END)  # Get all content from the text area
                file.write(content)
                window.title(f"Simple Text Editor - {file_path}")  # Update the window title with saved file name
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

# Create a Menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add Open, Save, and Exit options to the File menu
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

window.mainloop()


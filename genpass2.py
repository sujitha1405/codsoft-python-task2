import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 or more to include all character types.")

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation 

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + special_chars
    password += [random.choice(all_characters) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

def generate_password_gui():
    try:
        length = int(entry.get())
        if length < 4:
            raise ValueError("Password length must be at least 4.")
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Add label
label = tk.Label(root, text="Enter the desired length of the password:")
label.pack(pady=10)

# Add entry field
entry = tk.Entry(root)
entry.pack(pady=5)

# Add button to generate password
button = tk.Button(root, text="Generate Password", command=generate_password_gui)
button.pack(pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()

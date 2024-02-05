import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo("Error", "Please enable at least one category of characters.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_save_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, purpose):
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    if password:
        save_to_file(password, purpose)

def save_to_file(password, purpose):
    filename = "Passwords.txt"
    with open(filename, "a") as file:
        file.write(f"Purpose: {purpose}, Password: {password}\n")
        messagebox.showinfo("File Updated", f"Password for {purpose} has been added to '{filename}'")

def generate_password_gui():
    root = tk.Tk()
    root.title("Password Generator")

    root.iconbitmap("Lock.ico")

    root.geometry("500x450")
    background_image = tk.PhotoImage(file="Bg.gif")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    background_label.image = background_image
    background_label.config(bg="white", bd=0)

    label1 = tk.Label(root, text="Enter the purpose of the password:", font=("Comic Sans MS", 14), bg="black", fg="white")
    label1.pack(pady=5)

    purpose_entry = tk.Entry(root, font=("Comic Sans MS", 14))
    purpose_entry.pack(pady=5)

    label2 = tk.Label(root, text="Enter the length of the password:", font=("Comic Sans MS", 14), bg="black", fg="white")
    label2.pack(pady=5)

    length_entry = tk.Entry(root, font=("Comic Sans MS", 14))
    length_entry.pack(pady=5)

    uppercase_var = tk.BooleanVar(value=True)
    uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var, font=("Comic Sans MS", 14))
    uppercase_checkbox.pack(pady=5)

    lowercase_var = tk.BooleanVar(value=True)
    lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var, font=("Comic Sans MS", 14))
    lowercase_checkbox.pack(pady=5)

    digits_var = tk.BooleanVar(value=True)
    digits_checkbox = tk.Checkbutton(root, text="Include digits", variable=digits_var, font=("Comic Sans MS", 14))
    digits_checkbox.pack(pady=5)

    special_chars_var = tk.BooleanVar(value=True)
    special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, font=("Comic Sans MS", 14))
    special_chars_checkbox.pack(pady=5)

    generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_password_command(purpose_entry, length_entry, uppercase_var, lowercase_var, digits_var, special_chars_var), font=("Comic Sans MS", 14), bg="black", fg="white")
    generate_button.pack(pady=10)

    root.mainloop()

def generate_password_command(purpose_entry, length_entry, uppercase_var, lowercase_var, digits_var, special_chars_var):
    purpose = purpose_entry.get()
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    generate_and_save_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, purpose)

if __name__ == "__main__":
    generate_password_gui()

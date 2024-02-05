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
    filename = "generated_passwords.txt"
    with open(filename, "a") as file:
        file.write(f"Purpose: {purpose}, Password: {password}\n")
        messagebox.showinfo("File Updated", f"Password for {purpose} has been added to '{filename}'")

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.label = tk.Label(master, text="Enter the purpose of the password:")
        self.label.pack()

        self.purpose_entry = tk.Entry(master)
        self.purpose_entry.pack()

        self.length_label = tk.Label(master, text="Enter the length of the password:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.uppercase_var = tk.BooleanVar(value=True)
        self.uppercase_checkbox = tk.Checkbutton(master, text="Include uppercase letters", variable=self.uppercase_var)
        self.uppercase_checkbox.pack()

        self.lowercase_var = tk.BooleanVar(value=True)
        self.lowercase_checkbox = tk.Checkbutton(master, text="Include lowercase letters", variable=self.lowercase_var)
        self.lowercase_checkbox.pack()

        self.digits_var = tk.BooleanVar(value=True)
        self.digits_checkbox = tk.Checkbutton(master, text="Include digits", variable=self.digits_var)
        self.digits_checkbox.pack()

        self.special_chars_var = tk.BooleanVar(value=True)
        self.special_chars_checkbox = tk.Checkbutton(master, text="Include special characters", variable=self.special_chars_var)
        self.special_chars_checkbox.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        purpose = self.purpose_entry.get()
        length = int(self.length_entry.get())
        use_uppercase = self.uppercase_var.get()
        use_lowercase = self.lowercase_var.get()
        use_digits = self.digits_var.get()
        use_special_chars = self.special_chars_var.get()

        generate_and_save_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, purpose)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

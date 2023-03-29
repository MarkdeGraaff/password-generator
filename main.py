import tkinter as tk
from tkinter import ttk
import secrets
import string


class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x250")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.options_frame = ttk.Frame(self)
        self.options_frame.pack(pady=15)

        self.var_uppercase = tk.BooleanVar(value=True)
        self.check_uppercase = ttk.Checkbutton(
            self.options_frame, text="Uppercase (A-Z)", variable=self.var_uppercase)
        self.check_uppercase.grid(row=0, column=0, padx=5, pady=5)

        self.var_lowercase = tk.BooleanVar(value=True)
        self.check_lowercase = ttk.Checkbutton(self.options_frame, text="Lowercase (a-z)", variable=self.var_lowercase)
        self.check_lowercase.grid(row=0, column=1, padx=5, pady=5)

        self.var_numbers = tk.BooleanVar(value=True)
        self.check_numbers = ttk.Checkbutton(self.options_frame, text="Numbers (0-9)", variable=self.var_numbers)
        self.check_numbers.grid(row=1, column=0, padx=5, pady=5)

        self.var_symbols = tk.BooleanVar(value=True)
        self.check_symbols = ttk.Checkbutton(self.options_frame, text="Symbols (#,@,*,...)", variable=self.var_symbols)
        self.check_symbols.grid(row=1, column=1, padx=5, pady=5)

        self.length_label = ttk.Label(self, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = ttk.Entry(self)
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")

        self.generated_password = ttk.Entry(self, state="readonly")
        self.generated_password.pack(pady=5)

        self.generate_button = ttk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())
        characters = ""

        if self.var_uppercase.get():
            characters += string.ascii_uppercase
        if self.var_lowercase.get():
            characters += string.ascii_lowercase
        if self.var_numbers.get():
            characters += string.digits
        if self.var_symbols.get():
            characters += string.punctuation

        password = ''.join(secrets.choice(characters) for _ in range(length))

        self.generated_password.config(state="normal")
        self.generated_password.delete(0, tk.END)
        self.generated_password.insert(0, password)
        self.generated_password.config(state="readonly")


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()

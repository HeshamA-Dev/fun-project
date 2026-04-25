import tkinter as tk


class FakeCalculatorApp:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("300x300")
        self.window.title("Fake Calculator")
        self.window.configure(bg="darkred")

        label = tk.Label(
            self.window,
            text="This is a fake calculator",
            font=("Arial", 18),
            bg="darkred",
            fg="white"
        )

        label.pack(pady=60)

        close_button = tk.Button(
            self.window,
            text="Click me to close",
            command=self.window.destroy
        )

        close_button.pack()
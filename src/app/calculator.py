import tkinter as tk


class CalculatorApp:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("300x400")
        self.window.title("Calculator")
        self.window.configure(bg="gray")

        self.current_text = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Label(
            self.window,
            text="",
            font=("Arial", 24),
            bg="white",
            fg="black",
            anchor="e"
        )

        self.display.pack(
            fill="x",
            padx=10,
            pady=10,
            ipady=10
        )

        self.button_frame = tk.Frame(
            self.window,
            bg="gray"
        )

        self.button_frame.pack(
            expand=True,
            fill="both"
        )

        button_texts = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"
        ]

        row = 0
        column = 0

        for text in button_texts:
            button = tk.Button(
                self.button_frame,
                text=text,
                font=("Arial", 18),
                command=lambda value=text: self.button_clicked(value)
            )

            button.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=2,
                pady=2
            )

            column += 1

            if column == 4:
                column = 0
                row += 1

        for i in range(4):
            self.button_frame.columnconfigure(i, weight=1)

        for i in range(4):
            self.button_frame.rowconfigure(i, weight=1)

    def button_clicked(self, value):
        if value == "C":
            self.current_text = ""
            self.display.config(text=self.current_text)

        elif value == "=":
            try:
                result = eval(self.current_text)
                self.current_text = str(result)
                self.display.config(text=self.current_text)
            except:
                self.current_text = ""
                self.display.config(text="Error")

        else:
            self.current_text += value
            self.display.config(text=self.current_text)
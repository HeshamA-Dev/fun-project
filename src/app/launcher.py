import tkinter as tk
from tkinter import PhotoImage

from calculator import CalculatorApp
from fake_calculator import FakeCalculatorApp


class AppLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.configure(bg="black")
        self.root.title("Mini Desktop")

        self.icons = []

        #buttons will be here automated
        self.apps = [
            {
                "name": "Calculator",
                "icon": "imgs/icon_calc.png",
                "command": self.open_calculator
            },
            {
                "name": "Fake Calculator",
                "icon": "imgs/icon_calc_1.png",
                "command": self.open_fake_calculator
            }
        ]

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Pick An App",
            font=("Arial", 22),
            bg="black",
            fg="white"
        )

        title.pack(pady=20)

        self.desktop_frame = tk.Frame(
            self.root,
            bg="black"
        )

        self.desktop_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.create_app_grid()

    def create_app_grid(self):
        columns = 4

        for index, app in enumerate(self.apps):
            row = index // columns
            column = index % columns

            app_icon = PhotoImage(file=app["icon"])
            app_icon = app_icon.subsample(3, 3)

            self.icons.append(app_icon)

            app_button = tk.Button(
                self.desktop_frame,
                image=app_icon,
                text=app["name"],
                compound="top",
                command=app["command"],
                bg="black",
                fg="white",
                activebackground="gray",
                activeforeground="white",
                borderwidth=0
            )

            app_button.grid(
                row=row,
                column=column,
                padx=20,
                pady=20,
                sticky="nsew"
            )

        for column in range(columns):
            self.desktop_frame.columnconfigure(column, weight=1)

    def open_calculator(self):
        CalculatorApp()

    def open_fake_calculator(self):
        FakeCalculatorApp()

    def run(self):
        self.root.mainloop()
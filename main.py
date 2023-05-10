import tkinter as tk
import math
import winsound


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("CASIO fx-991ex")

        # Configure main frame
        main_frame = tk.Frame(master, bg="gray", padx=0, pady=0)
        main_frame.pack(expand=True)

        # Create header frame
        header_frame = tk.Frame(main_frame, bg="gray")
        header_frame.pack()

        # Create header labels
        casio_label = tk.Label(header_frame, text="CASIO", font=("Eurostile", 30, "bold"), fg="dark blue", bg="gray")
        casio_label.pack()
        fx_label = tk.Label(header_frame, text="fx-991ex", font=("Helvetica", 10, "italic"), fg="black", bg="gray")
        fx_label.pack()

        # Create display
        self.display = tk.Entry(main_frame, width=50, font=("Helvetica", 20), justify="right", bd=5)
        self.display.pack(pady=20)

        # Create buttons
        button_frame = tk.Frame(main_frame, bg="gray")
        button_frame.pack()

        buttons = [
            "7", "8", "9", "/", "C",
            "4", "5", "6", "*", "^2",
            "1", "2", "3", "-", "sqrt",
            "0", ".", "=", "+", "Close",
            "sin", "cos", "tan"
        ]

        for button in buttons:
            button_col = self.get_button_col(button)
            tk.Button(button_frame, text=button, font=("Helvetica", 15), width=7, height=2,
                      command=lambda text=button: self.button_click(text), bg=button_col).grid(
                row=buttons.index(button) // 5, column=buttons.index(button) % 5, padx=5, pady=5)

    def get_button_col(self, text):
        cols = {
            "7": "white",
            "8": "white",
            "9": "white",
            "/": "orange",
            "4": "white",
            "5": "white",
            "6": "white",
            "*": "orange",
            "1": "white",
            "2": "white",
            "3": "white",
            "-": "orange",
            "0": "white",
            ".": "white",
            "=": "orange",
            "+": "orange",
            "C": "red",
            "Close": "red",
            "sin": "white",
            "cos": "white",
            "tan": "white",
            "^2": "white",
            "sqrt": "white"
        }
        return cols[text]

    def button_click(self, text):
        winsound.Beep(2000, 100)
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "Close":
            self.master.destroy()
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "sqrt":
            num = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, math.sqrt(num))
        elif text == "sin":
            num = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, math.sin(math.radians(num)))
        elif text == "cos":
            num = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, math.cos(math.radians(num)))
        elif text == "tan":
            num = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, math.tan(math.radians(num)))
        elif text == "^2":
            num = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, num**2)
        else:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + str(text))

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()

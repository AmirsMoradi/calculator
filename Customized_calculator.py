import customtkinter as ctk
import math

class CustomCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My CustomTkinter Calculator")
        self.root.geometry("500x600")
        self.expression = ""
        self.input_text = ctk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        input_frame = ctk.CTkFrame(self.root, corner_radius=15)
        input_frame.pack(pady=20)

        input_field = ctk.CTkEntry(input_frame, textvariable=self.input_text, font=("Arial", 24), width=400, height=50, justify="right")
        input_field.pack(padx=10, pady=10)

        btns_frame = ctk.CTkFrame(self.root, corner_radius=15)
        btns_frame.pack(pady=10)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0), ("√", 4, 1), ("x²", 4, 2), ("1/x", 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(btns_frame, text, row, col)

    def create_button(self, frame, text, row, col):
        btn = ctk.CTkButton(
            frame, text=text, font=("Arial", 18, "bold"),
            width=100, height=60,
            fg_color=("gray75", "gray25") if text not in {"=", "C"} else ("green", "red")[text == "C"],
            hover_color=("gray65", "gray35"),
            command=lambda: self.on_button_click(text)
        )
        btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "√":
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "x²":
            try:
                result = str(eval(self.expression) ** 2)
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "1/x":
            try:
                result = str(1 / eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = CustomCalculator(root)
    root.mainloop()

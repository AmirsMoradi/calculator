import tkinter as tk
import math

class CustomCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Unique Calculator")
        self.root.geometry("630x600")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg='lightblue')
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=30, insertwidth=4, width=14, justify='right', bg='lightyellow')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE, bg='lightblue')
        btns_frame.pack()

        self.create_button(btns_frame, "7", 1, 0)
        self.create_button(btns_frame, "8", 1, 1)
        self.create_button(btns_frame, "9", 1, 2)
        self.create_button(btns_frame, "/", 1, 3, 'orange')

        self.create_button(btns_frame, "4", 2, 0)
        self.create_button(btns_frame, "5", 2, 1)
        self.create_button(btns_frame, "6", 2, 2)
        self.create_button(btns_frame, "*", 2, 3, 'orange')

        self.create_button(btns_frame, "1", 3, 0)
        self.create_button(btns_frame, "2", 3, 1)
        self.create_button(btns_frame, "3", 3, 2)
        self.create_button(btns_frame, "-", 3, 3, 'orange')

        self.create_button(btns_frame, "0", 4, 0)
        self.create_button(btns_frame, ".", 4, 1)
        self.create_button(btns_frame, "=", 4, 2, 'green')
        self.create_button(btns_frame, "+", 4, 3, 'orange')

        self.create_button(btns_frame, "C", 5, 0, 'red')
        self.create_button(btns_frame, "√", 5, 1)
        self.create_button(btns_frame, "x²", 5, 2)
        self.create_button(btns_frame, "1/x", 5, 3)

    def create_button(self, frame, text, row, col, color='lightgrey'):
        button = tk.Button(frame, text=text, font=('arial', 18, 'bold'), command=lambda: self.on_button_click(text), height=2, width=9, bg=color)
        button.grid(row=row, column=col, padx=1, pady=1)

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
    root = tk.Tk()
    CustomCalculator(root)
    root.mainloop()
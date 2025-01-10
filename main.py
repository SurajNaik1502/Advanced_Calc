import tkinter as tk
from math import sqrt, pow

# Function Definitions
def click(button_text):
    """Handle button click events."""
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "√":
        try:
            value = float(entry.get())
            result = sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "x²":
        try:
            value = float(entry.get())
            result = pow(value, 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "1/x":
        try:
            value = float(entry.get())
            if value == 0:
                raise ZeroDivisionError
            result = 1 / value
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

# GUI Setup
window = tk.Tk()
window.title("Advanced Calculator")

# Entry widget for user input
entry = tk.Entry(window, font=("Arial", 20), bd=5, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button Layout
buttons = [
    ("C", 1, 0), ("√", 1, 1), ("x²", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("1/x", 5, 2), ("=", 5, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Make the grid cells expand with the window
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

# Run the GUI loop
window.mainloop()

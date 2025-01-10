import tkinter as tk
from math import sin, cos, tan, radians, sqrt, pow

memory = 0

def click(button_text):
    """Handle button click events."""
    global memory
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "M+":
        try:
            memory = float(entry.get())
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "MR":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(memory))
    elif button_text == "MC":
        memory = 0
    elif button_text == "sin":
        try:
            value = float(entry.get())
            result = sin(radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "cos":
        try:
            value = float(entry.get())
            result = cos(radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "tan":
        try:
            value = float(entry.get())
            result = tan(radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

window = tk.Tk()
window.title("Advanced Calculator")

window.configure(bg="#282c34")
button_bg = "#3c4047"
button_fg = "#000"
entry_bg = "#1c1f26"
entry_fg = "#61dafb"

entry = tk.Entry(window, font=("Arial", 20), bd=5, insertwidth=4, width=14, justify="right", bg=entry_bg, fg=entry_fg)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("C", 1, 0), ("M+", 1, 1), ("MR", 1, 2), ("MC", 1, 3), ("/", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3), ("√", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), ("x²", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3), ("1/x", 4, 4),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("sin", 5, 3), ("cos", 5, 4),
    ("tan", 6, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for j in range(5):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()

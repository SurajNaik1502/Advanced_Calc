import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan, radians, degrees, log, log10, sqrt, pow

# Global variables for memory and angle mode
memory = 0
angle_mode = "Degrees"

# Button click handler
def click(button_text):
    """Handle button click events."""
    global memory, angle_mode
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
    elif button_text == "√":
        try:
            value = float(entry.get())
            result = sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "x²":
        try:
            value = float(entry.get())
            result = pow(value, 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
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
    elif button_text in ["sin", "cos", "tan"]:
        try:
            value = float(entry.get())
            angle = radians(value) if angle_mode == "Degrees" else value
            result = sin(angle) if button_text == "sin" else cos(angle) if button_text == "cos" else tan(angle)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text in ["log", "ln"]:
        try:
            value = float(entry.get())
            if value <= 0:
                raise ValueError("Invalid input")
            result = log10(value) if button_text == "log" else log(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "RAD/DEG":
        angle_mode = "Radians" if angle_mode == "Degrees" else "Degrees"
        mode_button.config(text=f"Mode: {angle_mode}")
    else:
        entry.insert(tk.END, button_text)

# Add keyboard support
def key_press(event):
    key = event.keysym
    if key in "0123456789+-*/.=C":
        click(key)
    elif key == "Return":
        click("=")
    elif key == "BackSpace":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])

# GUI Setup
window = tk.Tk()
window.title("Advanced Calculator")
window.configure(bg="#282c34")

# Entry widget
entry = ttk.Entry(window, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# Buttons configuration
buttons = [
    ("C", 1, 0), ("M+", 1, 1), ("MR", 1, 2), ("MC", 1, 3), ("/", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3), ("√", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), ("x²", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3), ("1/x", 4, 4),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("sin", 5, 3), ("cos", 5, 4),
    ("tan", 6, 3), ("log", 6, 4), ("ln", 6, 2),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = ttk.Button(window, text=text, command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Mode button for RAD/DEG toggle
mode_button = ttk.Button(window, text=f"Mode: {angle_mode}", command=lambda: click("RAD/DEG"))
mode_button.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Configure grid expansion
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for j in range(5):
    window.grid_columnconfigure(j, weight=1)

# Bind keyboard events
window.bind("<Key>", key_press)

# Run the main event loop
window.mainloop()

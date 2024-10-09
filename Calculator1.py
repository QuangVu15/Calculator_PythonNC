# Ngô Quang Vũ - 197CT10170
import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field for input
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# List of buttons and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons and attach them to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start Tkinter's event loop
root.mainloop()

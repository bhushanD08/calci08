import tkinter as tk

# Function to update the expression
def press(num):
    current = expression.get()
    expression.set(current + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except Exception:
        expression.set("Error")

# Function to clear the input field
def clear():
    expression.set("")

# Set up main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = tk.StringVar()

# Input field
entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)
    
    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=action).grid(row=row, column=col, sticky="nsew")

# Run the app
root.mainloop()

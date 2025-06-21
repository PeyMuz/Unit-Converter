import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
import itertools

# Window setup
window = tk.Tk()
window.title("Unit Converter")
window.geometry("500x600")
window.configure(bg='#181c20')

# Neon colors
NEON_BLUE = "#00f0ff"
NEON_PINK = "#ff00de"
NEON_GREEN = "#39ff14"
DARK_BG = "#181c20"
ENTRY_BG = "#23272b"
ENTRY_FG = "#00f0ff"

# Unit options and conversion factors (same as before)
unit_options = {
    'Length': ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch'],
    'Mass': ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce'],
    'Volume': ['Liter', 'Milliliter', 'Cubic meter', 'Cubic centimeter', 'Gallon', 'Pint']
}
conversion_factors = {
    'Length': {
        'Meter': 1,
        'Kilometer': 1000,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    },
    'Mass': {
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 0.000001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    },
    'Volume': {
        'Liter': 1,
        'Milliliter': 0.001,
        'Cubic meter': 1000,
        'Cubic centimeter': 0.001,
        'Gallon': 3.78541,
        'Pint': 0.473176
    }
}

# Functions
def select(event=None):
    unit_type = n.get()
    fromdd['values'] = unit_options[unit_type]
    tto['values'] = unit_options[unit_type]
    fromdd.set('')
    tto.set('')
    result_entry.delete(0, tk.END)

def fromfuncc(event=None):
    result_entry.delete(0, tk.END)

def to(event=None):
    result_entry.delete(0, tk.END)

def convert():
    unit_type = n.get()
    from_unit = f.get()
    to_unit = t.get()
    try:
        value = float(number.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if not from_unit or not to_unit:
        messagebox.showerror("Unit Missing", "Please select both units.")
        return

    base_value = value * conversion_factors[unit_type][from_unit]
    result = base_value / conversion_factors[unit_type][to_unit]
    result_entry.delete(0, tk.END)
    result_entry.insert(0, f"{result:.6g}")

# Fonts
font1 = tkFont.Font(family="Consolas", size=30, weight="bold")
font2 = tkFont.Font(family="Consolas", size=10)
font3 = tkFont.Font(family="Consolas", size=20)

# Animated Canvas "Techy" effect
canvas = tk.Canvas(window, width=500, height=80, bg=DARK_BG, highlightthickness=0)
canvas.place(relx=0.5, rely=0.05, anchor='n')
lines = []
for i in range(0, 500, 20):
    line = canvas.create_line(i, 0, i, 80, fill=NEON_BLUE, width=2)
    lines.append(line)

def animate_lines():
    colors = itertools.cycle([NEON_BLUE, NEON_PINK, NEON_GREEN])
    for i, line in enumerate(lines):
        canvas.itemconfig(line, fill=next(colors))
    window.after(120, animate_lines)
animate_lines()

# Title label (centered)
main = tk.Label(window, text="Unit Converter", bg=DARK_BG, fg=NEON_PINK, font=font1)
main.place(relx=0.5, rely=0.18, anchor='center')

# Unit label (centered above combobox)
unit_label = tk.Label(window, text="Select Unit", bg=DARK_BG, fg=NEON_GREEN, font=font2)
unit_label.place(relx=0.5, rely=0.23, anchor='center')

# Main combobox (centered)
n = tk.StringVar()
unit_combobox = ttk.Combobox(window, width=35, textvariable=n, font=font2, state='readonly')
unit_combobox['values'] = ('Length', 'Mass', 'Volume')
unit_combobox.place(relx=0.5, rely=0.28, anchor='center')
unit_combobox.current(0)
unit_combobox.bind("<<ComboboxSelected>>", select)

# From label (left aligned, same row as from combobox)
label_from = tk.Label(window, text="From:", bg=DARK_BG, fg=NEON_BLUE, font=font2)
label_from.place(relx=0.3, rely=0.36, anchor='e')

# From combobox (aligned with label)
f = tk.StringVar()
fromdd = ttk.Combobox(window, width=20, textvariable=f, font=font2, state='readonly')
fromdd.place(relx=0.5, rely=0.36, anchor='center')
fromdd.bind('<<ComboboxSelected>>', fromfuncc)

# number entry
number = tk.Entry(window, width=10, font=font2, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=NEON_PINK)
number.place(relx=0.82, rely=0.37, anchor='center')

# creating to label
to_label = tk.Label(window, text="To:", bg=DARK_BG, fg=NEON_BLUE, font=font2)
to_label.place(relx=0.3, rely=0.44, anchor='e')

# dropdown for to
t = tk.StringVar()
tto = ttk.Combobox(window, width=20, textvariable=t, font=font2, state='readonly')
tto.place(relx=0.5, rely=0.44, anchor='center')
tto.bind('<<ComboboxSelected>>', to)

# result label
result = tk.Label(window, text="Result:", bg=DARK_BG, fg=NEON_GREEN, font=font2)
result.place(relx=0.3, rely=0.52, anchor='e')
# result entry
result_entry = tk.Entry(window, width=20, font=font2, bg=ENTRY_BG, fg=NEON_GREEN, insertbackground=NEON_PINK)
result_entry.place(relx=0.5, rely=0.52, anchor='center')

# Create answer button with hover effect
def on_enter(e):
    answer_button['bg'] = NEON_PINK
    answer_button['fg'] = DARK_BG
def on_leave(e):
    answer_button['bg'] = NEON_GREEN
    answer_button['fg'] = DARK_BG

answer_button = tk.Button(window, text='Answer', width=10, height=2, bg=NEON_GREEN, fg=DARK_BG, font=font2, command=convert, activebackground=NEON_PINK, activeforeground=DARK_BG)
answer_button.place(relx=0.5, rely=0.6, anchor='center')
answer_button.bind("<Enter>", on_enter)
answer_button.bind("<Leave>", on_leave)

# Create the art label
art_label = tk.Label(window, text='BANTOG CORP', width=50, height=2, bg=DARK_BG, fg=NEON_PINK, font=font3)
art_label.place(relx=0.5, rely=0.9, anchor='center')

# Initialize dropdowns
select()

# Mainloop
window.mainloop()
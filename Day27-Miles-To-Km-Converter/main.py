from tkinter import *

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilometer_result_label.config(text=str(km))
    except ValueError:
        kilometer_result_label.config(text="Invalid input")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is Equal Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer result Label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Kilometer Label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
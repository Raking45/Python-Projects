import tkinter as tk 

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("420x180")

# Celsius to Fahrenheit
def celsius_to_fahrenheit():
  degree_symbol = chr(176)
  celsius = float(celsius_entry.get())
  fahrenheit = (celsius * 9 / 5) + 32
  result_label.config(text=f"{celsius}{degree_symbol}C = {fahrenheit}{degree_symbol}F")
  
# Fahrenheit to Celsius
def fahrenheit_to_celsius():
  degree_symbol = chr(176)
  fahrenheit = float(fahrenheit_entry.get())
  celsius = (fahrenheit - 32) * 5 / 9
  result_label.config(text=f"{fahrenheit}{degree_symbol}F = {celsius}{degree_symbol}C")
  
# User Interface

# Celsius to Fahrenheit Conversion Section
celsius_label = tk.Label(window, text="Celsius")
celsius_label.pack()

celsius_entry = tk.Entry(window)
celsius_entry.pack()

celsius_to_fahrenheit_button = tk.Button(window, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack()

# Fahrenheit to Celsius Conversion Section
fahrenheit_label = tk.Label(window, text="Fahrenheit")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.pack()

fahrenheit_to_celsius_button = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack()

# Result Section
result_label = tk.Label(window, text="", bg="lightgreen", pady=3, padx=10, borderwidth=1, relief="solid")
result_label.pack()

window.mainloop()
import tkinter as tk
from tkinter import messagebox

def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': {'INR': 84.0, 'EUR': 0.94, 'GBP': 0.76, 'JPY': 150.0, 'AUD': 1.56, 'CAD': 1.36, 'CHF': 0.91, 'CNY': 7.3, 'MXN': 17.0},
        'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.009, 'JPY': 1.8, 'AUD': 0.019, 'CAD': 0.016, 'CHF': 0.011, 'CNY': 0.088, 'MXN': 0.21},
        'EUR': {'USD': 1.06, 'INR': 88.0, 'GBP': 0.81, 'JPY': 160.0, 'AUD': 1.65, 'CAD': 1.45, 'CHF': 0.97, 'CNY': 7.8, 'MXN': 18.0},
        'GBP': {'USD': 1.32, 'INR': 108.0, 'EUR': 1.23, 'JPY': 198.0, 'AUD': 2.03, 'CAD': 1.79, 'CHF': 1.17, 'CNY': 9.0, 'MXN': 21.0},
        'JPY': {'USD': 0.0067, 'INR': 0.56, 'EUR': 0.0062, 'GBP': 0.0051, 'AUD': 0.010, 'CAD': 0.0091, 'CHF': 0.0061, 'CNY': 0.048, 'MXN': 1.2},
        'AUD': {'USD': 0.64, 'INR': 53.0, 'EUR': 0.61, 'GBP': 0.49, 'JPY': 98.0, 'CAD': 0.87, 'CHF': 0.58, 'CNY': 4.7, 'MXN': 13.0},
        'CAD': {'USD': 0.74, 'INR': 61.0, 'EUR': 0.69, 'GBP': 0.56, 'JPY': 113.0, 'AUD': 1.15, 'CHF': 0.67, 'CNY': 5.4, 'MXN': 14.0},
        'CHF': {'USD': 1.1, 'INR': 91.0, 'EUR': 1.03, 'GBP': 0.85, 'JPY': 165.0, 'AUD': 1.72, 'CAD': 1.5, 'CNY': 8.1, 'MXN': 19.0},
        'CNY': {'USD': 0.14, 'INR': 12.0, 'EUR': 0.13, 'GBP': 0.11, 'JPY': 21.0, 'AUD': 0.21, 'CAD': 0.19, 'CHF': 0.12, 'MXN': 2.5},
        'MXN': {'USD': 0.058, 'INR': 4.7, 'EUR': 0.056, 'GBP': 0.048, 'JPY': 0.84, 'AUD': 0.077, 'CAD': 0.071, 'CHF': 0.053, 'CNY': 0.4}
    }
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return round(amount * exchange_rates[from_currency][to_currency], 2)
    else:
        return None

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from_currency.get().upper()
        to_currency = entry_to_currency.get().upper()

        converted_amount = currency_converter(amount, from_currency, to_currency)
        if converted_amount is not None:
            result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            messagebox.showerror("Error", "Conversion rate not available!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")

# Create the GUI window
window = tk.Tk()
window.title("Currency Converter")

# Input fields and labels
tk.Label(window, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="From Currency (e.g., USD):").grid(row=1, column=0, padx=10, pady=5)
entry_from_currency = tk.Entry(window)
entry_from_currency.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="To Currency (e.g., INR):").grid(row=2, column=0, padx=10, pady=5)
entry_to_currency = tk.Entry(window)
entry_to_currency.grid(row=2, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI loop
window.mainloop()

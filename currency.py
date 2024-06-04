import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = "7a7383a95e65ee9accc6d5f5"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching exchange rates: {response.status_code}")
    
    data = response.json()
    
    if "conversion_rates" not in data:
        raise Exception("Invalid response: 'conversion_rates' key not found")
    
    if to_currency not in data["conversion_rates"]:
        raise Exception(f"Currency '{to_currency}' not found in conversion rates")
    
    return data["conversion_rates"][to_currency]

def convert_currency():
    try:
        from_currency = from_currency_var.get().upper()
        to_currency = to_currency_var.get().upper()
        amount = float(amount_var.get())
        
        if from_currency not in valid_currencies:
            raise Exception(f"Invalid from_currency code: {from_currency}")
        if to_currency not in valid_currencies:
            raise Exception(f"Invalid to_currency code: {to_currency}")
        
        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as e:
        result_var.set(f"Error: {e}")

valid_currencies = [
    "USD", "EUR", "GBP", "INR", "AUD", "CAD", "SGD", "CHF", "MYR", "JPY", "CNY",
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AWG", "AZN", "BAM", "BBD",
    "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP",
    "BYN", "BZD", "CDF", "CLP", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK",
    "DOP", "DZD", "EGP", "ERN", "ETB", "FJD", "FKP", "FOK", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "IMP", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "KES", "KGS", "KHR",
    "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL",
    "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR",
    "MWK", "MXN", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB",
    "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF",
    "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD",
    "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TVD", "TWD", "TZS", "UAH", "UGX", "UYU", "UZS", "VES", "VND", "VUV", "WST",
    "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
]

root = tk.Tk()
root.title("Currency Converter")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), foreground="blue")
style.configure("TButton", font=("Arial", 12), foreground="black", background="red")
style.configure("TEntry", font=("Arial", 12), foreground="black")

from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
amount_var = tk.StringVar()
result_var = tk.StringVar()

ttk.Label(root, text="From Currency (e.g., USD):").grid(column=0, row=0, padx=10, pady=10)
from_currency_entry = ttk.Entry(root, textvariable=from_currency_var)
from_currency_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="To Currency (e.g., INR):").grid(column=0, row=1, padx=10, pady=10)
to_currency_entry = ttk.Entry(root, textvariable=to_currency_var)
to_currency_entry.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(root, text="Amount:").grid(column=0, row=2, padx=10, pady=10)
amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.grid(column=1, row=2, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
convert_button.configure(style="TButton")

ttk.Label(root, textvariable=result_var).grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()

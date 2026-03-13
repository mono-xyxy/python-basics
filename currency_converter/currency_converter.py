import requests

BASE_URL="https://api.exchangerate-api.com/v4/latest/"

from_currency=input("Enter base currency (e.g., USD): ").upper()
to_currency=input("Enter target currency (e.g., INR): ").upper()

amount = float(input("Enter amount: "))

response = requests.get(BASE_URL+from_currency)
data=response.json()

if "rates" in data and to_currency in data["rates"]:
    rate = data["rates"][to_currency]
    converted_amount = amount*rate


    print("\nCurrency Conversion")
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


else:
      print("Invalid currency code.")
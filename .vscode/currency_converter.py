import requests
currencyFrom=input("Enter Currency to convert From : ")

url = 'https://api.exchangerate-api.com/v4/latest/'+currencyFrom

response = requests.get(url)
lines = response.json()

for line in lines:
    country=lines["rates"]

amount=int(input("Enter amount: \n"))
print("Enter the name of currency you want to convert this amount to? "
      "Available options:\n")
[print(item) for item in country.keys()]
currency=input("Please enter one of these values :\n")
print(f"{amount} {currencyFrom} is equal to {amount*float(country[currency])} {currency}")
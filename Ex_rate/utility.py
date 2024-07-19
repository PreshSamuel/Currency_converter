import requests
def currency_listing():
    r = 'https://v6.exchangerate-api.com/v6/7e6c9b35e3ebff2d36128ca0/latest/USD'

    response = requests.get(r)
    value = response.json()["conversion_rates"]
    return value

def convert(base_currency: str, amount: float, target_currency: str):
    r = 'https://v6.exchangerate-api.com/v6/7e6c9b35e3ebff2d36128ca0/latest/USD'

    response = requests.get(r)  
    value = response.json()["conversion_rates"]
    if base_currency == 'USD':
        result = value[target_currency] * amount
        return result
    else:
        result = amount / value[base_currency] 
        return f'{result:.2f} {target_currency}'
    

# print(convert(base_currency='USD', amount=1200, target_currency='NGN'))
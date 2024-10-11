import requests

"""
   {'moneda':
    'casa': 
    'nombre':
    'compra':
    'venta':
    'fechaActualizacion':}
"""

def response_parser(response):
    resnse_json = response.json()
    currency = resnse_json['moneda']
    type = resnse_json['casa']
    sellValue = resnse_json['venta']
    buyValue  = resnse_json['compra']
    print( f"La moneda es: {currency}")
    print( f"El tipo de cambio es: {type}")
    print( f"El valor de venta es: {sellValue}")
    print( f"El valor de compra es: {buyValue}")


if __name__ == "__main__":
    response = requests.get("https://dolarapi.com/v1/dolares/blue")
    response_parser(response)
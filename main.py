import requests
from model.DolarBlue import DolarBlue
from utils.functions import response_parser

def main():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares/blue")
        response.raise_for_status() 
        currency, type_currency, sellValue, buyValue, date = response_parser(response)
        
        dolar_blue = DolarBlue(currency, type_currency, sellValue, buyValue, date)
        dolar_blue.show_values()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()


"""
El siguiente trabajo es hacer que guarde todo en un csv para que lo pueda consultar el historico, de esta forma
date - hour
sellValue
buyValue
averageValue
"""
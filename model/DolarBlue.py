from dataclasses import dataclass
from model.Date import Date

@dataclass
class DolarBlue:
    
    currency: str
    type_currency: str
    sellValue: float
    buyValue: float
    date: Date
    
    def __init__(self, currency, type_currency, sellValue, buyValue, date):
        self.currency = currency
        self.type_currency = type_currency
        self.sellValue = sellValue
        self.buyValue = buyValue
        self.date = date

    def calculate_dolar_blue_average(self):
        return float((self.sellValue + self.buyValue) / 2)

    def show_values(self):
        print("Dolar Blue")
        print(f"Date: {self.date.date} - {self.date.hour}")
        print(f"Sell Value:    {self.sellValue}")
        print(f"Buy Value:     {self.buyValue}")
        print(f"Average Value: {self.calculate_dolar_blue_average()}")
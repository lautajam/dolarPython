from dataclasses import dataclass

@dataclass
class Date:
    
    date: str
    hour: str
    
    def __init__(self, date, hour):
        self.date = date
        self.hour = hour
        
    def show_date(self):
        print(f"Date: {self.date}")
        print(f"Hour: {self.hour}")
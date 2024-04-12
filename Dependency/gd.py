from pymongo import MongoClient
from forex_python.converter import CurrencyRates
from datetime import datetime

# Connection
client = MongoClient("mongodb://localhost:27017")
db = client.get_database("currency_data")
collection = db.currency_rates

c = CurrencyRates()
print(c)

currency_pairs = [("USD", "EUR"), ("USD", "GBP"), ("USD", "CAD")] 

for pair in currency_pairs:
    rate = c.get_rate(pair[0], pair[1])
    today_date = datetime.now().date().isoformat()
    data = {
        "Date": today_date,
        "FromCurrency": pair[0],
        "ToCurrency": pair[1],
        "ExchangeRate": rate
    }
    collection.insert_one(data)

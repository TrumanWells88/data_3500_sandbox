import requests
import json

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=NG9C9EPVYBMQT0C8"

request = requests.get(url)

stock_dictionary = json.loads(request.text)
print(stock_dictionary)

time_key = "Time Series (Daily)"
# key2 = "2026-04-06"
price_key = "4. close"

for date_key in stock_dictionary[time_key].keys():
    print(date_key, stock_dictionary[time_key][date_key][price_key])


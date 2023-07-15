import requests

def get_historical_prices(symbol):
    # Binance API'sına istek gönder
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}USDT&interval=1d&limit=1000"
    response = requests.get(url)
    data = response.json()
    prices = [float(entry[4]) for entry in data]
    all_time_high = max(prices)
    return all_time_high

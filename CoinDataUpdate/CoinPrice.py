import requests

def get_coin_data(symbol):
    # Binance API'sına istek gönder
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}USDT"
    response = requests.get(url)
    data = response.json()
    current_price = float(data["lastPrice"])
    return current_price

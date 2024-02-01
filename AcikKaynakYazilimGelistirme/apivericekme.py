import requests

url = "https://api.coinlore.net/api/tickers/"
response = requests.get(url)
data = response.json()

# Tüm piyasa verilerini döngü içinde kontrol et
for market in data['data']:
    market_symbol = market.get('symbol', 'N/A')
    price_btc = market.get('price_btc', 'N/A')

# Filtrelenmiş verilerin symbol ve price btc değerlerini ekrana yazdır

    print(f"SEMBOL: {market_symbol}")
    print(f"Price btc: {price_btc}")
    print("---------")

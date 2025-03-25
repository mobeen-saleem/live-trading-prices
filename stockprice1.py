import yfinance as yf
import requests

def stock_price(symbol):
    stock = yf.Ticker(symbol) # create stock object for given symbol
    price=stock.history(period="1d")["Close"].iloc[-1] # gets the closing price of the stock
    return round(price,2) # returns the price rounded to 2dp

def crypto_price(symbol, currency="USDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}{currency}" # URL for Binance API
    data = requests.get(url).json() # converts the data from the API to a python dictionary
    return float(data["price"]) # extracts the price and rounds it

def gbp_usd_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    rate = 1 / float(data["rates"]["GBP"])  # Converts the GBP/USD rate to USD/GBP (since the API gives 1 USD = X GBP, we need 1 GBP = X USD)
    return rate

if __name__ == "__main__": # only runs if the script is run directly
    stock_symbol = input("Enter the stock symbol: ").upper()
    crypto_symbol = input("Enter the cryptocurrency symbol: ").upper()

crypto_gbp = (crypto_price(crypto_symbol)) / gbp_usd_rate() # converts the cryptocurrency price to GBP by dividing its USD price by the USD/GBP rate

print(f"{stock_symbol} Price: £{stock_price(stock_symbol)}")
print(f"{crypto_symbol} Price: £{round(crypto_gbp,3)}")
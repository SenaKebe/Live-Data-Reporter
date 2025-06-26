import requests, os, time
from dotenv import load_dotenv

load_dotenv()

def fetch_news():
    try:
        key = os.getenv("NEWS_API_KEY")
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={key}"
        r = requests.get(url)
        data = r.json()
        log_event("Fetched news", "SUCCESS")
        return [a["title"] for a in data["articles"]]
    except Exception as e:
        log_event(f"News error: {str(e)}", "FAILURE")
        return []

def fetch_stock():
    try:
        key = os.getenv("STOCK_API_KEY")
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={key}"
        r = requests.get(url)
        data = r.json()
        time_series = data["Time Series (5min)"]
        latest = sorted(time_series.keys())[0]
        price = time_series[latest]["1. open"]
        log_event("Fetched stock price", "SUCCESS")
        return f"IBM stock price at {latest}: ${price}"
    except Exception as e:
        log_event(f"Stock error: {str(e)}", "FAILURE")
        return "Could not retrieve stock data."

def log_event(message, status):
    with open("logs.txt", "a") as log:
        log.write(f"{time.ctime()} | {status} | {message}\n")

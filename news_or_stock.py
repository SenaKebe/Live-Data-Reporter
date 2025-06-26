import requests, os, time
from dotenv import load_dotenv

load_dotenv()

def fetch_news():
    try:
        key = os.getenv("NEWS_API_KEY")
        if not key:
            raise ValueError("Missing NEWS_API_KEY in .env file")

        url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={key}"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        if data.get("status") != "ok":
            raise ValueError(f"NewsAPI error: {data.get('message', 'Unknown error')}")

        articles = data.get("articles", [])
        headlines = [a["title"] for a in articles]
        log_event("Fetched news", "SUCCESS")
        return headlines

    except Exception as e:
        log_event(f"News error: {str(e)}", "FAILURE")
        return []

def fetch_stock():
    try:
        key = os.getenv("STOCK_API_KEY")
        if not key:
            raise ValueError("Missing STOCK_API_KEY in .env file")

        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={key}"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        if "Time Series (5min)" not in data:
            raise ValueError(data.get("Note") or data.get("Error Message") or "Unexpected response")

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

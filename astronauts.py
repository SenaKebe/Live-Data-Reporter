import requests
import time

def fetch_astronauts():
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n--- Astronauts ---\nTime: {time.ctime()}\n")
            for astro in data["people"]:
                f.write(f"{astro['name']} on {astro['craft']}\n")
        log_event("Fetched astronauts", "SUCCESS")
        return data["people"]
    except Exception as e:
        log_event(f"Error fetching astronauts: {str(e)}", "FAILURE")
        return []

def log_event(message, status):
    with open("logs.txt", "a") as log:
        log.write(f"{time.ctime()} | {status} | {message}\n")

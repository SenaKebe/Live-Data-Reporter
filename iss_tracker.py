import requests
import time

def fetch_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        position = data["iss_position"]
        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n--- ISS Location ---\nTime: {time.ctime()}\n")
            f.write(f"Latitude: {position['latitude']}, Longitude: {position['longitude']}\n")
        log_event("Fetched ISS position", "SUCCESS")
        return position
    except Exception as e:
        log_event(f"Error fetching ISS location: {str(e)}", "FAILURE")
        return {}

def log_event(message, status):
    with open("logs.txt", "a") as log:
        log.write(f"{time.ctime()} | {status} | {message}\n")

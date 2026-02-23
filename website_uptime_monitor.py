import requests
import time
import datetime

def check_website_status(url):
    try:
        response = requests.head(url, timeout=5) # Use HEAD request for efficiency
        if response.status_code == 200:
            print(f"[{datetime.datetime.now()}] {url} is UP (Status: 200 OK)")
        else:
            print(f"[{datetime.datetime.now()}] {url} is DOWN (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.datetime.now()}] {url} is DOWN (Error: {e})")

# --- Main monitoring loop ---
website_url = "https://www.google.com" # Replace with the URL you want to monitor
monitoring_interval = 60 # Check every 60 seconds

while True:
    check_website_status(website_url)
    time.sleep(monitoring_interval)

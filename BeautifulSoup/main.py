import requests
import os

def fetch_and_save(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    dir_path, file_name = os.path.split(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(path, "w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"
fetch_and_save(url, "date/times.html")
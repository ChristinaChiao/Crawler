import requests

url = "https://httpbin.org/headers"


headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.google.com"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.text)
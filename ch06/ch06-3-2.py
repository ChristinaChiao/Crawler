import requests

url = "https://httpbin.org/status/404"

try:
    res = requests.get(url)
    res.raise_for_status( ) 
except requests.exceptions.HTTPError as err:
    print(f"連線出錯了：{err}")

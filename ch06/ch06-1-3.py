from urllib.parse import urlparse, parse_qs

full_url = "https://www.google.com/search?q=python%E7%94%B1%E4%BE%86"
parsed_url = urlparse(full_url)
print("Parsed URL:", parsed_url)
print(f"路徑: {parsed_url.path}")
print(f"查詢: {parsed_url.query}")
print(f"主機: {parsed_url.netloc}")
print(f"協議: {parsed_url.scheme}")
print(f"片段: {parsed_url.fragment}")

query_params = parse_qs(parsed_url.query)
print("Query Parameters:", query_params)
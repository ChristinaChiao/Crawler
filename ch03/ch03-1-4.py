import pandas as pd

products = [
  {"name": "咖啡機", "price": 5000, "rating": 4.8},
  {"name": "磨豆機", "price": 1200, "rating": 4.2},
  {"name": "濾紙", "price": 150, "rating": 4.9},
  {"name": "保溫杯", "price": 800, "rating": 3.5}
]

df = pd.DataFrame(products)
print(df)
print()
print(df[df["rating"] >= 4.5]) #4.5以上的商品
print(df[df["price"] >= 500]) #價格500以上的商品
print(df[(df["rating"] >= 4.5) & (df["price"] <= 2000)]) #4.5以上且價格2000以下的商品
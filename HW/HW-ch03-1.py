#3-1-1
products = [
    {"product": ["iPh one ", "ipad"], "price": ["$30,000", "$20,000"]},
]

for item in products:
   item["product"] = [p.replace(" ", "") for p in item["product"]]
   item["price"] = [p.replace("$", "").replace(",", "") for p in item["price"]]
   print(item["product"])
   print(item["price"][0])
   print(item["price"][1])
#3-1-2
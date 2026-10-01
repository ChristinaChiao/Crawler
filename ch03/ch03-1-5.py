#異常格式處理、或是重複
import pandas as pd
df = pd.DataFrame({
    "user": [" Alice ", "Bob\n", "  Charlie  "], 
    "email": ["ALICE@gmail.com", "bob@Gmail.com", "CHARLIE@outlook.com"]
})

df["user"] = df["user"].str.strip()
df["email"] = df["email"].str.lower()

print(df["user"])
print(df["email"])

print(df)
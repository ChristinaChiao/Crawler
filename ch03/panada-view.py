import tkinter as tk
from tkinter import ttk
import pandas as pd

df = pd.DataFrame({
    "姓名": ["小明", "小華", "小美"],
    "年齡": [20, 25, 22],
    "城市": ["台北", "桃園", "台中"]
})

root = tk.Tk()
root.title("Pandas DataFrame Viewer")
root.geometry("500x300")

# Treeview
tree = ttk.Treeview(
    root,
    columns=list(df.columns),
    show="headings"
)

# 建立欄位
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

# 填入 DataFrame
for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

# 垂直捲軸
scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()

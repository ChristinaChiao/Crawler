import re

text = "我的電話是 0912-345-678，我的 ID 是 worker_007。我的分機是526，員編是ABC12345"

# 範例 1：找出所有單個數字
result_1 = re.findall(r"\d", text)
print(f"範例 1 結果: {result_1}")

# 範例 2：找出連續的四位數字
result_2 = re.findall(r"\d\d\d\d", text)
print(f"範例 2 結果: {result_2}")

# 範例 3：找出所有單個文字字元（含底線）
result_3 = re.findall(r"\w", "ID: user_1")
print(f"範例 3 結果: {result_3}")

# 範例 4：尋找特定模式（ID 是兩個字母加上底線與三位數字）
result_4 = re.findall(r"\w\w_\d\d\d", text)
print(f"範例 4 結果: {result_4}")


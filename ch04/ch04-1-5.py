import re

test_str = "apple, appple, appleee, aple, ae, color, colour"

# 範例 1：找出包含 1 個或多個 p 的單字 (apple 家族)
# p+ 代表 p 出現 1 次以上
result_1 = re.findall(r"ap+le", test_str)
print(f"範例 1 (+): {result_1}")

# 範例 2：找出包含 0 個或多個 p 的單字 (ae 家族)
# p* 代表 p 出現 0 次就行
result_2 = re.findall(r"ap*le", "ale, aple, appple")
print(f"範例 2 (*): {result_2}")

# 範例 3：處理「英式」與「美式」拼法的差異
# u? 代表 u 可能有，也可能沒有
result_3 = re.findall(r"colou?r", "color, colour, colouur")
print(f"範例 3 (?): {result_3}")

# 範例 4：連續數字的快速抓取
# \d+ 代表抓取連續的一串數字，不限長度
phone_text = "門牌 123 號，電話 0912345678"
result_4 = re.findall(r"\d+", phone_text)
print(f"範例 4 (\d+): {result_4}")

# 範例 5：混搭應用 (\w+ 代表連續單字)
result_5 = re.findall(r"\w+", "Hello, Regex_123 World!")
print(f"範例 5 (\w+): {result_5}")
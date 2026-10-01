import tkinter as tk # tkinter 用於建立圖形使用者介面(GUI)
def click():
    try:
        height = float(entry1.get())
        weight = float(entry2.get())
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "過輕：可能有營養不良、骨質疏鬆等風險"
        elif bmi < 24:
            status = "正常：建議維持健康生活習慣"
        elif bmi < 27:
            status = "過重：需注意飲食與運動，避免進一步肥胖"
        else:
            status = "肥胖：BMI ≥ 27"

        result_label.config(text=f"BMI={bmi:.2f} \n {status}")

    except ValueError:
        result_label.config(text="請輸入正確的數字")

root = tk.Tk() # 建立主視窗
root.geometry("500x300") #設定視窗大小
root.title("BMI計算器") # 設定主視窗的標題

label1 = tk.Label(root, text="身高（公尺）", font=("微軟正黑體", 16))
label1.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky="w")  #padx是左右的間距，pady是上下的間距，sticky="w"表示靠左對齊(西邊)

label2 = tk.Label(root, text="體重（公斤）", font=("微軟正黑體", 16))
label2.grid(row=1, column=0, padx=(10,0), pady=(10,0), sticky="w") 

result_label = tk.Label(root, text="Result", width=30, font=("微軟正黑體", 16)) #建立一個空的標籤元件，用於顯示使用者輸入的姓名
result_label.grid(row=3, column=0, columnspan=2, padx=(10,0), pady=(10,0), sticky="w")

entry1 = tk.Entry(root, font=("微軟正黑體", 16))
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root, font=("微軟正黑體", 16))
entry2.grid(row=1, column=1)

button = tk.Button(root, text="計算BMI", width=25, font=("微軟正黑體", 16), command=click) # 建立按鈕元件，點擊後執行登入操作
button.grid(row=2, column=0, columnspan=2) # 將按鈕元件加入主視窗並顯示


root.mainloop() # 啟動主視窗的事件迴圈
import tkinter as tk # tkinter 用於建立圖形使用者介面(GUI)
def click():
    print("發生按下事件")
    result ['text'] = entry1.get() + " " + entry2.get()
root = tk.Tk() # 建立主視窗
root.geometry("500x300") #設定視窗大小
root.title("資料分析") # 設定主視窗的標題

label1 = tk.Label(root, text="First Name")
label1.grid(row=0, column=0) # 建立另一個標籤元件
label1['text'] = "Name"

label2 = tk.Label(root, text="Last Name")
label2.grid(row=1, column=0) 

label3 = tk.Label(root, text="") #建立一個空的標籤元件，用於顯示使用者輸入的姓名
label3.grid(row=3, column=0)

result = tk.Label(root, text="Result", width=30) #建立一個空的標籤元件，用於顯示使用者輸入的姓名
result.grid(row=4, column=0, columnspan=2)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# button = tk.Button(root, text="Close", width=25, command=root.destroy) # 建立按鈕元件，點擊後關閉主視窗
def display(): #制定一個函數，用於顯示使用者輸入的姓名
    # print("Name:", entry1.get())
    # print("Last Name:", entry2.get())
    label3['text'] = "Hello, " + entry1.get() + " " + entry2.get()
button = tk.Button(root, text="Enter", width=25, command=display) # 建立按鈕元件，點擊後執行登入操作
button.grid(row=2, column=0) # 將按鈕元件加入主視窗並顯示

# label = tk.Label(root, text="Hello, Tkinter!") # 建立標籤元件
# label.pack() # 將標籤元件加入主視窗並顯示
# button = tk.Button(root, text="Close", width=25, command=root.destroy) # 建立按鈕元件，點擊後關閉主視窗
# button.pack() # 將按鈕元件pack加入主視窗並顯示

root.mainloop() # 啟動主視窗的事件迴圈
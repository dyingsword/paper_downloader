import tkinter as tk
from tkinter import messagebox
import loader as ld

# 创建窗口
window = tk.Tk()
window.title("论文下载器")
window.geometry("600x400")

# 定义搜索按钮响应事件
def search():
    scientist_name = entry.get()
    pid=ld.get_author_pid( scientist_name)
    result=ld.get_author_publications(pid)
    for item in result:
        print(f"{item}\n")
    

# 设置整个窗口可伸缩
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# 添加控件
label = tk.Label(window, text="请输入科学家名称：")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="搜索", command=search)
button.pack(pady=10)

# 进入主循环
window.mainloop()

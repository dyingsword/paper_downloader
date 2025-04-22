import tkinter as tk
from tkinter import messagebox
import loader as ld
class ui():
    def __init__(self,title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("600x400")                  #根据初始化时提供的标题参数生成窗口
      # 设置整个窗口可伸缩
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)  

    def add_label(self,text:str):       # 添加控件
        self.label = tk.Label(self.window, text=text)
        self.label.pack(pady=10)

    def add_entry(self):  #提供可添加输入框的方法，如要更加拓展，可更改控件添加方法，增加尺寸参数，使得可自由地更改ui界面
        self.entry = tk.Entry(self.window)
        self.entry.pack()
    
    def add_button(self,text):   #可增加按钮控件
        self.button = tk.Button(self.window, text=text, command=self.search)
        self.button.pack(pady=10)   
 
    def add_out(self):            #可增加输出框控件
        self.output_text = tk.Text(self.window, height=15, wrap=tk.WORD)
        self.output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 

    def search(self):
        scientist_name = self.entry.get()
        pid=ld.get_author_pid( scientist_name)
        result=ld.get_author_publications(pid)
        self.output_text.delete("1.0", tk.END)
        for item in result:
           self.output_text.insert(tk.END, item + "\n")

# 定义搜索按钮响应事件方法，为了保证class的泛用性


#生成对象
my_ui=ui("论文列表下载器")
#增添各项控件
my_ui.add_label(text="请输入科学家姓名")
my_ui.add_entry()
my_ui.add_button(text="搜索")
my_ui.add_out()

# 进入主循环
my_ui.window.mainloop()

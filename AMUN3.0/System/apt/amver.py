import tkinter as tk  
  
# 实例化Tk窗口  
version_window = tk.Tk()  
version_window.title("AMUNVER")  
version_window.geometry("320x300")  
  
image_path = "amun_logo.ppm"  
image = tk.PhotoImage(file=image_path)  
  
# 在窗口中添加并显示图片  
label = tk.Label(version_window, image=image)  
label.pack()  
  
# 显示版本信息，并使其左对齐  
version_label = tk.Label(version_window, text="AMUN 3.0 版本 3.0 202407", font=("Arial", 10), anchor=tk.W)  
version_label.pack(fill=tk.X)  # 使用fill=tk.X使标签水平填充整个容器
version_label = tk.Label(version_window, text="(c) Amun保留所有权利", font=("Arial", 10), anchor=tk.W)  
version_label.pack(fill=tk.X)  # 使用fill=tk.X使标签水平填充整个容器
  
# 添加关闭按钮，并设置其在右侧且周围有空白  
close_button = tk.Button(version_window, text="   关闭   ", command=version_window.destroy)  
close_button.pack(side=tk.RIGHT, pady=10, padx=(0, 20))  # padx的(0, 20)表示按钮左侧无空白，右侧空白20像素  
  
# 进入Tk窗口的主循环  
version_window.mainloop()

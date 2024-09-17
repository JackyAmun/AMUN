import tkinter as tk  
from tkinter import filedialog  
from PIL import Image, ImageTk  
  
class ImageViewer:  
    def __init__(self, master):  
        self.master = master  
        master.title("Image Viewer")  
  
        # 创建菜单  
        self.menu_bar = tk.Menu(master)  
        file_menu = tk.Menu(self.menu_bar, tearoff=0)  
        file_menu.add_command(label="Open", command=self.open_image)  
        file_menu.add_command(label="Exit", command=master.quit)  
        self.menu_bar.add_cascade(label="File", menu=file_menu)  
        master.config(menu=self.menu_bar)  
  
        # 创建标签用于显示图像  
        self.image_label = tk.Label(master)  
        self.image_label.pack()  
  
    def open_image(self):  
        # 打开文件对话框选择图像文件  
        file_path = filedialog.askopenfilename()  
        if file_path:  
            # 使用 PIL 打开图像  
            image = Image.open(file_path)  
            # 将 PIL 图像转换为 tkinter 可显示的图像  
            tk_image = ImageTk.PhotoImage(image)  
            # 在标签中显示图像  
            self.image_label.config(image=tk_image)  
            # 保存对图像的引用，防止被垃圾回收  
            self.image_label.image = tk_image  
  
if __name__ == "__main__":  
    root = tk.Tk()  
    viewer = ImageViewer(root)  
    root.mainloop()

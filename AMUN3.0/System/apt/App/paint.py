import tkinter as tk  
from tkinter import Canvas, colorchooser, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageGrab

  
class SimpleDraw:  
    def __init__(self, master):  
        self.master = master  
        self.canvas = Canvas(self.master, width=800, height=600, bg='white')  
        self.canvas.pack()  
  
        self.paint_color = "black"  
        self.eraser_on = False  
        self.brush_size = 3  
        self.shape = None  
        self.draw_data = {}  # 用于存储绘制直线和矩形所需的数据  
  
        self.setup_buttons()  
        self.canvas.bind("<B1-Motion>", self.paint)  
        self.canvas.bind("<ButtonPress-1>", self.start_drawing)  
        self.canvas.bind("<ButtonRelease-1>", self.end_drawing)  
  
    def setup_buttons(self):  
        # Color chooser button  
        self.color_button = tk.Button(self.master, text="选择颜色", command=self.choose_color)  
        self.color_button.pack(side=tk.LEFT)  
  
        # Size chooser button  
        self.size_button = tk.Button(self.master, text="选择画笔大小", command=self.choose_size)  
        self.size_button.pack(side=tk.LEFT)  
  
        # Clear button  
        self.clear_button = tk.Button(self.master, text="清除画板", command=self.clear_pad)  
        self.clear_button.pack(side=tk.LEFT)  
  
        # Eraser button  
        self.eraser_button = tk.Button(self.master, text="橡皮擦", command=self.eraser)  
        self.eraser_button.pack(side=tk.LEFT)  
  
        # Save button  
        self.save_button = tk.Button(self.master, text="保存", command=self.save_file)  
        self.save_button.pack(side=tk.LEFT)  
  
        # Shape buttons (can be extended with more shapes)  
        self.line_button = tk.Button(self.master, text="直线", command=lambda: self.set_shape('line'))  
        self.line_button.pack(side=tk.LEFT)  
        self.rectangle_button = tk.Button(self.master, text="矩形", command=lambda: self.set_shape('rectangle'))  
        self.rectangle_button.pack(side=tk.LEFT)  
  
    def choose_color(self):  
        self.eraser_on = False  # Turn off eraser when choosing a color  
        (rgb, hex) = colorchooser.askcolor(color=self.paint_color, title="选择颜色")  
        if rgb is not None:  # Check if a color was actually chosen  
            self.paint_color = hex  
  
    def choose_size(self):  
        self.size_chooser = simpledialog.askinteger("选择画笔大小", "请输入画笔大小(1-10)：", minvalue=1, maxvalue=10, parent=self.master)  
        if self.size_chooser is not None:  
            self.brush_size = self.size_chooser  
  
    def clear_pad(self):  
        self.canvas.delete("all")  
  
    def eraser(self):  
        self.eraser_on = not self.eraser_on  
        if self.eraser_on:  
            self.paint_color = "white"  
  
    def start_drawing(self, event):  
        self.last_x, self.last_y = event.x, event.y  
        if self.shape in ('line', 'rectangle'):  
            self.draw_data[self.shape] = (self.last_x, self.last_y)  
  
    def end_drawing(self, event):  
        if self.shape:  
            if self.shape == 'line':  
                self.canvas.create_line(self.draw_data[self.shape][0], self.draw_data[self.shape][1],  
                                        event.x, event.y, fill=self.paint_color)  
            elif self.shape == 'rectangle':  
                x1, y1 = min(self.draw_data[self.shape][0], event.x), min(self.draw_data[self.shape][1], event.y)  
                x2, y2 = max(self.draw_data[self.shape][0], event.x), max(self.draw_data[self.shape][1], event.y)  
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.paint_color)  
        self.shape = None  
  
    def paint(self, event):  
        if self.shape:  
            return  # 不在绘制形状时绘制点  
        if self.eraser_on:  
            paint_color = "white"  
        else:  
            paint_color = self.paint_color  
        if event.state & 0x01:  # 检查是否按下了Shift键（可选功能，用于绘制直线）  
            if self.shape == 'line':  
                self.canvas.create_line(self.draw_data[self.shape][0], self.draw_data[self.shape][1],  
                                        event.x, event.y, fill=paint_color, width=self.brush_size)  
        else:  
            self.canvas.create_oval(event.x - self.brush_size, event.y - self.brush_size,  
                                    event.x + self.brush_size, event.y + self.brush_size,  
                                    fill=paint_color, outline=paint_color)   
  
    def start_line(self, event):  
        self.last_x, self.last_y = event.x, event.y  
  
    def end_line(self, event):  
        if self.shape == 'line':  
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.paint_color)  
        elif self.shape == 'rectangle':  
            x1, y1 = min(self.last_x, event.x), min(self.last_y, event.y)  
            x2, y2 = max(self.last_x, event.x), max(self.last_y, event.y)  
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.paint_color)  
        self.shape = None  
  
    def set_shape(self, shape):  
        self.shape = shape  
  
    def save_file(self):  
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])  
        if file_path:  
            try:  
                # 使用Pillow从tkinter Canvas中捕获图像  
                x = self.canvas.winfo_rootx() + self.canvas.winfo_x()  
                y = self.canvas.winfo_rooty() + self.canvas.winfo_y()  
                xy = (x, y, x + self.canvas.winfo_width(), y + self.canvas.winfo_height())  
                image = ImageGrab.grab(bbox=xy)  
  
                # 另一种方法：如果Canvas没有滚动条或复杂内容，可以直接绘制到PIL图像上  
                # image = Image.new("RGB", (self.canvas.winfo_width(), self.canvas.winfo_height()))  
                # draw = ImageDraw.Draw(image)  
                # for item in self.canvas.find_all():  
                #     # 这里需要处理Canvas上的各种item类型，将其绘制到PIL图像上  
                #     pass  
  
                # 保存PIL图像为PNG文件  
                image.save(file_path)  
                messagebox.showinfo("保存成功", "图像已保存为 PNG 文件")  
  
            except Exception as e:  
                messagebox.showerror("保存错误", f"保存图像时出错: {e}")  
    def start(self):  
        pass  # The start method is no longer needed as event bindings are set up in __init__  
  
if __name__ == "__main__":  
    root = tk.Tk()  
    root.title("Amun paint")  
    app = SimpleDraw(root)  
    app.start()  # This line is no longer needed  
    root.mainloop()

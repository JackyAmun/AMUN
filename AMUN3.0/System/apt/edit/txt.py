import tkinter as tk  
from tkinter import filedialog, messagebox, simpledialog  
  
class TextEditor:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Notepad")  
        self.file_path = None  
  
        # 创建文本编辑区域  
        self.text_area = tk.Text(self.root, undo=True)  
        self.text_area.pack(fill=tk.BOTH, expand=True)  
  
        # 创建菜单栏  
        self.main_menu = tk.Menu()  
        self.root.config(menu=self.main_menu)  
  
        self.file_menu = tk.Menu(self.main_menu, tearoff=False)  
        self.main_menu.add_cascade(label="文件", menu=self.file_menu)  
        self.file_menu.add_command(label="打开", command=self.open_file)  
        self.file_menu.add_command(label="保存", command=self.save_file)  
        self.file_menu.add_separator()  
        self.file_menu.add_command(label="退出", command=self.exit_editor)  
  
        # 创建编辑栏  
        self.edit_menu = tk.Menu(self.main_menu, tearoff=False)  
        self.main_menu.add_cascade(label="编辑", menu=self.edit_menu)  
        self.edit_menu.add_command(label="剪切", command=lambda: self.text_area.event_generate("<<Cut>>"))  
        self.edit_menu.add_command(label="复制", command=lambda: self.text_area.event_generate("<<Copy>>"))  
        self.edit_menu.add_command(label="粘贴", command=lambda: self.text_area.event_generate("<<Paste>>"))  
        self.edit_menu.add_separator()  
        self.edit_menu.add_command(label="撤销", command=self.text_area.edit_undo)  
        self.edit_menu.add_command(label="重做", command=self.text_area.edit_redo)  
  
        # 绑定快捷键  
        self.text_area.bind("<Control-x>", lambda e: self.text_area.event_generate("<<Cut>>"))  
        self.text_area.bind("<Control-c>", lambda e: self.text_area.event_generate("<<Copy>>"))  
        self.text_area.bind("<Control-v>", lambda e: self.text_area.event_generate("<<Paste>>"))  
        self.text_area.bind("<Control-z>", self.text_area.edit_undo)  
        self.text_area.bind("<Control-y>", self.text_area.edit_redo)  
  
    def open_file(self):  
        self.file_path = filedialog.askopenfilename(  
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]  
        )  
        if self.file_path:  
            with open(self.file_path, "r") as file:  
                self.text_area.delete(1.0, tk.END)  
                self.text_area.insert(1.0, file.read())  
            self.root.title(f"Notepad - {self.file_path}")  
  
    def save_file(self):  
        if self.file_path:  
            with open(self.file_path, "w") as file:  
                file.write(self.text_area.get(1.0, tk.END))  
        else:  
            self.save_as_file()  
  
    def save_as_file(self):  
        file_path = filedialog.asksaveasfilename(  
            defaultextension="txt",  
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],  
        )  
        if file_path:  
            with open(file_path, "w") as file:  
                file.write(self.text_area.get(1.0, tk.END))  
            self.file_path = file_path  
            self.root.title(f"Notepad - {self.file_path}")  
  
    def exit_editor(self):  
        if messagebox.askokcancel("退出", "确定要退出吗？"):  
            self.root.destroy()  
  
def main():  
    root = tk.Tk()  
    editor = TextEditor(root)  
    root.mainloop()  
  
if __name__ == "__main__":  
    main()

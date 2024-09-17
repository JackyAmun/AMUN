import os  
from tkinter import *  
from tkinter import filedialog, messagebox  
import pygame  
from pygame import mixer  
  
class MusicPlayer:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Music viewer)  
          
        # 设置pygame mixer  
        mixer.init()  
          
        # 创建播放列表  
        self.playlist = []  
        self.current_song_index = 0  
          
        # 创建UI  
        self.create_widgets()  
      
    def create_widgets(self):  
        # 创建菜单  
        menubar = Menu(self.root)  
        filemenu = Menu(menubar, tearoff=0)  
        filemenu.add_command(label="打开", command=self.open_file)  
        filemenu.add_command(label="退出", command=self.root.quit)  
        menubar.add_cascade(label="文件", menu=filemenu)  
          
        # 显示菜单  
        self.root.config(menu=menubar)  
          
        # 创建播放控件  
        self.play_button = Button(self.root, text="播放", command=self.play_song)  
        self.play_button.pack(pady=10)  
          
        self.stop_button = Button(self.root, text="停止", command=self.stop_song)  
        self.stop_button.pack(pady=10)  
          
        # 显示播放器状态  
        self.status_label = Label(self.root, text="")  
        self.status_label.pack(pady=10)  
      
    def open_file(self):  
        # 打开文件对话框选择音乐文件  
        filepath = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])  
          
        if not filepath:  
            return  
          
        # 添加文件到播放列表  
        self.playlist.append(filepath)  
        self.status_label.config(text=f"已添加歌曲: {os.path.basename(filepath)}")  
      
    def play_song(self):  
        # 检查是否有歌曲在播放列表中  
        if not self.playlist:  
            messagebox.showwarning("警告", "播放列表为空，请先添加歌曲。")  
            return  
          
        # 加载并播放当前选中的歌曲  
        mixer.music.load(self.playlist[self.current_song_index])  
        mixer.music.play()  
      
    def stop_song(self):  
        # 停止播放当前歌曲  
        mixer.music.stop()  
          
        # 重置播放状态  
        self.status_label.config(text="")  
  
# 创建主窗口并运行应用  
root = Tk()  
player = MusicPlayer(root)  
root.mainloop()

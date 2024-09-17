import os
import time
import tkinter
import tkinter.filedialog
import threading
import pygame

# 定义一些变量
folder = '' #歌曲文件夹路径
res = [] #存放歌曲路径
ret = [] #存放歌曲名称
num = 0
now_music = ''
one_start = True
# 功能
# 添加文件
def buttonChooseFile():
    global folder
    global res
    global ret
    folder = tkinter.filedialog.askdirectory()
    if folder:
        musics = [folder + '\\' + music
                  for music in os.listdir(folder)\
\
                  if music.endswith(('.mp3','.wav','.ogg'))]
        for i in musics:
            ret.append(i.split('\\')[1:])
            res.append(i.replace('\\','/'))
        var2 = tkinter.StringVar()
        var2.set(ret)
        global lb
        lb = tkinter.Listbox(root,listvariable=var2)

        lb.place(x=50,y=150,width=260,height=300)
        lb.bind("<Double-Button-1>", playActive) #绑定单击事件

    if not folder:
        return
    global playing
    playing = True
    # 根据情况禁用和启用相应的按钮
    button_play['state'] = 'normal'
    button_delete['state'] = 'normal'
    voice_bar['state'] = 'normal'
    pause_resume.set('播放')
# 删除音乐
def buttonDeleteClick():
    music = lb.get('active')[0]
    list_temp = [music]
    ret.remove(list_temp)
    for i in res:
        if i.split("/")[-1] == music:
            res.remove(i)
    lb.delete('active')

# 播放音乐
def play():
    global one_start
    if len(res):
        # 初始化
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                nextMusic = res[num]
                if one_start:
                    # 播放选中的那首歌
                    nextMusic = lb.get('active')
                    temp_list = [nextMusic[0]]
                    current_index = ret.index(temp_list)
                    num = current_index
                    nextMusic = res[current_index]
                pygame.mixer.music.load(nextMusic.encode())
                # 播放一次
                pygame.mixer.music.play(1)

                if len(res) - 1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('/')[-1]
                play_state.set('playing...')
                musicName.set(nextMusic)
                one_start = False
            else:
                time.sleep(0.1)
# 响应双击事件的
def playActive(self):
    global playing,one_start,num
    if not one_start:
        playing = False
        pygame.mixer.init()
        pygame.mixer.music.stop()

        nextMusic = lb.get('active')
        temp_list = [nextMusic[0]]
        current_index = ret.index(temp_list)
        num = current_index

        playing = True
        # 创建线程播放音乐
        t = threading.Thread(target=play)
        t.start()

# 点击播放
def buttonPlayClick():
    button_next['state'] = 'normal'
    button_prev['state'] = 'normal'
    # 选择要播放的音乐文件夹
    if pause_resume.get() == '播放':
        pause_resume.set('暂停')
        play_state.set('playing...')
        global folder
        if not folder:
            folder = tkinter.filedialog.askdirectory()
        if not folder:
            return
        global playing
        playing = True
        # 创建一个线程来播放音乐，当前主线程用来接收用户操作
        t = threading.Thread(target=play)
        t.start()
    elif pause_resume.get() == '暂停':
        # pygame.mixer.init()
        pygame.mixer.music.pause()
        pause_resume.set("继续")
        play_state.set('paused...')
    elif pause_resume.get() == '继续':
        # pygame.mixer.init()
        pygame.mixer.music.unpause()
        pause_resume.set('暂停')
        play_state.set('playing...')
# 上一首
def buttonPrevClick():
    global playing
    playing = False
    pygame.mixer.init()
    pygame.mixer.music.stop()
    global num
    if num == 0:
        num = len(res) - 2
    elif num == len(res) - 1:
        num -= 2
    else:
        num -= 2
    lb.activate(num)
    lb.see(num)
    playing = True
    # 创建线程播放音乐
    t = threading.Thread(target=play)
    t.start()
# 下一首
def buttonNextClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    global num
    if len(res) == num:
        num = 0
    playing = True
    lb.activate(num)
    lb.see(num)

    # 创建线程播放音乐
    t = threading.Thread(target=play)
    t.start()
# 关闭窗口
def closeWindow():
    global playing
    playing = False
    time.sleep(0.3)
    try:
        # 停止播放，如果已经停止
        # 再次停止时会抛出异常，所以需要异常捕获
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy() # 整个界面退出
# 音量控制，默认是一半的音量值
def control_voice(value=0.5):
    try:
        pygame.mixer.music.set_volume(float(value))
    except:
        pass

# 界面
root = tkinter.Tk()
root.title('Music player')
root.geometry('450x350')
root.resizable(False,False)


# 窗口关闭
root.protocol("WM_DELETE_WINDOW",closeWindow)
# 添加文件按钮
button_choose = tkinter.Button(root,text='添加',command=buttonChooseFile)
button_choose.place(x=50,y=10,width=50,height=20)
# 删除歌曲按钮
button_delete = tkinter.Button(root,text='删除',command=buttonDeleteClick)
button_delete.place(x=120,y=10,width=50,height=20)
button_delete['state'] = 'disabled'
# 可变字符串组件
pause_resume = tkinter.StringVar(root,value='播放')
# 播放按钮
button_play = tkinter.Button(root,textvariable=pause_resume,command=buttonPlayClick)
button_play.place(x=260,y=10,width=50,height=20)
button_play['state'] = 'disabled'
# 上一首
button_prev = tkinter.Button(root,text='上一首',command=buttonPrevClick)
button_prev.place(x=190,y=10,width=50,height=20)
button_prev['state'] = 'disabled'
# 下一首
button_next = tkinter.Button(root,text='下一首',command=buttonNextClick)
button_next.place(x=330,y=10,width=50,height=20)
button_next['state'] = 'disabled'
# 播放器状态
play_state = tkinter.StringVar(root,value='暂时没有播放音乐呢...')
stateLabel = tkinter.Label(root,textvariable=play_state,fg='green')
stateLabel.place(x=10,y=30,width=260,height=20)
# 当前播放的音乐
musicName = tkinter.StringVar(root,value='')
labelName = tkinter.Label(root,textvariable=musicName,font=("微软雅黑", 12),fg='#008c8c')
labelName.place(x=10,y=500,width=400,height=30)

# 音量条
voice_bar = tkinter.Scale(root,label='音量',from_=0,to=1,orient=tkinter.HORIZONTAL,
                  length=240,showvalue=0.5,tickinterval=0.5,resolution=0.1,command=control_voice)
voice_bar.set(0.5)
voice_bar.place(x=50,y=50,width=200)
voice_bar['state'] = 'disabled'

root.mainloop()

import sys   
import time
import subprocess  

print("Preloaded")
print("loading...")
X = 10000
for i in range(X):
    for j in range(X):
        k = j * i
    print(f'{i+1} / {X}', end='\r')
print('\nComplete！')

def print_big_text(text):  
    # 定义字符画所用的字符集  
    charset = '@%#*+=-:. '  
      
    # 定义Amun的字符画样式  
    # 这里我们为每个字符定义一个二维列表，每个列表的元素代表字符的一行  
    font = {  
        'A': [  
            '  ###  ',  
            ' ## ## ',  
            '#######',  
            '##   ##',  
            '##   ##'  
        ],  
        'M': [  
            '##   ##',  
            '##   ##',  
            '### ###',  
            '## # ##',  
            '##   ##'  
        ],  
        'U': [  
            '##   ##',  
            '##   ##',  
            '##   ##',  
            '##   ##',  
            '#######'  
        ],  
        'N': [  
            '###  ##',  
            '#### ##',  
            '#######',  
            '## ####',  
            '##  ###'  
        ],  
        # 空格字符不需要定义，因为它只是空格  
    }  
      
    # 设置字符画的宽度（每个字符所占的列数）和高度（行数）  
    width = max(len(char[0]) for char in font.values()) + 2  # 加2是为了字符之间的间隔  
    height = len(font['A'])  
      
    # 初始化输出字符画  
    output = [''] * height  
      
    # 遍历输入文本中的每个字符  
    for i, char in enumerate(text.upper()):  
        if char in font:  
            # 获取字符的字符画表示  
            char_art = font[char]  
              
            # 将字符画添加到输出中  
            for j, line in enumerate(char_art):  
                output[j] += line.rjust(width)  # 使用rjust来确保字符对齐  
        else:  
            # 如果字符没有定义，则添加空白  
            for j in range(height):  
                output[j] += ' ' * width  
      
    # 打印字符画  
    for line in output:  
        print(line)  
  
# 使用示例  
print_big_text('Amun')
  
def select_option(options):  
    selected_option_number = None  
    while selected_option_number is None:  
        show_options(options)  
        try:  
            choice = int(input("\nPlease select an option number: "))  
            if 1 <= choice <= len(options):  
                selected_option_number = choice  
            else:  
                print("Invalid option, please re-enter.")  
        except ValueError:  
            print("Please enter a valid number.")  
    return selected_option_number - 1  # 减1是因为选项列表是从1开始的，而索引是从0开始的  
  
def show_options(options):  
    for idx, option in enumerate(options, 1):  
        print(f"{idx}. {option}")  
  
def handle_option_1():  
    X = 15000
    for i in range(X):
   	    for j in range(X):
                k = j * i
   	    print('starting Amun...',
          	f'|{"█"*((i+1)*50//X):50}|', 
          	f'{(i+1)*100//X}%', 
          	end='\r')
    print('\nComplete！')
    print("Now,you can use the Amun System.")
    subprocess.run(["python", "Amun System1.0.py"])

	  
def handle_option_2():  
    print("1: Restart")  
    print("2: Exit and format")  
    # 注意：这里的“format”可能意味着其他操作，但在此示例中未实现  
    while True:  
        try:  
            choice = int(input("\nPlease select an option number: "))  
            if choice == 1:  
                def restart_program():  
                    python = sys.executable  
                    subprocess.Popen([python] + sys.argv)  
                    sys.exit()  
      
                if __name__ == "__main__":
                    restart_program()
            elif choice == 2:  
                sys.exit("Exiting program...")  
            else:  
                print("Invalid option, please re-enter.")  
        except ValueError:  
            print("Please enter a valid number.")  
  
def main():  
    options = ["starting Amun System", "other", "exit"]  
    while True:  
        selected_option_index = select_option(options)  
        if selected_option_index == len(options) - 1:  # 假设最后一个选项是退出  
            print("\nTurn offing")  
            sys.exit()  
        elif selected_option_index == 0:  # 选项1  
            handle_option_1()  
        elif selected_option_index == 1:  # 选项2  
            handle_option_2()  
  
if __name__ == "__main__":  
    main()

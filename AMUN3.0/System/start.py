import sys   
import time
import subprocess  
from pathlib import Path

print("Preloaded")
print("loading...")
X = 1000
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

def input_activation_key_parts():  
    # 检查 temp 文件夹是否存在，如果不存在则创建  
    temp_folder = Path("./temp")  
    temp_folder.mkdir(exist_ok=True)  
      
    key_file_path = temp_folder / "key.txt"  
      
    # 如果 key.txt 文件存在，则读取其内容作为激活密钥  
    if key_file_path.exists():  
        with open(key_file_path, "r") as file:  
            activation_key = file.read().strip()  
        print(f"Found existing activation key: {activation_key}")  
        return activation_key  
      
    parts = ["", "", "", ""]  
    print("Enter the activation key to activate the Amun.")  
    print("The activation key format is: keyx-xxxx-xxxx-xxxx (x=your key)")  
    for i in range(4):  
        part = input(f"Please enter the {i + 1} section of the key: ")  
        parts[i] = part  
    key = "-".join(parts)  
      
    # 将激活密钥保存到 key.txt 文件中  
    with open(key_file_path, "w") as file:  
        file.write(key)  
   
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
    X = 12000  
    for i in range(X):  
        for j in range(X):  
            k = j * i      
        print('starting Amun...',  
              f'|{"█"*((i+1)*50//X):50}|',   
              f'{(i+1)*100//X}%',   
              end='\r')
    print('\nComplete！')
    print("Amun3.0@Amun system")
    print("Now,you can use the Amun System 3.0.")
    subprocess.run(["python", "CMD.py"]) 
  
def restart_program():    
    python = sys.executable    
    subprocess.Popen([python] + sys.argv)    
    sys.exit()  
	  
def handle_option_2():  
    print("1: Restart")  
    print("2: Exit and format")    
    while True:  
        try:  
            choice = int(input("\nPlease select an option number: "))  
            if choice == 1:  
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
        if selected_option_index == len(options) - 1:  
            print("\nTurn offing")  
            sys.exit()  
        elif selected_option_index == 0:  # 选项1  
            handle_option_1()  
        elif selected_option_index == 1:  # 选项2  
            handle_option_2()  
  
if __name__ == "__main__":    
    activation_key = input_activation_key_parts()  
    print(f"\nYour full activation key is: {activation_key}")  
    if activation_key == "keyx-aefg-asht-aqws" or activation_key == "key0-1345-5470-7054":
        print("The activation was successful")
        main()
    elif activation_key == "key0-1234-5678-abcd" or activation_key == "keyx-bnmv-bghn-bvcx":
        print("The activation was successful")
        main()  
    else:  
        print("The activation key is invalid!")  
        input_activation_key_parts()# Or re-prompt for the key if desired


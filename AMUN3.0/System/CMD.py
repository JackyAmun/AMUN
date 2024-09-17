import os  
import shutil  
import subprocess
import datetime
import apt.download as IA

def list_files(path='.'):  
    """列出指定路径下的文件和文件夹"""  
    try:  
        print("Directory contents:")  
        for item in os.listdir(path):  
            print(item)  
    except FileNotFoundError:  
        print("Path does not exist.")  
  
def change_directory(path):  
    """更改当前工作目录"""  
    global current_directory  
    try:  
        if os.path.exists(path):  
            os.chdir(path)  
            current_directory = os.getcwd()  
            print(f"Changed directory to {current_directory}")  
        else:  
            print("Path does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")   
  
def remove_directory(directory_name):  
    """删除指定文件夹"""  
    global current_directory  
    directory_path = os.path.join(current_directory, directory_name)  
    try:  
        if os.path.isdir(directory_path):  
            shutil.rmtree(directory_path)  
            print(f"Directory {directory_name} deleted.")  
        else:  
            print("Directory does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}") 
  
def create_directory(directory_name):  
    """创建一个新目录"""  
    global current_directory  
    dir_path = os.path.join(current_directory, directory_name)  
    try:  
        if not os.path.exists(dir_path):  
            os.makedirs(dir_path)  
            print(f"Directory {directory_name} created.")  
        else:  
            print("Directory already exists.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
def copy_file(source, destination):  
    """复制文件"""  
    global current_directory  
    src_path = os.path.join(current_directory, source)  
    dest_path = os.path.join(current_directory, destination)  
    try:  
        if os.path.isfile(src_path):  
            shutil.copy(src_path, dest_path)  
            print(f"File {source} copied to {destination}.")  
        else:  
            print("Source file does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
def move_file(source, destination):  
    """移动文件"""  
    global current_directory  
    src_path = os.path.join(current_directory, source)  
    dest_path = os.path.join(current_directory, destination)  
    try:  
        if os.path.isfile(src_path):  
            shutil.move(src_path, dest_path)  
            print(f"File {source} moved to {destination}.")  
        else:  
            print("Source file does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")

def tree_directory(path='.', prefix=''):  
    """列出指定路径下的文件和文件夹结构tree命令"""  
    try:  
        files_and_dirs = [(os.path.join(path, item), os.path.isdir(os.path.join(path, item))) for item in os.listdir(path)]  
        for item, is_dir in sorted(files_and_dirs, key=lambda x: x[1], reverse=True):  
            if is_dir:  
                print(f"{prefix}|-- {os.path.basename(item)}/")  
                tree_directory(item, prefix + '    ')   
            else:  
                print(f"{prefix}|-- {os.path.basename(item)}")  
    except FileNotFoundError:  
        print("Path does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")
  
def quit_program():  
    """退出程序"""  
    print("Exiting program.")  
    exit()  
  
def print_current_directory():  
    """打印当前工作目录"""  
    global current_directory  
    print(current_directory)

def clear_screen():  
    """清屏"""  
    os.system('cls' if os.name == 'nt' else 'clear')  
  
def echo(text):  
    """显示文本"""  
    print(text)  
  
def type_file(filename):  
    """显示文件内容"""  
    global current_directory  
    file_path = os.path.join(current_directory, filename)  
    try:  
        with open(file_path, 'r') as file:  
            print(file.read())  
    except FileNotFoundError:  
        print("File does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
def delete_file(filename):  
    """删除文件"""  
    global current_directory  
    file_path = os.path.join(current_directory, filename)  
    try:  
        if os.path.isfile(file_path):  
            os.remove(file_path)  
            print(f"File {filename} deleted.")  
        else:  
            print("File does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
def rename_file(old_name, new_name):  
    """重命名文件"""  
    global current_directory  
    old_path = os.path.join(current_directory, old_name)  
    new_path = os.path.join(current_directory, new_name)  
    try:  
        if os.path.isfile(old_path):  
            os.rename(old_path, new_path)  
            print(f"File {old_name} renamed to {new_name}.")  
        else:  
            print("File does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
def create_file(filename):  
    """创建新文件"""  
    global current_directory  
    file_path = os.path.join(current_directory, filename)  
    try:  
        with open(file_path, 'w') as file:  
            print(f"File {filename} created.")  
    except Exception as e:  
        print(f"An error occurred: {e}")

def start_app(filename):
    """启动应用"""
    if args[2] =='/s':
        subprocess.run(['python', syspath + '\\apt\\App\\' + filename + '.py'])
    elif args[2] =='/a':
        subprocess.run(['python',filename])
    elif args[2] == '/exe':
        os.system(filename)
    elif args[2] == '/o':
        os.system(filename)
    else:
        print("Usage: start <app name> </s>/</a>/</exe>/</o>")

def find_in_computer(root_dir,search_term):
    """查找文件在电脑中"""
    try:     
        search_type = input("Search for [F]ile, [D]irectory, or [B]oth? ").lower()  
        found = False    
        for root, dirs, files in os.walk(root_dir):    
            if search_type in ['f', 'b']:  
                for file in files:  
                    if search_term in file:  
                        print(f"File found: {os.path.join(root, file)}")  
                        found = True    
            if search_type in ['d', 'b']:  
                for dir_name in dirs:  
                    if search_term in dir_name:  
                        print(f"Directory found: {os.path.join(root, dir_name)}")  
                        found = True
        if not found:  
            print(f"No files or directories matching '{search_term}' found in {root_dir} or its subdirectories.")  
  
    except Exception as e:  
        print(f"An error occurred during the search: {e}")
def ls_apt_l(app_folder_path):
    try:  
        contents = os.listdir(app_folder_path)  
      
        # 打印所有文件，排除文件夹  
        for item in contents:  
            item_path = os.path.join(app_folder_path, item)  
            if os.path.isfile(item_path):  
                print(item)  
    except FileNotFoundError:  
        print(f"The folder '{app_folder_path}' does not exist in the current directory.")

print('(c) Amun保留所有权利。[Amun3.0 202407]')  
# 设置当前目录为系统目录
syspath = os.getcwd()
# 初始化当前目录为脚本所在目录  
current_directory = os.getcwd()  
  
# CLI主循环  
while True:  
    command = input(os.getcwd() + "> ")  
    args = command.split()  
    if len(args) == 0:  
        continue  
    elif args[0].lower() == 'ls':  
        if len(args) == 2:  
            list_files(args[1])  
        else:  
            list_files(current_directory)  
    elif args[0].lower() == 'cd':  
        if len(args) == 2:  
            path = args[1]  
            if path == '..':  
                path = os.path.dirname(current_directory)  
            change_directory(path)  
        else:  
            print("Usage: cd <path>")  
    elif args[0].lower() == 'rm':  
        if len(args) == 2:  
            remove_directory(args[1])  
        else:  
            print("Usage: rm <directory>")  
    elif args[0].lower() == 'mkdir':  
        if len(args) == 2:  
            create_directory(args[1])  
        else:  
            print("Usage: mkdir <directory_name>")  
    elif args[0].lower() == 'cp':  
        if len(args) == 3:  
            copy_file(args[1], args[2])  
        else:  
            print("Usage: cp <source> <destination>")  
    elif args[0].lower() == 'mv':  
        if len(args) == 3:  
            move_file(args[1], args[2])  
        else:  
            print("Usage: mv <source> <destination>")
    elif args[0].lower() == 'cls':  
        clear_screen()  
    elif args[0].lower() == 'echo':  
        if len(args) > 1:
            if args[1].lower() == '%time%':
                print(datetime.datetime.now())
            else:
                echo(' '.join(args[1:]))  
        else:  
            print("Usage: echo <text>")  
    elif args[0].lower() == 'type':  
        if len(args) == 2:  
            type_file(args[1])  
        else:  
            print("Usage: type <filename>")  
    elif args[0].lower() == 'del':  
        if len(args) == 2:  
            delete_file(args[1])  
        else:  
            print("Usage: del <filename>")  
    elif args[0].lower() == 'ren':  
        if len(args) == 3:  
            rename_file(args[1], args[2])  
        else:  
            print("Usage: ren <old_name> <new_name>")  
    elif args[0].lower() == 'nf':  
        if len(args) == 2:  
            create_file(args[1])  
        else:  
            print("Usage: nf <filename>")
    elif args[0].lower() == 'start':
        if len(args) == 3: 
            start_app(args[1])
        else:  
            print("Usage: start <app name> </s>/</a>/</exe>/</o>")
    elif args[0].lower() == 'tree':  
        if len(args) == 2:  
            tree_directory(args[1])  
        else:  
            tree_directory(current_directory)
    elif args[0].lower() == 'find':  
        if len(args) == 3:  
            find_in_computer(args[1], args[2])  
        else:  
            print("Usage: find <path> <search_term>")
    elif args[0].lower() == 'net':
        if len(args) == 2:
            if args[1] == 'sendm':
                subprocess.run(['python',syspath + '\\internet\\email\\send.py'])
            elif args[1] == 'showm':
                subprocess.run(['python',syspath + '\\internet\\email\\show_email.py'])
            elif args[1] == 'ipconfig':
                subprocess.run(['python',syspath + '\\internet\\config\\ipconfig.py'])
            elif args[1] == 'wifils':
                subprocess.run(['python',syspath + '\\internet\\config\\wifi_list.py'])
            else :
                print('Usage: net <sendm> <showm> <ipconfig> <wifils>')
        else :
            print('Usage: net <sendm> <showm> <ipconfig> <wifils>')
    elif args[0].lower() == 'apt':
        if len(args) == 2 or len(args) == 3:
            if args[1] == 'lsl':
                ls_apt_l(syspath + '\\apt\\App')
            elif args[1] == 'ls':
                subprocess.run(['python',syspath + '\\apt\\ls_apt_o.py'])
            elif args[1] == 'install':
                IA.download_apps(args[2])
            elif args[1] == 'uninstall':
                delete_file('apt\\App\\' + args[2])
            else:
                print('Usage: apt <code>')
                print('code: \n lsl \n ls \n install <apt_name> \n uninstall <apt_name> \n')
        else:
            print('Usage: apt <code>')
            print('code: \n lsl \n ls \n install <apt_name> \n uninstall <apt_name> \n')
    elif args[0].lower() == 'edit':  
        subprocess.run(['python',syspath + '\\apt\\edit\\txt.py'])
    elif args[0].lower() == 'pwd':  
        print_current_directory()
    elif args[0].lower() == 'amver':
        subprocess.run(['python',syspath + '\\apt\\amver.py'])
    elif args[0].lower() == 'ver':
        print('(c) Amun保留所有权利。[Amun3.0 202407]')
    elif args[0].lower() == 'exit':  
        quit_program()  
    else:  
        print("Unknown command. Type 'exit' to quit.")

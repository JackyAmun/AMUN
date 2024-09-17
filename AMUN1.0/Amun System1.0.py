# Amun Systen1.0.py  
  
import os  
import sys  
import time
import shutil
import tkinter as tk  
from tkinter import filedialog, Text, messagebox
import subprocess 
  
def main():  
    while True:  
        choice = input("Enter command (or 'HELP' for available commands): ")  
        if choice.upper() == "HELP":  
            print("\n*** Command Line Interface ***")  
            print("1. List files:   list")    
            print("2. New file:   newfile")  
            print("3. New folder:   newfolder")  
            print("4. Modify file:   modifyfile")  
            print("5. Delete file:   deletefile")  
            print("6. Delete folder:   deletefolder")
            print("7. Move file:   movefile")
            print("8. Other panel   other")
            print("9. Exit:   exit")  
            print("\nEnter the corresponding command to proceed.")  
        elif choice == "list":
            directory = input("Enter yuo want to list file: ")
            list_files(directory)
        elif choice == "display":
            display_file()
        elif choice == "newfile":  
            new_file()  
        elif choice == "newfolder":  
            new_folder()  
        elif choice == "modifyfile":  
            modify_file()  
        elif choice == "deletefile":  
            delete_file()  
        elif choice == "deletefolder":  
            delete_folder()
        elif choice == "movefile":  
            move_file()
        elif choice == "other":  
            subprocess.run(["python", "other.py"])
        elif choice == "exit":  
            sys.exit()  
        else:  
            print("Invalid choice. Please try again.")   

def list_files(directory):  
    print("Files in directory:", directory)  
    files = os.listdir(directory)  
    for file in files:  
        print(file)  
    time.sleep(2)  # Pause for 2 seconds
    
def new_file():  
    filename = input("Enter filename with path : ")  
    directory, file_only = os.path.split(filename)  
      
    if not directory:  # 如果用户没有提供目录  
        directory = input("Enter the directory path where the file should be created: ")  
        filename = os.path.join(directory, file_only)  
      
    try:  
        with open(filename, 'w') as file:  
            file.write("")   
        print("File created successfully.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
      
    time.sleep(2)  
  
def new_folder():  
    foldername = input("Enter foldername with path: ")  
      
    try:  
        os.makedirs(foldername, exist_ok=True)  # Create a new folder, don't raise an error if it already exists  
        print("Folder created successfully.")  
    except OSError as e:  
        print(f"An error occurred while creating the folder: {e}")  
      
    time.sleep(2)  # Pause for a few seconds before returning to the main menu
    
def delete_file():  
    filename = input("Enter filename with path to delete: ")  
    try:  
        os.remove(filename)  # 删除文件  
        print("File deleted successfully.")  
    except OSError as e:  
        print("Error: ", e.strerror)  # 更具体的错误信息   
      
    time.sleep(2)  # 暂停几秒钟后再返回主菜单    
  
def delete_folder():  
    foldername = input("Enter the folder path to delete: ")  
    try:  
        shutil.rmtree(foldername)  # Deletes a folder and all its contents  
        print("Folder deleted successfully.")  
    except OSError as e:  
        print("Error:", e.strerror)  # More specific error message  
      
    time.sleep(2)  # Pauses for a few seconds before returning to the main menu   

def move_file():    
    source_file = input("Please enter the file path you want to move:")  
    target_dir = input("Please enter the path to the destination directory:")  
     
    if not os.path.isfile(source_file):  
        print("The source file does not exist, please check the path and file name.")  
        return  
      
    # 检查目标目录是否存在，如果不存在则创建  
    if not os.path.exists(target_dir):  
        os.makedirs(target_dir)  
      
    # 获取文件名，以便在目标目录中使用  
    filename = os.path.basename(source_file)  
    target_file = os.path.join(target_dir, filename)  
      
    # 移动文件  
    try:  
        shutil.move(source_file, target_file)  
        print(f"The file was successfully move from {source_file} to {target_file}")  
    except Exception as e:  
        print(f"Error moving file: {e}")
        
def modify_file():  
    # 从控制台读取文件路径  
    file_path = input("Please enter the file path: ")  
  
    def save_and_exit():  
        new_content = text_editor.get('1.0', tk.END)  
        try:  
            with open(file_path, 'w') as file:  
                file.write(new_content)  
            print("modified successfully.")  
            root.destroy()  
        except Exception as e:  
            messagebox.showerror("error", f"Error saving file: {e}")
            
    try:  
        # 读取文件内容  
        with open(file_path, 'r') as file:  
            content = file.read()  
    except FileNotFoundError:  
        print(f"file '{file_path}' not found.")  
        main()  
  
    # 创建tkinter窗口  
    root = tk.Tk()  
    root.title("Modify File")    
    root.wm_attributes("-topmost", True)  
  
    # 创建Text控件用于编辑文件内容  
    text_editor = Text(root)  
    text_editor.pack(fill='both', expand=True)  
    text_editor.insert('1.0', content)  # 将文件内容插入到Text控件中  
  
    # 创建保存并退出按钮  
    save_button = tk.Button(root, text="save and exit", command=save_and_exit)  
    save_button.pack()  
  
    # 启动tkinter事件循环  
    root.mainloop()
    
main()
          
if __name__ == "__main__":  
    main()

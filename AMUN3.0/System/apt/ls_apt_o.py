import requests  
import os  
  
def download_file_output_content_and_delete(url, local_file_path):  
    try:  
        # 发送GET请求下载文件  
        response = requests.get(url, stream=True)  
        # 确保请求成功  
        response.raise_for_status()  
          
        # 将文件内容写入本地  
        with open(local_file_path, 'wb') as file:  
            for chunk in response.iter_content(chunk_size=8192):  
                if chunk:  
                    file.write(chunk)  
          
        # 输出文件内容  
        with open('list.txt', 'r', encoding='utf-8') as file:  
            content = file.read()  
            print(content)
          
        # 删除本地文件  
        os.remove(local_file_path)  
        print(f"{local_file_path} ")  
    except requests.RequestException as e:  
        print(f"Error: {e}")  
    except FileNotFoundError:  
        print(f"File {local_file_path} not found")  
    except Exception as e:  
        print(f"发生错误: {e}")  
  
# 远程文件的URL  
url = 'http://8.134.210.60/Amun/list.txt'  
# 本地存储文件的路径  
local_file_path = 'list.txt'  
  
# 执行函数  
download_file_output_content_and_delete(url, local_file_path)

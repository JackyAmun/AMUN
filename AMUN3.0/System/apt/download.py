import requests  
import os 

def download_apps(app_name):
    try:
        # 发送GET请求下载文件  
        response = requests.get('http://8.134.210.60/Amun/apt/' + app_name, stream=True)
        # 确保请求成功  
        response.raise_for_status()

        # 将文件内容写入本地  
        with open("apt\\App\\" + app_name, 'wb') as file:  
            for chunk in response.iter_content(chunk_size=8192):  
                if chunk:  
                    file.write(chunk)
        print('Download complete!')
    except requests.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:  
        print(f"发生错误: {e}")
 

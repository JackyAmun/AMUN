import pywifi  
from pywifi import const  
  
def scan_wifi():  
    # 初始化wifi  
    wifi = pywifi.PyWiFi()  
    # 检查是否有无线网卡  
    if len(wifi.interfaces()) == 0:  
        print("没有找到无线网卡")  
        return  
      
    # 使用第一个无线网卡  
    interface = wifi.interfaces()[0]  
    # 断开所有连接（如果需要）  
    interface.disconnect()  
      
    # 设置扫描模式  
    interface.scan()  
      
    # 获取扫描结果  
    bss = interface.scan_results()  
      
    # 列举扫描到的WiFi网络  
    for b in bss:  
        print(f"SSID: {b.ssid}, Signal: {b.signal}")  
  
scan_wifi()

import psutil  
import socket  
  
def get_network_info():  
    net_if_addrs = psutil.net_if_addrs()  
    for interface, addrs in net_if_addrs.items():  
        print(f"Interface: {interface}")  
        for addr in addrs:  
            print(f"  Address: {addr.address}")  
            print(f"  Netmask: {addr.netmask}")  
            print(f"  Broadcast: {addr.broadcast}")  
            print(f"  PTP: {addr.ptp}")  
            if addr.family == socket.AF_INET:  
                print("  IPv4")  
            elif addr.family == socket.AF_INET6:  
                print("  IPv6")  
            print()  
  
get_network_info()

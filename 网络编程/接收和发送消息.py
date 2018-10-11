from socket import *
from threading import Thread
#接收的方法
udp = socket(AF_INET,SOCK_DGRAM)
udp.bind(('',8899))
def rec():
    while True:
        print('开始接收数据',end="")
        content = udp.recvfrom(1024)
        print(content[0].decode('gb2312'))
#发送的方法
def send(ip_temp,point_temp):
    while True:
        infos = input('要发送什么')
        udp.sendto(infos.encode('gb2312'),(ip_temp,point_temp))
#主方法
def main():
    ip = input('目的ip')
    point= input('目的端口')
    se = Thread(target=rec)
    re = Thread(target=send,args=(ip,int(point)))
    se.start()
    re.start()
if __name__=="__main__":
    main()

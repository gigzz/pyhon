#-*-coding:utf-8-*-

from socket import *


import struct
#发送tftp消息
udp= socket(AF_INET,SOCK_DGRAM)
send = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)
print(send)
udp.sendto(send,("192.168.1.11",69))

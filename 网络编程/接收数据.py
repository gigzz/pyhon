from socket import *

udppoint = socket(AF_INET,SOCK_DGRAM)
point = ('',8899)
udppoint.bind(point)
while True:
    content = udppoint.recvfrom(1024)
    print(content[0].decode('gb2312'))
#encode用来编码
#decode用来解码

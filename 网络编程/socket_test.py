
import socket 

udpss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpss.sendto(b"hhhhh",("192.168.50.1",8080))

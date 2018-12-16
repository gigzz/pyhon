# 创建socket
from socket import *
import re
from multiprocessing import Pool

HTML_DIR = './Html/'

def request(new_socket_temp):
    # 接收数据
    content = new_socket_temp.recv(1024)
    # 处理数据
    req = content.decode('utf-8')

    res = re.match(r"\w+?\s*/(.+?) +", req)
    my_url = res.group(1)
    # 返回数据
    strs = 'HTTP/1.1 200 OK\r\n\r\n'
    try:
        if len(my_url) > 1:
            print(HTML_DIR+my_url)
            files = open(HTML_DIR+my_url, 'rb')
            strs += files.read(1024).decode()
            files.close()
            print(strs)
        else:
            strs += 'hello world'
        new_socket_temp.send(strs.encode('utf-8'))
    except:
        strs = 'HTTP/1.1 404 NO Not Found\r\n\r\n'
        new_socket_temp.send(strs.encode('utf-8'))


if __name__ == "__main__":

    Socket = socket(AF_INET, SOCK_STREAM)
    Socket.bind(('', 8989))
    Socket.listen()

    while True:
        newSocket, add = Socket.accept()
        pool = Pool(5)
        pool.apply(func=request, args=(newSocket,))
        newSocket.close()

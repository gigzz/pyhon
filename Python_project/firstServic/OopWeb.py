from socket import *
import re
from multiprocessing import Pool


class HttpService(object):
    HTML_DIR = './Html/'

    # 初始化
    def __init__(self):
        self.Socket = socket(AF_INET, SOCK_STREAM)

    # 设置端口
    def my_bind(self, port):
        self.Socket.bind(('', int(port)))

    # 开启服务
    def start_service(self):
        self.Socket.listen()
        while True:
            newSocket, add = self.Socket.accept()
            pool = Pool(5)
            pool.apply(func=self.request, args=(newSocket,))
            newSocket.close()

    def request(self, new_socket_temp):
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
                print(self.HTML_DIR+my_url)
                files = open(self.HTML_DIR+my_url, 'rb')
                strs += files.read(1024)
                files.close()
                print(strs)
            else:
                strs += 'hello world'
            new_socket_temp.send(strs.encode('utf-8'))
        except:
            strs = 'HTTP/1.1 404 NO Not Found\r\n\r\n'
            new_socket_temp.send(strs.encode('utf-8'))


if __name__ == "__main__":
    my_http = HttpService()
    my_http.my_bind(8989)
    my_http.start_service()

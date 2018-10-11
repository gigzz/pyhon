from multiprocessing import Pool 
from socket import *
def deals(socket_temp):
   # try:
        while True:
            content = socket_temp.recv(1024)
            strs = content.decode('gb2312')
            print(strs)
            if len(strs)<=0:
                break
   # finally:
    #    socket_temp.close()

def main():
    try:
        #创建tcpsocket
        tcpsocket = socket(AF_INET,SOCK_STREAM)
        tcpsocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        #绑定端口
        tcpsocket.bind(('',8989))
        #设置监听
        tcpsocket.listen()
        #创建进程池
        pool = Pool(5)
        #循环等待请求
        while True:
            newsocket,ipInfo = tcpsocket.accept()

            #为每一个请求创建进程为其服务
            pool.apply_async(deals,(newsocket,))
    finally:
        tcpsocket.close()
if __name__=="__main__":
    main()

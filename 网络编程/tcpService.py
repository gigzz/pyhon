from socket import *
tcpservice = socket(AF_INET,SOCK_STREAM)
#绑定端口和ip
tcpservice.bind(('',8986))
#设置监听
tcpservice.listen()
#等待请求
newsocket,clientInfo = tcpservice.accept()
#处理请求
content = newsocket.recv(1024)
print('%s%s'%(clientInfo,content))
newsocket.close()
tcpservice.close()

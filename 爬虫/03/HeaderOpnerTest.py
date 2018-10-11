# encoding:utf-8
# Resquest因为不支持代理,所以搜用opener,无法处理cookie

import urllib2
header = urllib2.ProxyHandler({"http":"101.37.79.125:3128"})
# 使用私密代理输入密码  密码正常不写在代码力为了安全放在系统环境变量(为成功没有.bash_profile文件)
# urllib2.ProxyHandler({"http":"用户名:密码@103.101.71.9:8080"})
openers = urllib2.build_opener(header)
content = openers.open("http://www.google.com").read()
# content = urllib2.urlopen('https://www.baidu.com').read()
# 设置后为全局可以直接调用ueropen()来实现
# urllib2.install_opener(openers)
print(content)



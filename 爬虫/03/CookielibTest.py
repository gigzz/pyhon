# encoding:utf8

import urllib2
import cookielib
import urllib
# 成功使用代理ip加上自动保存cookie(成功)
my_cookie = cookielib.CookieJar()
pox_header = urllib2.ProxyHandler({"http":"192.168.1.11:8888"})
header = urllib2.HTTPCookieProcessor(my_cookie)
my_opener = urllib2.build_opener(header, pox_header)
he = {


            "Connection": "keep-alive",

            "Cache-Control": "max-age=0",

            "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Language": "zh-CN,zh;q=0.9"
        }
# 可以使用addheaders来添加报头列表里面放元组
# my_opener.addheaders = [()]
datas= {
    # "email": "18350227230",
    # "password": "123456wq",
}
my_data = urllib.urlencode(datas)
urllib2.install_opener(my_opener)
my_opener.open('http://www.renren.com/PLogin.do', data=my_data)
html = urllib2.urlopen("http://www.renren.com/880792860/profile").read()

print(html)

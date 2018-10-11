# encoding:utf-8

# post请求练习 爬取有道(Y有问题)

import urllib2
import urllib
import random
import time
import hashlib
i = raw_input('需要翻译的内容')
"""  n = l.substr(0, 5e3),
    o = u.md5(S + n + r + D)
"""
S = "fanyideskweb"
n = i
D = "ebSeFb%=XZ%T[KZ)c(sy!"
# print((time.time())*100)
print(D)
my_times = (int(time.time()*1000))
r = str(my_times + random.randint(1,10))
o = hashlib.md5((S+n+r+D)).hexdigest()
print(o)
print(r)
data = {
"i":i,
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
'salt': r,
'sign' : o,
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_CLICKBUTTION",
"typoResult": "false"
}

header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
datas = urllib.urlencode(data)
my_requesr = urllib2.Request(url=url, data=datas, headers=header)
content = urllib2.urlopen(my_requesr).read()
# print(datas)
print(my_requesr.get_data())
print(content)
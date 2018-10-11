# encoding:utf-8
import urllib2
import urllib
import random
url = 'https://www.baidu.com'
ua = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50']
# 随机获取一个user-angent
user = random.choice(ua)
# 设置url
my_request = urllib2.Request(url)
# 设置响应头
my_request.add_header('User-Agent', user)
# 只有第一个单词大写其余小写
print(my_request.get_header('User-agent'))
# 接收字典 帮助解码
# url的get请求方式的中文是需要转吗的,使用需要使用
print(type(urllib.urlencode({'w':'你好'})))


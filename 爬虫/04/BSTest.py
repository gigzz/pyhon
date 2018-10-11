# encoding:utf8
# BeautifulSop的使用
import json
import jsonpath
import requests

ip_port = requests.get("http://ip.jiangxianli.com/api/proxy_ips").text
my_dic = json.loads(ip_port)
a = jsonpath.jsonpath(my_dic, "$..ip,port")
ipp = {}
for i in range(0,len(a)-1):
       ipp[a[i]] = a[i+1]

print(ipp)

# encoding:utf8
# BeautifulSop的使用
import json
import jsonpath
import requests


def get_ip():
    ip_port = requests.get("http://ip.jiangxianli.com/api/proxy_ips").text
    my_dic = json.loads(ip_port)
    ipp = []
    # print(my_dic['data'])
    for ic in my_dic['data']['data']:
        # print(ic)
        ip = ic['ip']
        port = ic['port']
        ipp.append({'ip_port': ip + ":" + port})
        # print(ip+port)
    # a = jsonpath.jsonpath(my_dic, "$..ip,port")

    # for i in range(0,len(a)-1):
    #     ipp.append( {'ip_port':a[i]+":"+a[i+1]})

    # print(ipp)
    # print(ipp)
    return ipp

if __name__ == '__main__':
    get_ip()

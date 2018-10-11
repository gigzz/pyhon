# encoding:utf8
from scrapy  import Request
from MiddleTest.settings import USER_AGENT
from MiddleTest.ip import get_ip
import random
import base64
class IpMiddle(object):

    def process_request(self, request, spider):
        # Request().headers
        # ip = random.choice(get_ip())
        # request.meta['proxy'] = "http://"+ip['ip_port']
        # 不需要密碼
        request.meta['proxy'] = "https://"+"192.168.1.11:8888"
        # print(ip)
        # x需要密碼的話
        # base = base64.b64decode("user:password")
        # request.meta['proxy'] = "https://"+"192.168.1.11:8888"
        # request.headers["Proxy-Authorization"] ="basic"+ base
        # print('中间件')

class UserAgent():
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT)
        request.headers.setdefault('User_Agent', user_agent)

        # 需要密碼的話
        # print(user_agent)
        # print(type(UserAgent))
        # request.headers()


if __name__ == "__main__":
    UserAgent().process_request(None, None)
    IpMiddle().process_request(None, None)

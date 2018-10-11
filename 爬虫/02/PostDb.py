# encoding:utf-8
import urllib2
import urllib


class MySpider(object):
    """
    抓取数据类
    """
    def __init__(self, urls, page, count):
        self.url = urls
        self.page = page
        self.count = count

    def send_request(self):
        """
        发送请求
        """

        header = {

        "Connection":" keep-alive",
        "Accept":" */*",
        "X-Requested-With":" XMLHttpRequest",
        "User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
        }
        data = {

            "type": "11",

            "interval_id": "100:90",

            "action": "",

            "start": self.page,

            "limit": self.count
        }
        data = urllib.urlencode(data)
        my_request = urllib2.Request(self.url, data=data, headers=header)
        print(urllib2.urlopen(my_request).read())

if __name__ == "__main__":
    url ="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="
    db = MySpider(url,1,20)
    db.send_request()

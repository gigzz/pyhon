#encoding:utf8
import requests
from lxml import etree
from threading import Thread
from Queue import Queue
import time
# 完成段子的多线成下载(可以使用)

# 爬取数据类
class SpiderPage(Thread):
    def __init__(self, page_queue,data_queue):
        super(SpiderPage, self).__init__()
        self.page_queue = page_queue
        self.data_queue = data_queue
    def run(self):
        print('正在抓取数据')
        he = {

            "Connection": "keep-alive",

            "Cache-Control": "max-age=0",

            "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        while True:
            try:
               urls = self.page_queue.get(block=False)
               print(urls)
               contrnt = requests.get(urls, headers=he).text
               self.data_queue.put(contrnt)
            except:
                print('结束抓取')
                break




# 数据处理类
class SpiderDate(Thread):
    def __init__(self, data_queue):
        super(SpiderDate, self).__init__()
        self.data_queue = data_queue

    def run(self):
        print('数据正在处理')
        while True:
            try:
                con = self.data_queue.get(block=True, timeout=1)
                htmls = etree.HTML(con)
                # 获取内容
                cons = htmls.xpath("//div[contains(@id,'content-left')]/div[contains(@id,'qiushi_tag_')]/a/div[@class='content']/span")
                # a = cons[0].xpath('./div/div/span/i')
                # print(str(len(a)))
                for i in cons:
                    with open('段子.txt', 'a')as f:
                        f.writelines("\n        "+i.text.strip('\n').encode('utf8'))
            except:
                print('下载完成')
                break

#主函数
def main():
    page_queue = Queue(13)
    data_queue = Queue()
    for i in range(1, 2):
        url = 'http://www.qiushibaike.com/8hr/page/'+str(i)+'/'
        page_queue.put(url)
    for i in range(5):
        my_spider = SpiderPage(page_queue,data_queue)
        my_spider.start()
        # my_spider.join()
    # time.sleep(5)
    # print(data_queue.get())
    for i in range(2):
        my_data = SpiderDate(data_queue)
        my_data.start()

if __name__ == "__main__":
    main()

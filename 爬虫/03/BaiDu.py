# encoding:utf-8

# 爬取  (可以使用)
from lxml import etree
import urllib2
class SpiderSina(object):
    def __init__(self, urls):
        self.url = urls

    def down_data(self):
        he = {

            "Connection": "keep-alive",

            "Cache-Control": "max-age=0",


            "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        re = urllib2.Request(self.url,headers=he)
        my_html = urllib2.urlopen(re).read()
        # self.deal_data(my_html)
        return my_html
    def deal_data(self, datas, select):
        print('正在处理数据.......')
        # print(data)
        htmls = etree.HTML(datas)
        # print(datas)
        titles = htmls.xpath(select)
        for i in titles:
            self.url = "http://tieba.baidu.com"+i
            content_html = self.down_data()
            content_html = etree.HTML(content_html)
            a =content_html.xpath('//div[contains(@id,"post_content")]/img[@class="BDE_Image"]/@src')
            for i in a:
                # 保持数据
                print("正在下载%s"%self.url[-8:])
                self.url = i
                img_content = self.down_data()
                with open(self.url[-8:],'wb') as f :
                    f.write(img_content)

    def contorl(self):
        re_select = '//a[@class="j_th_tit "]/@href'
        my_htmls = self.down_data()
        self.deal_data(my_htmls, re_select)
        print('谢谢使用')

if __name__ == '__main__':
    kw = raw_input('需要爬去哪个贴吧')
    url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%s&fr=search'%kw
    SpiderSina(url).contorl()

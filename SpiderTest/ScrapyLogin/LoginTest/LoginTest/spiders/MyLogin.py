# -*- coding: utf-8 -*-
import scrapy
# 使用cookie登入人人网(成功)

class MyloginSpider(scrapy.Spider):
    name = "MyLogin"
    # allowed_domains = ["www.baidu.com"]
    url = 'http://zhibo.renren.com/top'
    cookie = {
        "	anonymid": "jkxejwk2-aea5j0",
        "	_r01_": "1",
        "	_de": "553DAF6A8674D74AFF25AC6ADDFA252E",
        "	ln_uact": "18350227230",
        "	ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "	Hm_lvt_966bff0a868cd407a416b4e3993b9dc8": "1534590956,1534681124",
        "	depovince": "GW",
        "	ick_login": "e97d3406-cfe8-4c9e-a575-cf04770cb3de",
        "	jebecookies": "00f133b5-57a0-4dfd-a94b-fbcabbe8e3d8|||||",
        "	jebe_key": "215eb4db-8c75-420e-b050-0ae835d91e61%7C4127bba43e0995d37189e0a4ec8b98b8%7C1534680338059%7C1%7C1535159886212",
        "	p": "36a223b7d13a5695589943e176f4b7839",
        "	first_login_flag": "1",
        "	t": "05464f4896c143fbd2b76ce5ac7de9859",
        "	societyguester": "05464f4896c143fbd2b76ce5ac7de9859",
        "	id": "967597189",
        "	xnsid": "9145bcf8",
        "	loginfrom": "syshome",
        "	JSESSIONID": "abc_v7rMSHxnz63oKUUvw",

    }

    def start_requests(self):
        yield scrapy.FormRequest(self.url, cookies=self.cookie)

    def parse(self, response):
        print('23123213')
        # scrapy.FormRequest(cookies=self.cookie)
        print(response.text)

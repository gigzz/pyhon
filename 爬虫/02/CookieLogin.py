# encoding:utf-8
import urllib
import urllib2
# 使用已有的cookie登入 (成功)

class MySpider(object):
    def __init__(self, urls):
        self.url = urls

    def my_login(self):
        hedaer = {
            "Upgrade-Insecure-Requests": " 1",
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Cookie': 'anonymid=jkxejwk2-aea5j0; depovince=GW; _r01_=1; JSESSIONID=abc4GIoekIARmcWa3Rmvw; ick_login=9b7b3960-739c-4688-8136-1ad8b9703fec; jebe_key=215eb4db-8c75-420e-b050-0ae835d91e61%7Ccfcd208495d565ef66e7dff9f98764da%7C1534589892908%7C0%7C1534589899981; ick=1862f1e1-3423-4834-a431-139905ecc593; XNESSESSIONID=fe6982865644; wp_fold=0; jebecookies=5befcdc1-8f05-4d17-a434-9ce26a790c24|||||; _de=553DAF6A8674D74AFF25AC6ADDFA252E; p=cb05f11a632d5a5de8980bd16e1567149; first_login_flag=1; ln_uact=18350227230; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=ad1aa6780971f6e651e787384a3664ff9; societyguester=ad1aa6780971f6e651e787384a3664ff9; id=967597189; xnsid=b349759e; loginfrom=syshome'
           }
        my_request = urllib2.Request(url=self.url, headers=hedaer)
        print(urllib2.urlopen(my_request).read())

if __name__ == "__main__":
    url = 'http://www.renren.com/967597189/profile'
    rr = MySpider(url)
    rr.my_login()
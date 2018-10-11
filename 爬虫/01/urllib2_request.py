import urllib2

# 构建模拟的相应头信息为了反爬虫

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
      }

# 使用urllib.Request来构建,header必须是字典类型
my_request = urllib2.Request('https://www.baidu.com/',headers=ua)
response = urllib2.urlopen(my_request)
html = response.read()
print(html)

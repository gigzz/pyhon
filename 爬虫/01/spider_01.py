# encoding:utf-8
import urllib
import  urllib2
def down_file(html):
    print('正在下载...........')
    return html.read()
    """
    用于下载的页面
    """
    pass

def save(content,filename):
    """用于保存文件"""
    print('正在保存')
    with open(filename,'w') as f:
        f.write(content)

    pass

def deal_url():
    """
    用于处理url
    http://tieba.baidu.com/f?kw=python&pn=0
    """
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
      }
    text = raw_input('输入爬去的贴吧名')
    start_page = raw_input('从第几页开始')
    end_page = raw_input('到第几页')
    url_temp = 'http://tieba.baidu.com/f?'
    key_con = {'kw':text}
    cont = urllib.urlencode(key_con)
    for i in range(int(start_page),int(end_page)+1):
        pn = (i-1)*50
        url = url_temp+cont+'&pn='+str(pn)
        my_re = urllib2.Request(url,headers=ua)
        html = urllib2.urlopen(my_re)
        content = down_file(html)
        filename = str(i)+'.html'
        save(content,filename)
    print('欢迎使用')
        # print(html.read())

        # urllib2.Request(url,ua)

if __name__ == '__main__':
    deal_url()

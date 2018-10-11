# encoding:utf8
from selenium import webdriver
import time
import urllib2
from selenium.webdriver.chrome.options import Options
my_chrome = Options()

my_chrome.binary_location = "/opt/google/chrome/chrome"
my_chrome.add_argument('headless')
my_chrome.add_argument('--disable-gpu')
# /home/python/未命名文件夹
a = webdriver.Chrome(executable_path='/home/python/chromedriver/chromedriver', chrome_options=my_chrome)
a.set_window_size(1300,700)
# a.get('http://fanyi.youdao.com/')
a.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_607b409ce7654624af3f5524b0c252fd')
# a.save_screenshot('bidu.png')
time.sleep(2)
a.save_screenshot('s.png')
time.sleep(2)
cc = raw_input()
# time.sleep(1)
# time.sleep(10)
# time.sleep(10)
# a.find_element_by_id('inputOriginal').send_keys(u'你好吗我还好')
# a.find_element_by_id('transMachine').click()
# time.sleep(0.5)
# con = a.find_element_by_id('transTarget').text
# time.sleep(3)
a.save_screenshot('s.png')

a.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_607b409ce7654624af3f5524b0c252fd')
time.sleep(1)
a.save_screenshot('s.png')
a.quit()

# print(con.encode('utf-8'))
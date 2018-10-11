# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
# (未完工程)"""
class My12306(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.binary_location = "/opt/google/chrome/chrome"
        self.my_browser = webdriver.Chrome(executable_path='/home/python/chromedriver/chromedriver', options=self.options)

    def listen(self):
        a = {
            "	JSESSIONID": "92F61F9AD1F2A188F2F2184A2FD6711C",
            "	tk": "gO4qUrKqNQzmVer9I5M6y7rA8fe0eJTdHjClk-48xqc091210",
            "	_jc_save_wfdc_flag": "dc",
            "	_jc_save_detail": "true",
            "	_jc_save_fromDate": "2018-09-01",
            "	RAIL_EXPIRATION": "1535299938901",
            "	RAIL_DEVICEID": "aFztag-ziS9OAOrfCCiaYy4Q7PfJb9DGGBnVONosXPxEBlVetXN0WvWJGOcWKRrAGe5IxmcZVxxmt87Ox487U58LCVb4eDJuyD9qx_0oM5O45dCQPBK9TdcALSLQC2w3O7Uw9w7HAufl4JVPvzopJaaRNujibcfz",
            "	_jc_save_fromStation": "%u53A6%u95E8%u5317%2CXKS",
            "	_jc_save_toStation": "%u798F%u5B89%2CFAS",
            "	_jc_save_toDate": "2018-08-23",
            "	route": "495c805987d0f5c8c84b14f60212447d",
            "	BIGipServerotn": "48497162.64545.0000",
            "	BIGipServerpool_passport": "166527498.50215.0000"
        }
        self.my_browser.get('https://kyfw.12306.cn/otn/leftTicket/init')
        # self.my_browser.get_cookie("JSESSIONID=E74423C7774BF7F72196B4A4F02FA30B; tk=8HIFdyOGWHniLVkD18p2mmbjaPXdmR-5i4RA25Y6i0Qfs1210; _jc_save_wfdc_flag=dc; _jc_save_detail=true; _jc_save_fromDate=2018-09-01; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=351273482.64545.0000; RAIL_EXPIRATION=1535299938901; RAIL_DEVICEID=aFztag-ziS9OAOrfCCiaYy4Q7PfJb9DGGBnVONosXPxEBlVetXN0WvWJGOcWKRrAGe5IxmcZVxxmt87Ox487U58LCVb4eDJuyD9qx_0oM5O45dCQPBK9TdcALSLQC2w3O7Uw9w7HAufl4JVPvzopJaaRNujibcfz; _jc_save_fromStation=%u53A6%u95E8%u5317%2CXKS; _jc_save_toStation=%u798F%u5B89%2CFAS; _jc_save_toDate=2018-08-23; BIGipServerpool_passport=166527498.50215.0000")
        self.my_browser.add_cookie({'name': 'cookie', 'value':a})
        self.my_browser.get('https://kyfw.12306.cn/otn/leftTicket/init')
        # time.sleep(3)
        # self.my_browser.save_screenshot('kan.png')
        # pass

    def login(self):
        pass

    def select(self):
        pass

    def buy_12306(self):
        pass

    def close(self):
        self.my_browser.close()

if __name__ == "__main__":
    my12306 = My12306()
    my12306.listen()
    # a = 'Cookie: JSESSIONID=2EF705C80E722F9B9B9CE91DC6F8F42F; tk=jNtorCJOqirSPc2cGES4dniSLdUPSLRLPRJz5oislcwsd1210; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=99615242.50210.0000; RAIL_EXPIRATION=1535311672511; RAIL_DEVICEID=Rm7bW8xMmDQvoSOxlxe0f9HcRHGmPUPIqSBCBAXcwc6rJEGPoTkakr5dFemh8SCK2I9o3mdOwRjK5wDq-OIR4UGP_NrR86pz5htuKgLE1E6DxRS9LfX6tSiw30fo_yEn2BUDao572BEerbbBHhknknD5t7r6WR4V; BIGipServerpool_passport=250413578.50215.0000'
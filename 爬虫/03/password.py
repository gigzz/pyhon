#encoding:ytf8

import urllib2
password_mg = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mg.add_password(None, "www.baidu.com", '123', '123')
pass_head = urllib2.HTTPBasicAuthHandler(password_mg)
openers = urllib2.build_opener(password_mg)

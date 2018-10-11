
import pymysql
try:
    mysqls = pymysql.connect('192.168.1.11', 'root', '123456', 'test', charset='utf8')
    cu = mysqls.cursor()
    cu.execute('select * from stude where name = "小明" or 1=1')
    cu.fetchone()
    cu.fetchall()# fetch表示去所有
    for i in cu:
        print(i)
    cu.close()
    mysqls.close()
except Exception:
    print('出错')

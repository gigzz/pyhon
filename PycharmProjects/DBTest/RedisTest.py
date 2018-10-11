from redis import StrictRedis
import pymysql
# try:
r = StrictRedis(host='localhost', port=6379, db=0,encoding='utf8')
sql = pymysql.connect(host='192.168.1.11', password='123456',
                      user='root', database='radis',charset='utf8')
# redis = StrictRedis.from_url('redis://@localhost:6379/1')
cu = sql.cursor()
name = input('用户名')
password = input('密码')
if not r.get(name):
    cu.execute('select * from user where name=%s',args=[name])
    users= cu.fetchone()
    if not users:
        print('用户名错误')
    else:
        r.set(users[1],users[2])
        if users[2] == password:
            print('成功')
        else:
            print('密码错误')
elif r.get(name).decode('utf8')== password:
    print('成功')
else:
    print('密码错误')
# except Exception:
#     print('连接失败')

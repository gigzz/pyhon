from pymongo import MongoClient

# client1 = MongoClient()# 默认端口和主机ip地址链接
# client2 = MongoClient('mongodb://admin:123456@localhost:27017/admin')# 有身份验证
client2 = MongoClient('localhost', 27017)
# 等于命令行的use test1
# 切换数据库
mydb = client2.test1
# 选择集合
db = mydb.find
# 插入一条语句
# db.insert_one({'name': '小白'})
# 插入多条
# db.insert_many([{'name': '小红', 'age': 12}, {'name': 'qb', 'age': 89}])
# 第一个为条件 第二个为改为什么
# db.update_one({'name': '小红'}, {'$set': {'name': '白白', 'aaa': 'sdasdsdsa'}})
# 修改多个
# db.update_many({'name': '小白'}, {'$set': {'name': '嘿嘿', 'aaa': 'sdasdsdsa'}})
# 删除一个
# db.delete_one({'name': '嘿嘿'})
# 删除多个
# db.delete_many({'name': '嘿嘿'})
# 查询多个
cur = db.find({'name': '白白'}).sort([('_id', 1)]).skip(0).limit(1)
for i in cur:

    print(i)





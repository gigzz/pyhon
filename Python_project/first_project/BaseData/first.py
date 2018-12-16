# # import re
# # a = 3.14
# # b = "xiaoba"
# # c = '180'
# # print("%d   %d %d"%(a,a,a))
# # print(type(a))
# # a="""https//www.baidu.com"""
# # opinion = ('http','https')
# # re.findall()
# # print()
# # [s,s,s]列表 （s,s,s）元素 {s,s,s}set集合 {key:value}字典
# # # 数组合并为字符串
# # List = ['I','LOVE','YOU','你',1]
# # # 以什么做分隔符
# # newList = ' '.join(List)
# # print(newList)
# # 对比列表和字符串的区别，没有区别!!
# # list = 'abcdefgh'
# # list2 = ['a','b','c','d','e','f','g','h']
# # print(list[1:5])
# # print(list2[1:5])
#
# #列表的合并
# # a = [1,2,3]
# # b = [4,5,6]
# # print(a+b)
#
# # 是否在列表中
# # a = [1,2,3,4,5,6]
# # print(1 in a)
#
# #判断多个值是否在列表中
# # a = [1,2,3,4,5,6,7,8,9]
# # print(set([1,4]) <= set(a))
#
# # 元组，不能修改值，其他和列表类似
# # a=(1,)
# # b = a+(1,1)
# # print(type(a),a,b)
#
# # set 集合 无序不重复 创建：{1，1}或set(),创建空的集合时不能使用{}，{}是创建字典的方法
# # - | & ^ <=(判断是否存在集合中) 数学里的集合的运算一样
# # print(set([1,2,3]) <= set([1,2]) )
#
# # 字典
## a = {1:"first",2:"tow",3:"three"}

# # 删除
# # del a['1']
# # 添加
# # a['5']  = "five"
# # a['4']  = "five"
# # 取值
# # a['2']
# # 排序
# # sorted(a.keys())
# # 是否存在
# # c = "tow" in a.values()
# #  dict 将 key = value或 (key,value) 转换成字典
# # f = dict([(1,2),(3,4)])
# # f = dict(ac=2,fv = 3)
# # print(list(a.keys()),c,f)
#
# ##pandas 是python的库
# # from pandas import Series;
# # s = Series(['1','2','3'])
# # s = s.append(Series(['s'],index=[4]),)
# # s = s.append(Series(['w']))
# # s = s.append(Series(['w']))
# # print(s)
# # print(s.values)
#
# # from pandas import DataFrame
# # dic = {'name':['小白','小黑','小红'],'age':[2,3,4]}
# # df = DataFrame(dic)
#
# #访问第0行到第一行的数据
# # print(df)
# # 这是第0行到第一行的第0列到第0列的数据
# # print(df.iloc[0:2,0:1])
# # 修改列名
# # df.columns = ["names",'namess']
# #修改索引
# # df.index = range(0,3)
# # df.loc[len(df)+1] = ['小芬',33]
# # print('长度' + str(len(df)))
# # print(df)
#
# #判断
#
#
# # if  (1 > 2 or 3<4):
# #     elif False:
# #         print('输出')
# #     print("ss")
# # name = '小黑'
# # if name =='小白':
# #      print(name)
# #      print(name+'ss')
# # elif name=='小黑':
# #     print(name + 'ss')
# # else:
# #     print("错误")
#
# # 循环
# # for i in range(10):
# #     print(i)
# #
# # for a in '厦门理工':
# #     print(a)
# # [s,s,s]列表 （s,s,s）元素 {s,s,s}set集合 {key:value}字典
# # list=['第一','第二','第三']
# # # for str in list:
# # #     print(str)
# from pandas import Series,DataFrame
# # x = Series(['第一','第二','第三'])
# # for i in x.index:
# #     print(i)
#
# # x = DataFrame({'name':[1],'age':[1]})
# # x = DataFrame({
# #     'name':Series(['第一','第二','第三']),
# #     'age':Series(['第一','第二','第三'])
# # })
# #
# # for a in x.:
# #     print(x)
#
#
# # Demo 打印三角形
#
# # for count in range(1,10):
# #     print(' '*(10-count)+"*"*(2*count-1))
# # i = 0
# # while i<10:
# #     i+=1
# #     print(' ' * (10 - i) + "*" * (2 * i - 1))
#
# # for temp in range(1,1000000000000000000000000000000000000000000000000000000000000):
# #     if temp%2==0:
# #         print(temp,end='\n')
# #         if temp == 20:
# #             break
#
# # list = [1,2,'3']
# # #
# # # a,b,c = list
# # # print(a,b,c)
# # tuples = (1,2,3,4,5)
# # dics = {"name":'小编','age':"32"}
# # print(**dics)
#
# # 文件读写
# # f = open("../Grammar/GrammarFirst.py",'r',encoding='utf-8')
# # while True:
# #     content = f.read(1024)
# #     if len(content)==0:
# #         break
# #     else:
# #         print(content)
# #
# # f.seek()
#
# # # 批量重命名
# # import os
# # list = os.listdir('../Grammar')
# # for name in list:
# #     os.rename(name,'s')
#
# # list = [1,2,3,44,55,66,77,88]
# # list2 =[1,44,55]
# # for item in list2:
# #     list.remove(item)
# #
# # print(list)
# # import sys
# # sys.path.append('../Grammar')
# # sys.path.append('../ClassStudy')
# # print(sys.path)
# #
# # import Dog
# # import copy
# # a = [1,2,3,4]
# # b = [7,8,9]
# # c = (a,b)
# #
# # e = copy.deepcopy(c)
# # print(id(e))
# # print(id(c))
# #
# # a = 0o123
# # print(a)


# # 迭代
# x = [i for i in range(10) ]
# print(x)
# y =(i for i in range(10))
# print(next(y))
# print(next(y))
#  next()c __next__()
# def nums():
#     for i in range(4):
#         for j in range(3):
#             yield (i,j)
# d=nums()
# print(d.__next__())
# print(next(d))
# print(next(d))

# send
def nums():
    for i in range(4):
        for j in range(3):
           temp = yield (i,j)#当c对象调用send方法时y
                        # ield会返回这个seng的方法传入的值，前提必须在调用了
                        #next后。
           print(temp)
c = nums()
#
c.__next__()
c.send('hh')
# c.__next__()

# 判断是否可以迭代
# from  collections import Iterable
# print(isinstance([1,2],Iterable))

# 迭代器 可以使用next()的对象属于迭代器
# from collections import Iterator
# print(isinstance((x for x in range(5)),Iterator))

# 将可迭代的对象转换为迭代器
# str = iter('sssssffff')
# print(next(str))

# 闭包 作用重复的数据不需要重新输入,主要有变量指向num2那么重新调用num不会修改之前的数据
# def num(x,y):
#     def num2(a):
#         print(a*x+y)
#     return num2
#
# first = num(2,3)
# first(3)
# first(2)

# 装饰器
#

# 万能方法装饰器
# def num(func,*args,**kwargs):
#     def num2(*args2):
#         print('dsadsa')
#         func()
#     return num2
# @num
# def test():
#     print('------验证')
# test()

# 给实例对象动态添加属性和方法
# import  types
# class test(object):
#     # 禁止添加属性的，将已有的属性写入集合中
#     # __slots__ = {'name'}
#     def __init__(self):
#         self.name = '小白'
#
# ob = test()
# # 添加属性
# ob.age = 12
# # 添加方法
# def getAge(self):
#     return self.age
# ob.getage = types.MethodType(getAge,ob)
# print(ob.getage())
# print(ob.__dir__())

# # 给类对象添加类属性，类方法和静态方法
# class test(object):
#     # 禁止添加属性的，将已有的属性写入集合中
#     # __slots__ = {'name'}
#     def __init__(self):
#         self.name = '小白'
# 添加类属性
# test.age = '33'
# print(dir(test))
# 添加类方法
# def getAge(cls):
#     return cls.age
# 类方法也需要使用 使用Type
# test.getAge = types.MethodType(getAge,test)
# 添加静态方法
# @staticmethod
# def staticm():
#     print('静态方法')
# test.staticm = staticm
# print(test.getAge())
# test.staticm()
# a = test()
# print(a.getAge())

# 新建进程 (在window系统下无法使用)
# import os
# os.fork()
# print()

# 线程在进程里
#
# from multiprocessing import Pool
# p = Pool(3)
# p.join()



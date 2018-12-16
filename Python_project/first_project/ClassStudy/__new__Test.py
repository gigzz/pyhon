# class newTest(object):
#     def __new__(cls):
#         print('.....')
#         return object.__new__(cls)
#
#     def run(self):
#             print('跑')
#
#
# newtest = newTest()
# newtest.run()

# 单例模式
class single(object):
    newcls = None
    def __new__(cls):
        if not single.newcls:
            single.newcls = object.__new__(cls)
            return single.newcls
        else:
            return single.newcls

print(id(single()))
print(id(single()))
print(id(single()))


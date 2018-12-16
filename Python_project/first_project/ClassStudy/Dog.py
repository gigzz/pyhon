# class Dog(object):
#     TestAtt = "测试"
#     # 类实例方法
#     # 初始化
#     def __init__(self, DogName, DogAge):
#         self.DogName = DogName
#         self.DogAge = DogAge
#     # 类实例方法
#
#     def __str__(self):
#         print('%s的名字，%d岁' % self.DogName % self.DogAge)
#     # 类实例方法
#     def test(self):
#         print('输出')
#     #    类对象方法
#     @classmethod
#     def supers(cla):
#             print('')
#
#     #类的静态方法
#     @staticmethod
#     def static():
#         print()
#
#
#
# class1 = Dog('小白', 2)
# class2 = Dog('小黑', 3)
# class1.TestAtt = '修改数据'
# print(class2.TestAtt)
# print()
# print(Dog.TestAtt)
# print('新添加')


# class person(object):
#     def __init__(self):
#         self.__name = None
#     # def __getname(self):
#     #     return self.__name
#     # def __setname(self,name_temp):
#     #     self.__name = name_temp
#     # name = property(__getname,__setname)
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name_temp):
#         self.__name = name_temp
#
# superman = person()
# superman.name = '1'
# print(superman.name)
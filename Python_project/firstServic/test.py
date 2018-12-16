import re
#
# s =""<div><p>岗位职责：</p> <p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p> <p><br></p> <p>必备要求：</p> <p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p> <p>&nbsp;<br></p> <p>技术要求：</p> <p>1、⼀年以上	Python	开发经验，掌握⾯向对象分析和设计，了解设计模式</p > <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p> <p>3、掌握关系数据库开发设计，掌握	SQL，熟练使⽤	MySQL/PostgreSQL	中 的⼀种<br></p> <p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>
# ""
#
#
# def res(result):
#     r =result.group()
#     print(r)
#     return ''
#
#
# strs = re.sub(r'<\s*/?\w+\s*>',res,s)
#
# print(strs)
s = "php:1000 python,java,javascript,c"
ss =re.split(r'[:,/]',s)
print(ss)


class Note(object):
    def __init__(self,emev):
        self.emev = emev
        self.next = Note


# 冒泡排序
def sort1(my_list):
    for i in range(len(my_list)-1):
        count = 0
        for j in range(len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                count += 1
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]


#  选择排序
def sort2(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_index = i
        for j in range(1+i, n):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]


# 插入排序
def sort3(my_list):
    n = len(my_list)
    for i in range(1, n):
        while i > 0:
            if my_list[i] < my_list[i-1]:
                my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
                i -= 1
            else:
                break


# 希尔排序
def sort4(my_list):
    n = len(my_list)
    group = n//2
    while group > 0:
        for i in range(group, n):
            while i - group >= 0:
                if my_list[i] < my_list[i-group]:
                    my_list[i], my_list[i-group] = my_list[i-group], my_list[i]
                i -= group
        group = group//2


# 快速排序（懵懂,重点）
def sort5(lt, s, e):
    if s >= e:
        return
    low = s
    high = e
    mid = lt[low]
        # while low <= high:
    while high > low:
        while high > low and mid <= lt[high]:
            high -=1
        lt[low] = lt[high]
        while high > low and mid > lt[low]:
            low += 1
        lt[high] = lt[low]
    lt[low] = mid
    sort5(lt, s, high-1)
    sort5(lt,high+1,e)



def before(self,tree):
    if len(tree) == 1:
        print(tree)
        return
    elif root.left is not None:
        print(root.left)
        before(root.left)
    elif root.righ is not None:
        before(root.righ)





if __name__ == "__main__":
        a = [60, 3, 2, 50, 3, 65, 23, 98, 2, 344, 34, 89, 2137, 43]
        sort5(a, 0, len(a)-1)
        print(len(a))
        print(a)

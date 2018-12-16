import time


# 需要传入两个值 第一个为用户的请求参数，第二个为处理响应头的方法
def interface(option, head):
    # 一个参数为状态信息，第二个为响应消息
    # head(state, response)
    # wsgi规定返回值只能是消息体数据
    return time.ctime()

if __name__ == "__main__":
    start = time.time()
    for a in range(0,1001):
        for b in range(0,1001):
            for c in range(0,1001):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    print(a,b,c)
    print(time.time()-start)






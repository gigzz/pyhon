# 本田车类
class bentian(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + '车在跑')

    def stop(self):
        print(self.name + '车停下了')


# 汽车工厂的父类
class factory(object):
    def creat(self, cartype):
        if cartype == '本田':
            return bentian('本田')


# 商店的父类
class store(object):
    def buy(self, cartypes):
        return factory().creat(cartypes)


bencar = store().buy('本田')
bencar.run()
bencar.stop()

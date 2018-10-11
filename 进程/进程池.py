from multiprocessing import  Pool
def test(op):
    print("------%s进程---------"%op)

p  = Pool(3)
for i in range(5):
    p.apply_async(test,(i,))
p.close()
p.join()
print("父亲进程结束")
#join()必须配合close()来等带子进程否则父类执行完程序直接结束不会等待只类进程是否完成

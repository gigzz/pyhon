from multiprocessing import Process 
import time
def test(): 
    while True:
        print("子进程")
        time.sleep(1)
p =Process(target = test)
p.start()#执行代码
#加join父类会等带子类完成后在往下执行，不加的话父类会先执行完，然后在等带子类执行完后##在结束程序
p.join()
print("父类代码")

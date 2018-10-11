import os
from multiprocessing import Pool,Manager
#创建文件

#读取和复制文件
def copys(oldName_temp,newName_temp,file_temp_temp,queue_temp):
    fr = open("../"+oldName_temp+"/"+file_temp_temp)
    fw = open("../"+newName_temp+"/"+file_temp_temp,'w')
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue_temp.put(file_temp_temp)
#主程序控制
def main():
    oldName = input("输入需要拷贝的文件名")
#print(oldName)
    newName = oldName+"副本"
    files = os.listdir("../进程")
    os.mkdir("../"+newName)
    #创建新进程执行任务
    pool = Pool(5)
    queue = Manager().Queue()
    for file_temp in files:
        pool.apply_async(copys,(oldName,newName,file_temp,queue))
    count = 0
    for i in files:
        queue.get()
        count+=
        print("当前进度%d%%"%(count/len(files)*100))

if __name__ =="__main__":
    main()

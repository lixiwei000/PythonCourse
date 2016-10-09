from multiprocessing import Process,Queue,Array,Value,Manager
from threading import Thread
from queue import Queue as Q2
import time


def run(infoList,n):
    infoList.append(n)
    print(infoList)

def processRunQueue(q,n):
    q.put([n,"hello"])
    print(q.get())
    print(q.get())

def processRunVA(num,array):
    num.value = 3.1415926
    for i in range(len(array)):
        array[i] = - array[i]

def processRunManager(d,l):
    d[0]  = '1'
    d['1'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    '''
    multiprocessing中的Queue可以被多个 进程 共享
    而queue.Queue 是不能被进程共享的
    '''
    # infoList = []
    # q = Queue()
    # q = Q2()
    # q.put("测试Queue被克隆了几份")
    # for i in range(5):
    #     p = Process(target=processRunQueue,args=(q,i))
    #     p.start()
    # t = Thread(target=run,args=(infoList,i))
    # t.start()
    # time.sleep(1)
    # while not q.empty():
    #     print(q.get())

    #  测试 Value Array 共享内存
    # num = Value('d',0.0)
    # array = Array('i',5)
    # for i in range(5):
    #     array[i] = i
    # for i in range(5):
    #     p = Process(target=processRunVA,args=(num,array))
    #     p.start()
    # time.sleep(1)
    # print(num.value,array[:])

    # 测试Manager共享内存
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p = Process(target=processRunManager,args=(d,l))
    p.start()
    p.join()
    print(d)
    print(l)
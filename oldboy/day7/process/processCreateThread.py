from threading import Thread
from multiprocessing import Process,Queue
import time
def processFun(q,i):
    q.put(i)
    for x in range(4):
        t = Thread(target=threadFun,args=(q,i+x+1))
        t.start()

def threadFun(q,i):
    q.put(i)

if __name__ == "__main__":
    queue = Queue()
    for i in [x for x in range(50)][::5]:
        p = Process(target=processFun,args=(queue,i))
        p.start()
    resList = []
    time.sleep(1)
    while not queue.empty():
        resList.append(queue.get())
    resList.sort()
    print(resList)
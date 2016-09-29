from threading import Thread,Lock,RLock,Semaphore
import time
import random

n = 0
lock = Lock() # 正常锁
# lock = RLock() # 递归锁
semaphore = Semaphore(5)
def count():

    time.sleep(1)
    global n
    lock.acquire()
    n = n + 1
    lock.release()
    print("%s\n" % n)

# 死锁
def lockTest():
    lock.acquire()
    print("第一层锁 ")
    lock.acquire()
    print("第二层锁")
    lock.release()
    lock.release()

# 信号量
def semaphoreTest():
    semaphore.acquire()
    print("信号量测试")
    time.sleep(1)
    semaphore.release()

if __name__ == "__main__":
    # lockTest()
    threadList = []
    for i in range(1000):
        threadList.append(Thread(target=semaphoreTest))

    for t in threadList:
        t.start()
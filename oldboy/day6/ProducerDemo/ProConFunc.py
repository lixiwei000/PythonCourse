

from threading import Thread
import time
from queue import Queue

def Producer(name,cart):

    while True:
        if not cart.full():
            time.sleep(1)
            cart.put("包子")
            print(name,"生产了一个包子")

def Consumer(name,cart):

    while True:
        if not cart.empty():
            time.sleep(1)
            try:
                print(name,"吃了一个包子",cart.get_nowait())# 阻塞/非阻塞
            except Exception as e:
                print("没有包子了")

if __name__ == "__main__":
    cart = Queue(100)
    for i in range(15):
        producer = Thread(target=Producer,args=("生产者%d" % i,cart))
        producer.start()
    for i in range(10):
        consumer = Thread(target=Consumer,args=("消费者%d" % i,cart))
        consumer.start()


from threading import Event, Thread
import time


def Producer(event):
    print("老板:等待有人来买包子")

    event.wait()
    event.clear() # 如果不加clear  那么set一直为true,Consumer中的wait将不阻塞而继续执行,导致最后两句位置颠倒
    print("老板:好的,等会我给你做..")
    time.sleep(3)
    print("老板:做好了,给你吧")
    time.sleep(1 )
    event.set()

def Consumer(event):
    print("吃货:老板,来二斤包子")
    event.set()
    time.sleep(2)
    event.wait()
    print("吃货:给你钱,拜拜")

if __name__ == "__main__":
    event = Event()
    producer = Thread(target=Producer,args=(event,))
    producer.start()
    consumer = Thread(target=Consumer,args=(event,))
    consumer.start()

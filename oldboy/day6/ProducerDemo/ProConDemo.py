from queue import Queue
from threading import Thread
import time


class Producer(Thread):
    def __init__(self, name, cart):
        self.__Name = name
        self.__Cart = cart
        super().__init__()

    def run(self):
        while True:
            if not self.__Cart.full():
                time.sleep(0.01)
                cart.put("包子")
                print(self.__Name, "生产包子")


class Consumer(Thread):
    def __init__(self, name, cart):
        self.__Name = name
        self.__Cart = cart
        super().__init__()

    def run(self):
        while True:
            if not self.__Cart.full():
                time.sleep(1)
                cart.get()
                print(self.getName(), "吃包子")


class Supervisor(Thread):
    def __init__(self, name, cart):
        self.__Name = name
        self.__Cart = cart
        super().__init__()

    def run(self):
        while True:
            time.sleep(1)
            print(self.__Name, cart.qsize())


if __name__ == "__main__":
    cart = Queue(1000)
    for i in range(3):
        p = Producer("厨师-" + str(i + 1), cart)
        p.start()
    for i in range(30):
        c = Consumer("吃货-" + str(i + 1),cart)
        c.start()
    admin = Supervisor("包子数量监督员",cart)
    admin.start()

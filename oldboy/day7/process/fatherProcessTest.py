from multiprocessing import Pool,Process
import os
import time
from threading import Thread

def info():
    print("Module Name : ",__name__)
    print("Current Pid :",os.getpid())
    print("Parent Pid :",os.getppid())

def f(name):
    info()
    print("Hello",name)

if __name__ == "__main__":
    f("Main")
    print("=================")
    p = Process(target=f,args=("Son Process",))
    p.start()
    time.sleep(1)
    print("=================")
    t = Thread(target=f,args=("Son Thread",))
    t.start()

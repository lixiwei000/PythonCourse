from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        print("This is My Thread")
        Thread.run(self)


def foo(args):
    print(args)

def show():
    for i in range(10):
        time.sleep(0.01)
        print(i)

def threadTest():
    thread = Thread(target=foo,args=("HelloWorld",))
    thread.start()
    # 设置线程名称
    thread.setName("Foo线程")
    print(thread.getName())
    showThread = Thread(target=show)
    # 是否为守护进程
    print(showThread.isDaemon())
    # 设置为守护线程 让主线程不需要等待守护进程完成才结束
    # 当主线程结束时,守护线程即时没有执行完 也会被销毁
    # showThread.setDaemon(True)
    showThread.start()
    print(showThread.getName())
    # join方法将暂时阻塞当前线程,让子线程先执行,子线程执行完毕后再继续当前线程
    showThread.join()
    # showThread.join()
    print("主线程即将结束")




if __name__ == "__main__":
    threadTest()
    # myThread = MyThread(target=foo,args=(1,))
    # myThread.start()
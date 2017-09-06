# -*- coding: utf-8 -*-

# Tip36: 用subprocess模块来管理子进程
import subprocess
import threading
from Queue import Queue
from time import time, sleep

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def sub_process_test1():
    """
    使用Popen构造器来启动进程
    communicate方法读取紫禁城的输出信息，并等待其终止
    """
    proc = subprocess.Popen(['echo', 'Hello NikoBelic'], stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print out.decode('utf-8')


def sub_process_test2():
    """ 使用poll查询子进程状态 """
    proc = subprocess.Popen(['sleep', '0.1'])
    while proc.poll() is None:
        print 'Working'
    print 'Exit status', proc.poll()


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


def sub_process_test3():
    """ 测试并行的性能，10个单个耗时1秒钟的任务，串行需要10秒，并行只需要1秒"""
    start = time()
    procs = []
    for _ in range(10):
        proc = run_sleep(1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time()
    print 'Finished in %.3f seconds' % (end - start)


# Tip37: 可以用现成来执行阻塞式IO，但不要用它做平行计算

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


def do_factorize():
    numbers = [12431241, 42352452, 4574543, 1231224]
    start = time()
    for number in numbers:
        list(factorize(number))
    end = time()
    print 'It tooke %.3f seconds' % (end - start)


def parallel_do_factorize():
    """ 改成并行模式发现时间还长了，因为是Python的GIL缘故，导致CPU不能真正的并行 """
    numbers = [12431241, 42352452, 4574543, 1231224]
    start = time()
    threads = []

    def run(number):
        list(factorize(number))

    for number in numbers:
        thread = threading.Thread(target=run, args=(number,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time()
    print 'It tooke %.3f seconds' % (end - start)


# Tip 38: 在县城中使用Lock来防止数据竞争
class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        """ A += B 会拆分三步进行计算，在多线程切换的情况下，会出现新值被旧值替换的问题 """
        self.count += offset


def worker(how_many, counter, split_num):
    for _ in range(how_many / split_num):
        counter.increment(1)


def run_threads(func, how_many, counter):
    threads = []
    split_num = 5
    for _ in range(split_num):
        args = (how_many, counter, split_num)
        thread = threading.Thread(target=func, args=args)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def do_incr():
    how_many = 10 ** 5
    # counter = Counter()
    counter = LockCounter()
    run_threads(worker, how_many, counter)
    print 'should be %d , found %d' % (how_many, counter.count)
    # should be 100000 , found 67760


class LockCounter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


# Tip 39: 用Queue来协调各线程之间的工作

from collections import deque, namedtuple


class MyQueue(object):
    """ 自定义队列模型 """

    def __init__(self):
        self.items = deque()
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(threading.Thread):
    """ 消费者线程 """

    def __init__(self, func, in_queue, out_queue):
        super(Worker, self).__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                self.in_queue.get()
            except IndexError:
                sleep(0.01)  # No work to do
            else:
                result = self.func()
                self.out_queue.put(result)
                self.work_done += 1


def download():
    print '正在执行 download 任务...'


def resize():
    print '正在执行 resize 任务 ...'


def upload():
    print '正在执行 upload 任务...'


def do_work_with_my_queue():
    """
    这种消费者生产者模型有4个缺点：
    1. 当消费者无法从队列中获取数据时，会导致CPU空转，浪费资源
    2. Worker的run方法会一直执行其循环，即使应该退出了也不会停止
    3. 为了判断所有任务是否已经处理完毕，需要一直循环检查
    4. 如果某个步骤停滞，将导致内存溢出、程序崩溃
    """
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()
    done_queue = MyQueue()

    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue)
    ]

    for thread in threads:
        thread.start()

    download_num = 1000
    for _ in range(download_num):
        download_queue.put(object())

    while len(done_queue.items) < download_num:
        continue
    processed = len(done_queue.items)
    polled = sum(t.polled_count for t in threads)
    print 'Processed', processed, 'items after polling', polled, 'times'
    # Processed 1000 items after polling 3013 times


def test_queue():
    queue = Queue(1)

    def consumer():
        print 'Consumer waiting'
        queue.get()  # will blocked if queue is empty
        print 'Consumer done'

    def producer():
        print 'Producer putting'
        queue.put(object())  # will blocked if queue is full

        print 'Producer done'

    for _ in range(10):
        threading.Thread(target=producer).start()

    print 'Will consume the items'
    for _ in range(10):
        threading.Thread(target=consumer).start()

    queue.task_done()


class ClosableQueue(Queue):
    """ 使用Queue来解决以上问题 """
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()

            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        super(ConsumerThread, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            self.queue.get()
            print threading.currentThread().getName() + " 消费了 "
            sleep(1)


class ProducerThread(threading.Thread):
    def __init__(self, queue):
        super(ProducerThread, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            self.queue.put('1')
            print threading.currentThread().getName() + " 生产了 "
            sleep(1)


def do_consume_produce():
    queue = ClosableQueue()

    ProducerThread(queue).start()
    ConsumerThread(queue).start()


# Tip 40: 考虑用携程来并发地运行多个函数

def my_coroutine():
    while True:
        received = yield
        print 'received', received


def do_test_coroutine():
    it = my_coroutine()
    next(it)
    it.send('First')
    it.send('Second')


def minimize():
    current = yield
    while True:
        value = yield current  # 实际上这里会拆分为两步： 返回current，等待下一个send参数
        current = min(value, current)


def do_test_minize():
    it = minimize()
    next(it)

    print it.send(10)
    print it.send(4)
    print it.send(22)
    print it.send(-1)


# Tip 41: 考虑用concurrent.futures来实现真正的平行计算

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def do_calc_gcd():
    numbers = [(4325435, 3453463), (756756734, 43263546), (4564565, 234523546), (46575467, 23421345)]
    # numbers = [(4325435, 3453463)]
    start = time()
    # results = list(map(gcd, numbers))  # 单线程 7s
    # pool = ThreadPoolExecutor(max_workers=4) # 线程池方法 12s
    pool = ProcessPoolExecutor(max_workers=4)  # 进程池方法 4s
    result = list(pool.map(gcd, numbers))
    end = time()
    print 'Took %.3f seconds' % (end - start)


if __name__ == '__main__':
    do_calc_gcd()

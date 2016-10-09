from multiprocessing import Pool
import time
def fun(x):
    time.sleep(1)
    print(x*x)
    return x*x

if __name__ == "__main__":
    # 写法1
    pool = Pool(5)
    print(pool.map(fun,range(10)))
    # for x in map(fun,range(10)):
    #     print (x)

    # 写法2
    # pool = Pool(processes=4)
    # resList = []
    # for x in range(10):
    #     res = pool.apply_async(fun,args=(x,))
    #     resList.append(res)
    #
    # for x in resList:
    #     print(x.get())

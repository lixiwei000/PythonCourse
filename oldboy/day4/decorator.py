'''
装饰器
    装饰器本身是一个函数,装饰器和函数连接使用@符号来装饰需要被装饰的函数


流程:
    程序被执行,从上往下解释
    解释到outer时,将outer加载进内存
    解释道@outer时,解释为outer(func1)
    执行outer函数->将wrapper函数加载到内存->返回wrapper函数的引用
    对func1进行一次赋值,值为返回的wrapper函数
'''

def outer(func):
    def wrapper(args):
        print("Wrapper")
        return func(args)
    return wrapper

@outer
def func1(args):
    print("Func1",args)
    return "Fuck Off"

'''
将装饰器中 函数执行前和执行后的代码 封装到方法选中,传入装饰器
'''
def Filter(before_func,after_func):
    def outer(func):
        def wrapper(msg,args):
            before_result = before_func(msg)
            print(before_result)
            func_result = func(msg,args)
            print(func_result)
            after_result = after_func(msg)
            print(after_result)
        return wrapper
    return outer


def before_func(msg):
    print("Before Function Doing...")
    return msg

def after_func(msg):
    print("After Function Doing...")
    return msg

@Filter(before_func,after_func)
def func2(msg,args):
    print("Func2 Doing...")


if __name__ == "__main__":
    # result = func1("NikoBelic")
    # print(result)
    func2("MSG","FuckOff")
    # func3()
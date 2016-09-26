class Father:

    def __init__(self):
        print("I am father..")

    def habbit(self):
        print("抽烟喝酒烫头")

class Alive:

    def __init__(self):
        print("I am avlive")

    def habbit(self):
        print("Breath...")

# 多继承  从最左边开始 广度优先搜索 取第一个搜索到的返回
class Son(Father,Alive):

    def __init__(self):
        super(Son,self).__init__()
        print("I am son...")

    def show(self):
        print("This is Son's function")
# 抽象类 + 抽象方法 = 接口
from abc import ABCMeta ,abstractmethod

class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def alert(self):
        pass

class WeiXin(Alert):
    def __init__(self):
        print("this is weixin")


if __name__ == "__main__":
    # niko = Son()
    # niko.habbit()

    wx = WeiXin()
    wx.alert()

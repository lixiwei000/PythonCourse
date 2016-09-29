'''
面向对象

'''
# Person继承Object类
class Person(object):

    type = "人类"

    @staticmethod
    def help():
        print("This is static method,we are " , Person.type)

    def __init__(self,name,location):
        self.name = name
        self.__location = location

    def introduce(self):
        print("My name is " + self.name)

    def __heart(self):
        print("This is my private method..")

    @property
    def Bar(self):
        print("This is property methods")

    '''
    推荐:
        访问私有子字段不要使用 对象._类__私有变量 这样的方式
        应该使用 @property设置只读,@私有变量.setter设置只写
    '''
    # 只读特性
    @property
    def Location(self):
        return self.__location

    # 只写特性
    @Location.setter
    def Location(self,location):
        self.__location = location

    # 析构函数
    def __del__(self):
        print(self.__class__.__name__ ,"马上就要被销毁了")

    #
    def __call__(self, *args, **kwargs):
        print("Call is called")

Person.help()

niko = Person("Niko","北京")
niko.introduce()
niko._Person__heart()
 
print(niko.Location)
niko.Location = "上海"
print(niko.Location)
niko()

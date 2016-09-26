class MyException(Exception):
    def __init__(self,error):
        self.error = error

    def __str__(self):
        return self.error

if __name__ == "__main__":
    # try:
    #     s = int(input("输入一个数字"))
    # except ValueError as e:
    #     print(e)
    # else:
    #     print("No Error")
    # finally:
    #     print("Try Catch Finish..")

    try:
        raise MyException("自定义错误")
    except MyException as e:
        print(e)
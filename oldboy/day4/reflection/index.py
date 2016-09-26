# 反射复习
def reflect_review():
    str1 = 'demo'
    str2 = "Foo"

    moudle = __import__(str1)# == import demo
    method = getattr(moudle, str2)
    method()

if __name__ == "__main__":
    data = input("请输入URL:") # Demo:   account/login
    user_space = __import__(data.split("/")[0])
    func = getattr(user_space,data.split("/")[1])
    func()


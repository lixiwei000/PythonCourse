import os
retry_limit = 3
retry_time = 0
account_file = open("./account.txt","rb+")
account_lock_file = open("./account_lock.txt","a+")


def login():
    global retry_time,retry_limit
    while (retry_time < retry_limit):
        username = input("UserName:")
        password = input("Password:")
        account_file.seek(0)
        account_lock_file.seek(0)
        # 判断该账号是否已经被锁定
        for line in account_lock_file.readlines():
            if (line.replace("\n","") == username):
                print("账号已经被锁定")
                return
        for line in account_file.readlines():
            cur_name = line.decode().replace("\n","").split(":")[0]
            cur_pwd = line.decode().replace("\n","").split(":")[1]
            flag = False
            if (username == cur_name):
                flag = True
                if (password == cur_pwd):
                    print("登陆成功！！")
                    retry_time = 0
                    return
                else:
                    print("密码错误")
                    break;
        retry_time += 1
        if (flag == False):
            print("用户名不存在")
    account_lock_file.write(username + "\n")
    print("失败3次，账户被锁定")

if __name__ == '__main__':
    login()
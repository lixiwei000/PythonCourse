'''
1.登陆
    - 输入卡号密码  错误3次锁卡
    - 登陆后功能
        - 取现 5%手续费
        - 查询 查询余额与交易明细
        - 还款 现金还款
        - 转账 可转账到不同账户
        - 退出
2.交易数据 使用Pickle处理交易  生车工交易详单

3.购物网站
    - 选购商品
    - 加入购物车
    - 结算
    - 输入信用卡账户密码
    - 扣款
    - 余额不足
'''
# 高亮输出
def highlight_print(text):
    print('\033[32;1m ' + text + '\033[0m')
# 登陆
def login(username,password):
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/bank_card.txt") as f:
        for line in f.readlines():
            id,name,pwd,money = line.split()[0],line.split()[2],line.split()[1],line.split()[3]
            if name == username and password == pwd:
                highlight_print("欢迎您,编号" + str(id) + ",会员" + str(name) + ",余额" + str(money))
                return line.split()
        highlight_print("登陆失败!请检查用户名密码!")

# 显示菜单
def show_func():
    print(
        '''
        \033[31;1m
        --------------请选择功能--------------
        1. 取现
        2. 查询余额与交易明细
        3. 还款
        4. 转账
        5. 退出
        -------------------------------------
        \033[1m
        ''')

# 取现
def get_money():
    count = input("请输入您要取出的金额:")
    release_money = int(money) - int(count)
    if (release_money < -15000):
        highlight_print("对不起,您无法透支超过15000元")
    else:
        with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/bank_card.txt","r+") as f:
            line = f.readline()
            while line:
                if line.split()[0] == id:
                    start_pos = f.tell() - len(line)
                    # 删除旧的一行数据
                    for i in range(len(line) - 1):
                        f.seek(start_pos + i)
                        f.write(" ")
                    f.flush()
                    f.seek(start_pos)
                    f.write(line.split()[0] + ' '  + line.split()[1] + ' '  + line.split()[2] + ' '  + str(release_money))
                    add_log(line.split()[0],line.split()[1],"取现",count)
                    break
                line = f.readline()

# 添加交易记录
def add_log(id,name,action,money):
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/logs.txt","a+") as f:
        f.write(id + ' '  + name + ' '  + action + ' '  + money + '\n')

# 查询余额与交易明细
def show_details(id):
    result = []
    # 搜集交易详单
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/logs.txt","r") as f:
        for line in f.readlines():
            if line.split()[0] == id:
               result.append(line)
    money = 0
    # 查询余额
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/bank_card.txt","r+") as f:
        for line in f.readlines():
            if line.split()[0] == id:
                money = line.split()[3]
    highlight_print("--------------交易详单--------------")
    for l in result:
        highlight_print(l)
    highlight_print('余额:' + money)

# 还款
def repay():
    money = int(input("请输入您要存款/还款的金额:"))
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/bank_card.txt","r+") as f:
        line = f.readline()
        while line:
            if line.split()[0] == id:
                left_money = int(line.split()[3])
                start_pos = f.tell() - len(line)
                # 删除旧的一行数据
                for i in range(len(line) - 1):
                    f.seek(start_pos + i)
                    f.write(" ")
                f.flush()
                f.seek(start_pos)
                f.write(line.split()[0] + ' '  + line.split()[1] + ' '  + line.split()[2] + ' '  + str(money + left_money))
                add_log(line.split()[0],line.split()[1],"存款/还款",str(money))
                break
            line = f.readline()
# 转账
def send_money(id_from,id_to,money):
    with open("/Users/lixiwei-mac/Documents/IdeaProjects/PythonStudy/oldboy/day4/bank_card.txt","r+") as f:
        line = f.readline()
        while line:
            if line.split()[0] == id_to:
                left_money = int(line.split()[3])
                start_pos = f.tell() - len(line)
                # 删除旧的一行数据
                for i in range(len(line) - 1):
                    f.seek(start_pos + i)
                    f.write(" ")
                f.flush()
                f.seek(start_pos)
                f.write(line.split()[0] + ' '  + line.split()[1] + ' '  + line.split()[2] + ' '  + str(int(money) + left_money))
                f.flush()
                add_log(line.split()[0],line.split()[1],"转入",str(money))
            if line.split()[0] == id_from:
                left_money = int(line.split()[3])
                start_pos = f.tell() - len(line)
                # 删除旧的一行数据
                for i in range(len(line) - 1):
                    f.seek(start_pos + i)
                    f.write(" ")
                f.flush()
                f.seek(start_pos)
                f.write(line.split()[0] + ' '  + line.split()[1] + ' '  + line.split()[2] + ' '  + str(left_money - int(money)))
                f.flush()
                add_log(line.split()[0],line.split()[1],"转出",str(money))
            line = f.readline()
            while line.strip(" ") == "\n":
                line = f.readline()


if __name__ == '__main__':
    id,pwd,name,money = login("Tom","00002")
    show_func()
    no = input("功能:")
    while no != '5':
        if no == '1':
            get_money()
        elif no == '2':
            show_details(id)
        elif no == '3':
            repay()
        elif no == '4':
            id_to = input("请输入转入方编号:")
            money = input("请输入转账金额")
            send_money(id,id_to,money)
        show_func()
        no = input("功能:")
    highlight_print("拜拜~~")

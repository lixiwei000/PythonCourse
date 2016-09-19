'''
购物车程序
输入工资、商品编号 购买商品

需求分析:
1.打印购物车列表
2.输入工资
3.输入购买商品编号
    - 购买成功 扣除金额
    - 购买失败 提示信息
'''

def get_items():
    names = ["《HeadFirst设计模式》","《Python数据分析》","《Spark快速大数据分析》","《大型网站技术架构》","《Java中间件技术》","《Spark机器学习》"]
    prices = [89,65,45,50,66,65]
    return names,prices
def show_list():
    print("=========== Item List ============")
    names,prices = get_items()
    for i in range(len(names)):
        print(i,names[i] + "             $" , prices[i])

show_list()

money = int(input("Please Input Your Salary:\n"))
names,prices = get_items()
while(True):
    n = input("Please Input The No. To Buy.\n")
    if (n == "q"):
        print("Have A Nice Day! Bye.\n")
        break
    n = int(n)
    if (prices[n] > money):
        print("You Need More Money...\n")
        continue
    money -= prices[n]
    print("You Bought", names[n],"Money Left",money,"\n")

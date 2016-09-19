import time
'''
时间的3种表示方式
1.时间戳
2.元组
3.格式化
'''
print(time.time())
print(time.gmtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print("==================================")
# 转换
struc_time = time.strptime("2016-09-18","%Y-%m-%d")
print(struc_time)
print(time.localtime())
 
print(time.mktime(time.localtime()))

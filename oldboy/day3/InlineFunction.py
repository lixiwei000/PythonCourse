# 内置函数
from importlib import reload

# a = []
# print(dir(a))
# print(vars())

# from day2 import dict_test
# print("============ Reload ===============")
# 再次使用import  会被python优化而不重复执行
# from day2 import dict_test
# reload(dict_test)

# 内存地址
# a = 123
# b = 456
# print(id(a))
# print(id(b))

# 其他内置函数
# print(cmp(1,2))
# print(bool(0))
# print(divmod(9,4))
# print(abs(-9))
# print(max(1,2,2,4,5))
# print(min(412,23,423,523,524,535))
# print(sum([1,2,3]))
# print(pow(2,10))
from functools import reduce

print(len("shit"))
print(all([1,2,3,0]))
print(all([1,2,3,4]))
print(any([1,2,3,0]))
print(any([0,0,0,0]))
print("==============")
print(chr(65))
print(ord('A'))
print(hex(20))
print(bin(8))
print(oct(20))
print("==============")
li = ['Niko','Helen','Beleic']
for item in li:
    print(item)

for item in enumerate(li,1):
    print(item)
# 占位符
s = "My name is {0},{1} years old"
print(s.format('NikoBelic',18))
# map函数
for x in map(lambda x:x + 20,[1,2,3,4,5]):
    print(x)
print("==============")
# filter函数
for x in filter(lambda x:x>3,[1,2,3,4,5,6,7,8]):
    print (x)
print("==============")
# reduce函数
print(reduce(lambda x,y : x + y,[x for x in range(101)]))
# zip函数
print("==============")
for x in zip([1,2,3,4],[4,3,2,1],[5,6,7,8],[6,3,6,9]):
    print(x)
# eavl函数
s = "8+8*8"
print(eval(s))
print("==============")
# exec函数 compile函数
code = "for i in range(10):print(i)"
compile_code = compile(code,'',"exec")
exec(compile_code)
print("==============")
# 反射
# 以字符串的形式导入模块
package_name = "sys"
model = __import__(package_name)
print(model.path)
print("==============")
# 以字符串的形式执行函数
package_name = "FunctionTest"
function_name = "dict_show"
model = __import__(package_name)
print(hasattr(model,function_name))
# print(delattr(model,function_name))
func = getattr(model,function_name)
func(name="Niko",age=18)
print("==============")

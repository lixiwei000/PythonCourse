import re

result1 = re.match("\d+","uoasdhqwoudh8923ge")
if result1:
    print(result1.group())
else:
    print("Nothing")

result2 = re.search("\d+","y1289asiodha")
if result2:
    print(result2.group())
else:
    print("Nothing")

result3 = re.findall("\d+","as111udl222iga3svf44iasi")
if result3:
    print(result3)
else:
    print("Nothing")

pattern = re.compile("\d+")
print(pattern.findall("asouidh289p3dh3d8h23"))

pattern = re.compile("(\d+)ffffff(\d+)")
print(pattern.search("123ffffff456").group())
# groups只会去 组 中的结果
print(pattern.search("123ffffff456").groups())

# IP地址匹配练习
s = "21.2.5.sadg.asd.at23opr`KMKSALDKM2.123123.asd.192.168.1.110.asdcxz.214rewa.123.2."
pattern = re.compile("(?:\d{1,3}\\.){3}\d{1,3}")
result = pattern.findall(s)
if result:
    print(result)
else:
    print("Nothing")

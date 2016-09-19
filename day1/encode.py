'''
1.ASCII
8位，1个字节，可表示256个字符
问题：不能表示所有的字符

2.Unicode
16位，2个字节，能够存储65536个字符
问题：任何字符都使用2字节存储，浪费空间

3.UTF-8
长度不定，一般中文是3个字节。



读在内存中 一律都是Unicode编码
但是存储在硬盘中  需要使用UTF-8来存储
'''

s = '你好'
s_u = u'你好'
s_u8 = '你好'.encode("utf-8")
print(len(s))
print(type(s))
print(s)
print(len(s_u))
print(type(s_u))
print(s_u)
print(len(s_u8))
print(type(s_u8))
print(s_u8)

print("===============================================")
name = u'李熙伟'
print(name)
name_u8 = name.encode("utf-8")
print(name_u8)
name_u = name_u8.decode()
print(name_u)
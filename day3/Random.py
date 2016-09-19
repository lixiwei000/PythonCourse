import random
# print(random.random())
# print(random.randint(1,5))
# print(random.randrange(1,5))


def get_verify_card(n):
    card = []
    for i in range(n):
        card.append(chr(get_random()))
    return ''.join(card)

def get_random():
    if random.randint(0,1):
        return ord('0') + random.randint(0,9)
    else:
        return ord('A') + random.randint(0,25)
# 随机验证码
# print(get_verify_card(10))

# MD5加密
import hashlib
hash = hashlib.md5()
hash.update("admin".encode("utf-8"))
print(hash.hexdigest())
# print(hash.hex)


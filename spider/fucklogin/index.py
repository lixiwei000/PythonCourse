import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup
import time
loginUrl = "http://192.168.254.251/0.htm"
checkUrl = "http://192.168.254.251/1.htm"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '192.168.254.251',
    'Origin':'http://192.168.254.251',
    'Referer': 'http://192.168.254.251/0.htm',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
def login(sno, password):

    postValue = {
        'DDDDD' : sno,
        'upass' : password,
        'v6ip'  : '',
        '0MKKey': u'登 陆'.encode(encoding='gb2312')
    }

    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    data = urllib.parse.urlencode(postValue).encode(encoding='UTF8')
    request = urllib.request.Request(loginUrl,data,headers)

    try:
        response = opener.open(request)
        result = response.read().decode('gbk')
        bs = BeautifulSoup(result,"lxml")
        res = bs.find("p").get_text()
        return res
    except Exception as e:
        print(e)

def checkStatus():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(checkUrl,None,headers)

    try:
        response = opener.open(request)
        result = response.read().decode('gbk')
        print(result)
        bs = BeautifulSoup(result,"lxml")
        res = bs.findAll("input")[0]["value"]
        return "已经登录"
    except Exception as e:
        print(e)
        return "需要登陆"

if __name__ == "__main__":
    print('\033[32mNCUT登陆系统\033')
    # sno = input("学号:")
    # pwd = input("密码:")
    sno = "2015309040116"
    pwd = "080015"
    while True:
        if "已经登录" == checkStatus():
            print("已经登陆",time.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            res = login(sno,pwd)
            if "成功" in res:
                print("登陆成功",time.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                print("登陆失败",res,time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)


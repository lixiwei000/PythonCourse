from wsgiref.simple_server import make_server
from oldboy.web.django.config import *

def RunServer(environ,start_response):
    # 根据Url返回不同的信息
    start_response('200 OK',[('Content-Type','text/html')])
    for item in url:
        if item[0] == environ['PATH_INFO']:
            return [('<h1>%s</h1>' % item[1]()).encode('utf-8')]
    return [('<h1>%s</h1>' % '404 Page Not Found').encode('utf-8')]

if __name__ == "__main__":
    httpd = make_server('localhost',9000,RunServer)
    print("Serving HTTP on port 9000")
    httpd.serve_forever()

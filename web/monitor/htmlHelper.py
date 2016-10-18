from monitor.common import *
from django.utils.safestring import mark_safe
import math


class PageInfo(object):

    def __init__(self,currentPage,totalCount,pageSize=5):
        self.currentPage = currentPage
        self.totalCount = totalCount
        self.pageSize = pageSize

    @property
    def start(self):
        return (self.currentPage - 1) * self.pageSize

    @property
    def end(self):
        return self.currentPage * self.pageSize

    @property
    def totalPage(self):
        return math.ceil(self.totalCount / self.pageSize)

def pager(page,totalPage):

    pageMargin = 3
    pageHtml = []
    begin = page - pageMargin if page - pageMargin > 0 else 0
    end = page + pageMargin if page + pageMargin <= totalPage else totalPage
    print(begin,page,end,totalPage)
    pageHtml.append('<a href="/monitor/list?page=%d">首页</a>' % 1)
    if page > 1:
        pageHtml.append('<a href="/monitor/list?page=%d">上一页</a>' % (page-1,))
    for i in range(begin,end):
        if page == i+1:
            html = '<a style="color:red;" href="/monitor/list?page=%d">%d</a>' % (i + 1,i + 1)
        else:
            html = '<a href="/monitor/list?page=%d">%d</a>' % (i + 1,i + 1)
        pageHtml.append(html)
    if page < totalPage:
        pageHtml.append('<a href="/monitor/list?page=%d">下一页</a>' % (page+1,))
    pageHtml.append('<a href="/monitor/list?page=%d">尾页</a>' % totalPage)

    return mark_safe(''.join(pageHtml))

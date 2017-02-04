#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

if __name__ == '__main__':
    # 获取当前时间戳
    now_time_stamp = time.time()
    print now_time_stamp

    # 将时间戳转换为时间数组
    now_localtime = time.localtime(now_time_stamp)
    print now_localtime

    # 将时间数组格式化为各种格式化的时间字符串
    now_format_time = time.strftime('%Y-%m-%d %H:%M:%S',now_localtime)
    print now_format_time
    now_format_date = time.strftime('%Y-%m-%d',now_localtime)
    print now_format_date
    now_format_clock = time.strftime('%H:%M:%S',now_localtime)
    print now_format_clock

    print "=======================================================\n"

    # 设置一个时间字符串
    my_date = "2015-01-01 12:00:00"
    print my_date

    # 将时间字符串转换为时间数组
    my_date_array = time.strptime(my_date,"%Y-%m-%d %H:%M:%S")
    print my_date_array

    # 将时间数组转换为时间戳
    my_date_stamp = time.mktime(my_date_array)
    print my_date_stamp

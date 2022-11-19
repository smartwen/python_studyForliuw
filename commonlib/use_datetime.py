# -*- coding: utf-8 -*-
# @Time : 2022/11/12 11:46
# @Author :liuw
# @File : use_datetime.py
# @Software: PyCharm

'''
datime是python处理日期和时间的标准库
'''
import re
from datetime import datetime, timezone, timedelta

'''
练习
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
请编写一个函数将其转换为timestamp：

# -*- coding:utf-8 -*-

'''


def to_timestamp(dt_str, tz_str):
    # str转换为datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 时差正则分组
    time_diff_re = re.match('(UTC)(.\d{1,2})', tz_str)
    # 取时差
    time_diff = time_diff_re.group(2)
    # 设置时区
    tz_utc = timezone(timedelta(hours=int(time_diff)))
    # 根据时区转化时间 一个datetime类型有一个时区属性tzinfo，但是默认为None 强行给datetime设置一个时区
    dt = dt.replace(tzinfo=tz_utc)
    # 返回时间戳
    return dt.timestamp()
    # 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

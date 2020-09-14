# debugtalk.py
# 获取token
import random
import os
from datetime import date, datetime, timedelta


def get_random_num(wei=1):
    all = 0
    for i in range(wei):
        result = random.randint(1, 9) * (10 ** (wei - i - 1))
        all = all + result
    return all


# 获取一个0-9随机整数
def get_randint(start=0, end=9):
    result = random.randint(start, end)
    return result


def get_time(type=1, day=0):
    '''
    获取当前时间，以及前后几天的时间搓
    :param type: 展示的时间格式
    :param day: 提前或者延后几天的时间
    :return: 提前多少天，或者推迟几天的时间
    '''
    timeDict = {
        1: '%Y-%m-%d %H:%M:%S',  # 2020-01-03 10:12:13
        2: '%Y-%m-%d %H:%M',  # 2020-01-03 10:12
        3: '%Y-%m-%d %H',  # 2020-01-03 10
        4: '%Y-%m-%d',  # 2020-01-03
        5: '%Y-%m',  # 2020-01
        6: '%Y',  # 2020
        7: '%Y%m%d%H%M%S',  # 20200103101213
        8: '%Y%m%d%H%M',  # 202001031012
        9: '%Y%m%d%H',  # 2020010310
        10: '%Y%m%d',  # 20200103
        12: '%Y%m',  # 202001
        13: '%Y',  # 2020
        14: '%m',  # 01
        15: '%d',  # 03
        16: '%Y.%m.%d',  # 2020.01.03
        17: '%Y.%m'  # 2020.01
    }

    now = datetime.now()
    delta = timedelta(days=day)
    if day >= 0:
        time_day = now + delta
    else:
        time_day = now - delta
    return time_day.strftime(timeDict.get(type))

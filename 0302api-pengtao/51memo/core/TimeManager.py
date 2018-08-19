# !/usr/bin/env python
# -*- coding:utf-8 -*-
# TimeManager.py
# author: pengtao

import datetime
import dateutil
from datetime import datetime
from dateutil.relativedelta import relativedelta
# from dateutil.rrule import *    # 导入常量MO,TU,WE,TH,FR


def delay_from_now(years=0, months=None, weekdays=None, weeks=None, days=None, hours=None, minutes=None, seconds=None):
    """ 输入推延的时间，获得推延的日期，返回值为一个datetime.datetime的结构化时间
    注意：days和weekday不可同时输入
    """
    delaied_time = datetime.now() + relativedelta(years=years, months=months, weekday=weekdays, weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return delaied_time     # 返回datetime.datetime结构化时间

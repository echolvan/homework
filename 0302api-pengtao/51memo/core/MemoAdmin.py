# !/usr/bin/env python
# -*- coding:utf-8 -*-
# MemoAdmin.py
# author: pengtao


import pickle
import re
import os
import logging
import datetime
import dateutil
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import mylog
from datetime import datetime
from dateutil.relativedelta import relativedelta

# logging.disable(logging.CRITICAL)
# 禁止所有日志输出


class MemoAdmin:
    """添加MemoAdmin类，作为主体程序，管理Memo类构成的列表，进行Memo的增删改查，处理输入输出"""
    def __init__(self, memo_list):
        self.log = mylog.my_logger(base_path + '\\log\\' + '\
        MemoAdmin_log.log', logging.DEBUG, 'pengtaolog')
        self.memo_list = memo_list

    def add(self):
        "实例化Memo，添加到实例化MemoAdmin的对象里"
        info = input('请输入id，name，thing，date！之间用逗号隔开')
        my_memo = Memo.new_memo(info)
        self.memo_list.append(my_memo)
        print('已经成功添加')
        self.log.info('已经成功添加')

    def delete(self):
        "删除要选择的memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._deadline)
            num += 1
        i = input('请选择你要删除的memo')
        i = int(i)
        del self.memo_list[i]
        print('已经删除')
        self.log.info('已经删除')

    def modify(self):
        "修改memo_list中memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._deadline)
            num += 1
        index = input('请选择你要修改的memo')
        index = int(index)
        while True:
            i = input('请选择修改的内容,name(1),thing(2),date(3)')
            if re.match(r'[1-3]', i):
                break
            else:
                print('请重新输入')
            i = int(i)
        if i == 3:
            self.memo_list[index]._date = input('请输入date')
        elif i == 2:
            self.memo_list[index].thing = input('请输入thing')
        else:
            self.memo_list[index].name = input('请输入name')

    def query(self):
        "查询memo_list里的memo"
        num = 0
        for x in self.memo_list:
            print(num, x.thing, x._deadline)
            num += 1
        y = 1
        while y:
            try:
                i = input('请选择你要查询的memo')
                i = int(i)
                while True:
                    num = input('请选择查询的内容,name(1),thing(2),date(3)')
                    if re.match(r'[1-3]', num):
                        num = int(num)
                        break
                    else:
                        print('请重新输入')
                        self.log.info('请重新输入')
                    num = int(num)
                if num == 3:
                    print(f'{self.memo_list[i]._deadline}')
                elif num == 2:
                    print(f'{self.memo_list[i].thing}')
                else:
                    print(f'{self.memo_list[i].name}')
            except Exception:
                print('输入超出memo范围')
                self.log.info('输入超出memo范围')
            y = int(input('继续查询按1，退出按0'))


class Memo:
    "memo的内容"
    def __init__(self, id, name, thing, date):
        "给memo初始化"
        self.___id = id
        self.name = name
        self.thing = thing
        self._deadline = date
        datetime_str = datetime.now().strftime('%Yy%mm%dd %X')
        datetime_str = datetime_str.replace('y', '年').replace('m\
        ', '月').replace('d', '日')
        self._time_of_adding = datetime_str

    @classmethod
    def new_memo(cls, info):
        "利用输入的info给类实例化"
        __id, name, thing, _date = info.split(',')
        return cls(__id, name, thing, _date)

    @property
    def id(self):
        "把ID设置为只读"
        return self.___id


def memoadmin(user_data):
    "主函数调用方法实现memo_list的增删改查"
    try:
        with open(user_data, 'rb') as f:     # 先尝试打开用户数据文件，如果存在就读取用户数据
            memo_list = pickle.load(f)
    except Exception:
        with open(user_data, 'wb') as f:     # 没有用户数据文件就新建一个用户数据文件
            memo_list = []
            pickle.dump(memo_list, f)
    admin = MemoAdmin(memo_list)             # admin是备忘录管理对象
    y = 1
    while y:
        choice = input('请选择操作：add（1），del（2），modify（3），query（4）')
        while 1:                              # 保证选择在1-4中
            if re.match(r'[1-4]', choice):    # 在while循环里判断输入是否超出操作范围，提高容错率
                choice = int(choice)
                break
            else:
                print('请重新输入')
                choice = int(choice)
# 每个数字对应不同的增删改查的操作
        if choice == 1:
            admin.add()
        elif choice == 2:
            admin.delete()
        elif choice == 3:
            admin.modify()
        else:
            admin.query()

        y = int(input('继续（1）退出(0)'))
        if y == 0:
            print(admin.memo_list)
        with open(user_data, 'wb') as f:
            pickle.dump(admin.memo_list, f)



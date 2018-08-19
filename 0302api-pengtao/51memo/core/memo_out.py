# !/usr/bin/env python
# -*- coding:utf-8 -*-
# memo_out.py
# author: pengtao

import pickle
import re
import os
import json


class MemoOut:
    """根据输入内容选择发送整年，整月数据给特定人物"""
    def __init__(self, filepath):
        self.filepath = filepath

    def out_all_a_year(self):
        """"将整个年的数据从用户数据文件中筛选出来存入一个文件"""
        new_data_path = os.path.dirname(self.filepath)
        with open(self.filepath, 'rb') as f:
            data = pickle.load(f)
        years = []
        for memo in data:
            year = re.match('(.*?)年', memo._time_of_adding).group(1)
            years.append(year)
        years = list(set(years))
        print(f'这里有以下年份的memo{years}')
        while True:
            load_data = input('请输入年份')
            if load_data in years:
                memo_list = {}
                for memo in data:
                    if re.match(load_data + '年', memo._time_of_adding):
                        memo_list[memo._time_of_adding] = {
                            "name": memo.name,
                            "thing": memo.thing,
                            "date": memo._deadline
                            }
                with open(new_data_path + '/' + load_data + '\
                data.json', 'w') as f:
                    json.dump(json.dumps(memo_list), f)
                break
            else:
                print('重新输入')
        data_path = new_data_path + '/' + load_data + 'data.json'
        print('成功发送')
        return data_path, load_data

    def out_all_a_month(self):
        """"将整个月的数据从用户数据文件中筛选出来存入一个文件"""
        new_data_path = os.path.dirname(self.filepath)
        with open(self.filepath, 'rb') as f:
            data = pickle.load(f)
        months = []
        for memo in data:
            month = re.search('年(.*?月)', memo._time_of_adding).group(1)
            months.append(month)
        months = list(set(months))
        print(f'这里有以下年份的memo{months}')
        while True:
            load_data = input('请输入月份')
            if load_data in months:
                memo_list = {}
                for memo in data:
                    if re.search(load_data, memo._time_of_adding):
                        memo_list[memo._time_of_adding] = {
                            "name": memo.name,
                            "thing": memo.thing,
                            "date": memo._deadline
                            }
                with open(new_data_path + '/' + load_data + '\
                data.json', 'w') as f:
                    json.dump(json.dumps(memo_list), f)
                break
            else:
                print('重新输入')
        data_path = new_data_path + '/' + load_data + 'data.json'
        print('成功发送')
        return data_path, load_data

    def get_all_a_month(self):
        """"查询接口，可以根据月份返回json数据"""
        with open(self.filepath, 'rb') as f:
            data = pickle.load(f)    # 从数据文件中读取数据
        months = []
        for memo in data:            # 从用户的数据文件中查询有哪些月份
            month = re.search('年(.*?月)', memo._time_of_adding).group(1)
            months.append(month)
        months = list(set(months))   # 月份去重
        print(f'这里有以下年份的memo{months}')

        while True:
            # 按月份把memo的数据提取出来并返回json数据
            load_data = input('请输入月份')
            if load_data in months:
                memo_list = {}
                for memo in data:
                    if re.search(load_data, memo._time_of_adding):
                        memo_list[memo._time_of_adding] = {
                            "name": memo.name,
                            "thing": memo.thing,
                            "date": memo._deadline
                            }
                json_data = json.dumps(memo_list)
                break
            else:
                print('重新输入')
        return json_data


def main():
    a = MemoOut(r'C:\Users\Administrator\Desktop\my_code\0301office-pengtao\51memo\db\yun.pkl')
    a.out_all_a_year()
if __name__ == '__main__':
    main()
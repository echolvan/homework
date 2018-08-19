# !/usr/bin/env python
# -*- coding:utf-8 -*-
# config.py
# set config for program
# author: pengtao


import configparser
import os
import sys
import logging
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import mylog


# logging.disable(logging.CRITICAL)
# 禁止所有日志输出
def config(data_file_path):
    """将传来的章节名，数据名，数据文件类型，数据文件路径保存到配置文件中，配置文件命名为common.ini"""
    data_path = os.path.dirname(data_file_path)
    # 数据文件目录
    section_name = (os.path.splitext(data_file_path)[0]).split(os.path.sep)[-1]
    # 章节名
    data_name = (os.path.splitext(data_file_path)[0]).split(os.path.sep)[-1]
    # 数据文件名字
    data_type = os.path.splitext(data_file_path)[1].strip('.')
    # 数据文件类型
    log = mylog.my_logger(base_path + '\\log\\' + 'confi\
    g_log.log', logging.DEBUG, 'pengtaolog')
    config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(config_path + r'\conf', 'common.ini')
    # 配置文件名路径
    try:                                          # 尝试打开配置文件并添加个人配置，若无配置文件这生成
        config = configparser.ConfigParser()
        config.read(config_path)                  # 打开配置文件
        config.add_section(section_name)          # 添加用户个人章节
        items_list = {'data_name': data_name, 'data\
        _type': data_type, 'data_path': data_path}
        # 配置项
        for k, v in items_list.items():             # 写入用户个人配置
            config.set(section_name, k, v)
    except Exception:                              # 生成配置文件
        config = configparser.ConfigParser()
        config.add_section(section_name)
        items_list = {'data_name': data_name, 'data_\
        type': data_type, 'data_path': data_path}
        for k, v in items_list.items():
            config.set(section_name, k, v)
    with open(config_path, 'w') as f:              # 写入个人配置信息并保存配置文件
        config.write(f)
        log.debug('配置信息已存入配置文件')


def main():
    """主函数调用config（）函数进行调试"""
    # config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config(r'C:\Users\Administrator\Desktop\my_code\exercise\
    homework\51memo\db\pengtao.pkl')


if __name__ == '__main__':
    main()

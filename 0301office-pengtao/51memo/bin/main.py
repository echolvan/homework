# !/usr/bin/env python
# -*- coding:utf-8 -*-
# main.py
# invoke other file of py to realize functions
# author: pengtao

import os,sys,logging
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from core import login, MemoAdmin, config, mylog, memo_out, send_email


# logging.disable(logging.CRITICAL)
# 禁止所有日志输出
def main():
    log = mylog.my_logger(BASE_PATH + '\\log\\' + 'execute_log.log', logging.DEBUG, 'pengtaolog' )
    # 打开日志
    data_file_path = login.register(log)      # 用户登录，返回该用户数据文件名
    log.info('用户登录，返回该用户数据文件名')
    memo_o = memo_out.MemoOut(data_file_path)  # 生成Memo_Out对象
    log.info('利用数据文件名进行操作')
    
    if len(sys.argv) >= 2:
        if sys.argv[1] in ['-se', '--send_email']:   # 系统命令行参数调用发邮件
            log.debug('系统命令行参数调用发邮件')
            while True:
                try:
                    ask = input('输出整年（year），整月（month）')
                    if ask == 'year':
                        data_path, choose = memo_o.out_all_a_year()
                        log.debug('获得json文件的路径，和用户年份选择')
                    if ask == 'month':
                        data_path, choose = memo_o.out_all_a_month()
                        log.debug('获得json文件的路径，和用户月份选择')
                    break
                except Exception:
                    print('输入错误')
            send_email.send_email_attach(f'这是{choose}的数据，请查看！', data_path, 'lvan1033@live.cn')  # 发送给特定人物的邮件

    if len(sys.argv) >= 2:
        if sys.argv[1] in ['-rj', '--return_json']:    # 系统命令行参数调用返回json数据
            log.debug('系统命令行参数调用返回json数据')
            print(memo_o.get_all_a_month())      # 打印按月份返回的json数据

    MemoAdmin.memoadmin(data_file_path)       # 利用数据文件名进行操作

    config.config(data_file_path)             # 用户配置文件生成
    log.info('用户配置文件生成')


if __name__ == '__main__':
    main()
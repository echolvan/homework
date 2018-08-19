# !/usr/bin/env python
# -*- coding:utf-8 -*-
# mylog.py
# author: pengtao

import logging


# logging.basicConfig(level = logging.DEBUG, format ='%(levelname)s - %(asctime)s - %(lineno)s - %(filename)s - %(name)s- %(message)s ')
# logging.debug('这是一条debug信息，开始使用日志了')
# logging.info('这是一条info信息，开始使用日志了!')
# logging.warning('这是一条waring信息，开始使用日志了！')
# logging.error('这是一条error信息')
# logging.critical('这是一条critical信息')
# used = 'hjyguangzhou'
# logging.warning('%s python', used)


def my_logger(logger_file,  level=logging.WARNING, logger_name='ps_pictures-log'):
    """建立日志对象"""
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    # 创建控制台console handler
    ch = logging.StreamHandler()
    ch.setLevel(level=level)
    fh = logging.FileHandler(filename=logger_file, encoding='utf-8')
    fh.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s [line%(lineno)d]%(levelname)s %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    # 没有该日志文件可以创一个再写进去，有日志文件就在该日志文件中继续写
    return logger

log = my_logger('control_line.log', logging.DEBUG, 'control_line')


def main():
    log = my_logger('./log/'+'mylog.log', logging.DEBUG, 'pengtaolog')
    log.debug('终于完事了')
    log.info('这是info哟')
    log.warning('这是warning哟')
    log.error('这是error哟')
    log.critical('这是一条critical信息哟')


if __name__ == '__main__':
    main()
import logging

# logging.basicConfig(level = logging.DEBUG, format ='%(levelname)s - %(asctime)s - %(lineno)s - %(filename)s - %(name)s- %(message)s ')
# logging.debug('这是一条debug信息，开始使用日志了')
# logging.info('这是一条info信息，开始使用日志了!')
# logging.warning('这是一条waring信息，开始使用日志了！')
# logging.error('这是一条error信息')
# logging.critical('这是一条critical信息')
# used = 'hjyguangzhou'
# logging.warning('%s python', used)


def my_logger(logger_file,  level, logger_name='pengtao-log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.DEBUG)
    fh = logging.FileHandler(filename=logger_file, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(filename)s [line%(lineno)d]%(levelname)s %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


def main():
    log = my_logger('mylog', logging.DEBUG, 'pengtaolog')
    log.debug('终于完事了')
    log.info('这是info哟')
    log.warning('这是warning哟')
    log.error('这是error哟')
    log.critical('这是一条critical信息哟')


if __name__ == '__main__':
    main()
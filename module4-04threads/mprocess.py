# !/usr/bin/env python
# -*- coding:utf-8 -*-
# mprocess.py
# author: pengtao

import concurrent
import re
import time
import sys
import logging
import requests
import spider
from spider import Extract_link
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)-10s: %(message)s', filename='multipro.log')


class MultiCrawler:
    def __init__(self, url):
        self.links = Extract_link(url).extract_link()

    def crawler(self, link):
        """爬取url"""
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000"}
        try:
            r = requests.get(url=link,  headers=headers, timeout=7)
            if r.status_code < 300 and r.status_code >= 200:
                return link, r.status_code
            else:
                return None
        except Exception as e:
            print(e)

    def start_cralw(self):
        """利用线程池进行爬取"""
        start_time = time.time()
        try:
            with ThreadPoolExecutor(10) as executor:
                future_results = executor.map(self.crawler, self.links, timeout=120)
                for future in future_results:
                    print(future)
        except Exception as e:
            print(e)
        print('all cost {} seconds'.format(time.time()-start_time))
        logging.debug('All have done!')


def main():
    help = """该模块仅能传一个参数
    参数有：帮助（-h,--help）
            输入url
            输入url参数应带有协议名，比如：http://example.url"""
    if len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '--help']:
            print(help)
        elif re.match('http://|https://', sys.argv[1]):
            m = MultiCrawler(sys.argv[1])
            m.start_cralw()
        else:
            print('输入url错误')
    else:
        print('您输入参数错误：仅能输入一个参数，且必须输入一个参数')
        print('参数-h,--help,查看帮助')
        print('参数url,输入url')

if __name__ == '__main__':
    main()
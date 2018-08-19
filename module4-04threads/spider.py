# !/usr/bin/env python
# -*- coding:utf-8 -*-
# spider.py
# author: pengtao

import re
import csv
import requests


class Extract_link:
    def __init__(self, url):
        """初始化时访问url并将response的内容存储起来"""
        self.url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000"
            }
        r = requests.get(url=self.url,  headers=headers)
        if r.status_code == 200:
            self.text = r.text
        else:
            self.text = None

    def extract_link(self):
        """从页面中分析出链接"""
        if self.text is not None:
            regex_href = re.compile(r' href="(.*?)"')
            regex_src = re.compile('src="(.*?)"')
            regex_url = re.compile("url='(.*?)'")
            hrefs = list(filter(lambda x: re.match('http://|https://', x), regex_href.findall(self.text)))
            srcs = list(filter(lambda x: re.match('http://|https://', x), regex_src.findall(self.text)))
            urls = list(filter(lambda x: re.match('http://|https://', x), regex_url.findall(self.text)))
            with open('extract_link.csv', 'w+') as f:
                writer = csv.writer(f)
                writer.writerow(['No', 'link'])
                for a, link in enumerate(hrefs):
                    writer.writerow([a, link])
                for b, link in enumerate(srcs):
                    writer.writerow([a+b+1, link])
                # for c, link in enumerate(urls):
                #     writer.writerow([a+b+c+2, link])
            return hrefs + srcs + urls


def main():
    Extract_link('https://www.autohome.com.cn/beijing/').extract_link()


if __name__ == '__main__':
    main()
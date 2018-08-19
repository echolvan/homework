#!/usr/bin/env Python
# -*- coding:utf-8 -*-


import json


def w_json():
    dic = {
        'country':'cn',
        'capital':'beijing',
        'language':'chinese'
    }
    with open(r'C:\Users\Administrator\Desktop\my_code\03web\test.json', 'w') as f:
        f.write(json.dumps(dic))


def w_html():
    html ="""<html>
    <body>
    <h1>hello</h1>
    <h2>homepage页面显示啦！</h2>
    </body>
    </html>
    """
    with open(r'C:\Users\Administrator\Desktop\my_code\03web\homepage.html', 'w') as f:
        f.write(html)


def main():
    w_json()
    w_html()

if __name__ == '__main__':
    main()
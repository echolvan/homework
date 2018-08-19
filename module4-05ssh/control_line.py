# !/usr/bin/env python
# -*- coding=utf-8 -*-
# 包装命令行工具成类

import argparse


class ControlLine:
    def __init__(self):
        """初始化parse对象，建立分组"""
        self.usage = """服务器管理CLI工具，实现如下功能：
    - 使用-h查看帮助
    - 使用-s后面添加ip或主机名去连接和登陆服务器，多个参数时候直接连接多个
    - 使用-u上传文件
    - 使用-d下载文件
    - 使用-c进入交互控制台，可以进行常见shell命令的交互"""
        self.parse = argparse.ArgumentParser(usage=self.usage)
        self.group1 = self.parse.add_argument_group('基础命令'.center(20, '-'))
        self.group2 = self.parse.add_argument_group('交互控制'.center(20, '-'))
        # filename
        self.parse.add_argument(dest='filename', nargs='*', help='传入参数列表')

    def group(self):
        """将登录-s，上传-u，下载-d命令分入一组
        将-c交互控制分入二组"""
        # shell
        self.group1.add_argument('-s', '--shell', dest='shell', action='store_true', help='添加ip或主机名去连接和登录服务器，多个参数时候直接连接多个')

        # upload
        upload_help = '使用-u上传文件,第一个参数为上传文件路径(local_file_path),第二参数为远程服务器保存文件路径(file_path_in_server),若无参数则批量上传upload文件夹中的文件'
        self.group1.add_argument('-u', '--upload', dest='upload', action='store_true', help=upload_help)

        # download
        download_help = '使用-d下载文件,第一参数为远程服务器保存文件路径(file_path_in_server),第一个参数为上传文件路径(local_file_path),若只有一个参数且为文件夹时则为批量操作'
        self.group1.add_argument('-d', '--download', dest='download', action='store_true', help=download_help)

        # console
        console_help = '使用-c进入交互控制台，可以进行常见的shell命令的交互'
        self.group2.add_argument('-c', '--console', dest='console', action='store_true', help=console_help)

    def output(self):
        """输出控制台信息"""
        # self.parse.print_help()
        self.args = self.parse.parse_args()
        # print(self.args)
        # if self.args:
            # print(self.args.upload)
            # print(self.args.download)

    def run(self):
        """执行控制台的操作"""
        self.group()
        self.output()


def main():
    CLI = ControlLine()
    CLI.run()

if __name__ == '__main__':
    main()
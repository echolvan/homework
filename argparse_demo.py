# command line demo
# 解析命令行

import argparse

parse = argparse.ArgumentParser('介绍usage')

# 分组命令
group1 = parse.add_argument_group('-----------group1', '基础命令')

# verbose   # 一长串命令的意思
group1.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='针对这个命令的解释')
# dest为解析的目标
# action = 'store_true'表示参数如果被调用就赋值为true
# help 针对这个命令的解释

# filename
parse.add_argument(dest='filename', nargs='*', help='文件列表')

# upload
parse.add_argument('-u', '--upload', dest='upload', action='store', metavar='简介说明upload', help='upload file')

# download
parse.add_argument('-d', '--download', dest='download', action='append', help='download file')
# 但是这样来写的话，命令行应该这样写：python argparse_demo.py -d filepath1 -d filepath2


parse.print_help()
args = parse.parse_args()
print(args)
print(args.verbose)
print(args.upload)
print(args.download)
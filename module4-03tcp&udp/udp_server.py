#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# udp_server.py


import socket


HOST = ''  # localhost:本机，ip值 ， 空：任意主机都可访问，
# 我这里是用本机作为服务器，让虚拟机进行访问，设置ip值就那个ip的客户端就能访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # udp相关参数

# 绑定ip和端口
sock.bind(ADDR)

# 发送和接收数据
while True:
    # 因为我不知道什么时候来数据啊，就循环运行着吧
    try:
        print('utp server start...')
        data, addr = sock.recvfrom(BUFSIZE)  # 接收一个缓冲大小，我这里bufsize等于1024bytes
        # sock.recvfrom返回的是接收数据和哪来的地址
        print('get', data.decode('utf-8'))
        sock.sendto(data, addr)  # 我把我收到的东西返回给客户端
    except Exception as e:
        print(e)

# 关闭socket
sock.close()
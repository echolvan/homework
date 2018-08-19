#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# tcp_client.py

import socket


HOST = '192.168.202.1'  # localhost:本机，ip值 ， 空：任意主机都可访问，
# 我这里是用本机作为服务器，让虚拟机进行访问，设置ip值就那个ip的客户端就能访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # udp相关参数

# 连接服务器
sock.connect(ADDR)


# 收发数据
while True:
    try:
        msg = input('>>>')
        if not msg:
            break
        sock.sendall(msg.encode())  # 发送数据
        answer = sock.recv(BUFSIZE)   # 接收数据
        print('get answer: ', answer.decode())
    except Exception as e:
        print(e)

# 关闭socket
sock.close()
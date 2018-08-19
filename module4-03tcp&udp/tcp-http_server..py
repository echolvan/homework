#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# tcp_server.py


import socket


HOST = ''  # localhost:本机，ip值 ， 空：任意主机都可访问，
# 我这里是用本机作为服务器，让虚拟机进行访问，设置ip值就那个ip的客户端就能访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # udp相关参数
# AF_INET表示使用ipv4，由于tcp协议使用的是字节流传输，所以sock_stream
# 服务器绑定地址
sock.bind(ADDR)

# 监听连接个数
sock.listen(1)
print('tcp服务启动')

# 循环发送和接收数据

# 等待连接
while True:
    print('等待连接')
    connection, addr = sock.accept()   # connection也是一个socket
    print('成功连接: ', addr)
    # 循环等待接收
    data = connection.recv(BUFSIZE)   #recv()是用于tcp， recvfrom用于udp
    # print(data)
    while data:
        try:
            request_header = data.decode('utf-8')
            first_info = request_header.splitlines()[0]
            method, path, protocol = first_info.split(' ')
            print('收到数据: ', data.decode())
            print(f'转跳到{path}')
            response = """HTTP/1.1 200 OK

            <h1>hello</h1>
            <h2>how are you </h2>
            """.encode()
            connection.sendall(response)  # 在这里处理数据,然后发给客户端
            print('成功发送给客户端')
            connection.close()
            break
        except Exception as e:
            print(e)
            connection.close()
            break

# 关闭socket
sock.close()